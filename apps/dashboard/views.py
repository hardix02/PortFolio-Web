"""
Dashboard views for displaying GitHub and Wakatime activity statistics.
Provides developer activity insights with caching for performance.
"""

import logging
from typing import Dict, Optional, Any
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from datetime import datetime, timedelta
import random
from apps.core.base_views import BaseView
from apps.seo.mixins import DashboardSEOMixin
from apps.dashboard.github_api import GitHubClient, GitHubStatsCalculator
from apps.dashboard.wakatime_api import WakatimeClient, WakatimeStatsCalculator

logger = logging.getLogger(__name__)

# Cache timeout: 3 hours
CACHE_TIMEOUT = 10800


class DashboardView(DashboardSEOMixin, BaseView):
    """
    Dashboard view displaying GitHub and Wakatime statistics.
    Shows coding activity, contribution patterns, and development insights.
    """
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """Build context with GitHub and Wakatime data."""
        context = super().get_context_data(**kwargs)
        
        # Get GitHub statistics
        github_data = self._get_github_data()
        if github_data:
            context.update(github_data)
        else:
            context['github_activity'] = None
            context['github_last_update'] = None
        
        # Get Wakatime statistics
        wakatime_stats = self._get_wakatime_data()
        context['wakatime_stats'] = wakatime_stats

        # Add SEO data from mixin
        mixin_context = super(DashboardView, self).get_context_data(**context)
        context.update(mixin_context)
        
        return context

    # def _get_github_data(self) -> Optional[Dict]:
    #     """Get GitHub statistics with caching."""
    #     cache_key = 'github_activity_data'
    #     github_data = cache.get(cache_key)
    #
    #     if not github_data:
    #         try:
    #             about_data = self.get_about_data()
    #             github_client = GitHubClient(
    #                 username=about_data['username'],
    #                 access_token=settings.ACCESS_TOKEN
    #             )
    #             github_activity = github_client.get_contribution_data()
    #
    #             if github_activity and 'data' in github_activity:
    #                 user_data = github_activity['data']['user']
    #                 calendar_data = user_data['contributionsCollection']['contributionCalendar']
    #                 contribution_weeks = calendar_data['weeks']
    #                 total_contributions = calendar_data['totalContributions']
    #
    #                 github_stats = GitHubStatsCalculator.calculate_stats(
    #                     contribution_weeks, total_contributions
    #                 )
    #
    #                 github_data = {
    #                     'github_activity': github_activity,
    #                     'total_contributions': total_contributions,
    #                     'this_week': github_stats['this_week'],
    #                     'best_day': github_stats['best_day'],
    #                     'average': f"{github_stats['average']}",
    #                     'longest_streak': github_stats['longest_streak'],
    #                     'current_streak': github_stats['current_streak'],
    #                     'github_last_update': timezone.now().strftime('%B %d, %Y %I:%M %p')
    #                 }
    #
    #                 cache.set(cache_key, github_data, CACHE_TIMEOUT)
    #             else:
    #                 logger.error("GitHub activity data is missing or malformed.")
    #                 github_data = None
    #         except Exception as e:
    #             logger.error(f"Error fetching GitHub data: {e}")
    #             github_data = None
    #
    #     return github_data
    
    # def _get_wakatime_data(self) -> Optional[Dict]:
    #     """Get Wakatime statistics with caching."""
    #     cache_key = 'wakatime_activity_data'
    #     wakatime_stats = cache.get(cache_key)
    #
    #     if not wakatime_stats:
    #         try:
    #             wakatime_client = WakatimeClient(api_key=settings.WAKATIME_API_KEY)
    #             wakatime_activity = wakatime_client.get_activity_data()
    #
    #             if wakatime_activity:
    #                 wakatime_stats = WakatimeStatsCalculator.calculate_stats(wakatime_activity)
    #                 if wakatime_stats:
    #                     cache.set(cache_key, wakatime_stats, CACHE_TIMEOUT)
    #                 else:
    #                     logger.error("Wakatime statistics calculation failed.")
    #             else:
    #                 logger.error("Wakatime activity data is missing or malformed.")
    #                 wakatime_stats = None
    #         except Exception as e:
    #             logger.error(f"Error fetching Wakatime data: {e}")
    #             wakatime_stats = None
    #     else:
    #         logger.info("Using cached Wakatime statistics.")
    #
    #     return wakatime_stats

    def _get_github_data(self) -> Optional[Dict]:
        weeks = []
        today = datetime.now()
        one_year_ago = today - timedelta(weeks=52)

        for i in range(53):
            week_start = one_year_ago + timedelta(weeks=i)
            days = []
            for d in range(7):
                date = week_start + timedelta(days=d)
                # random contributions 0-30 for color variation
                contribution_count = random.choice(
                    [0, random.randint(1, 8), random.randint(9, 21), random.randint(22, 30), random.randint(31, 40)])
                days.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'contributionCount': contribution_count
                })
            weeks.append({'contributionDays': days})

        dummy_github_data = {
            'github_activity': {
                'data': {
                    'user': {
                        'contributionsCollection': {
                            'contributionCalendar': {
                                'weeks': weeks,
                                'totalContributions': 1234
                            }
                        }
                    }
                }
            },
            'total_contributions': 1234,
            'this_week': 12,
            'best_day': 50,
            'average': "3.4",
            'longest_streak': 45,
            'current_streak': 10,
            'github_last_update': timezone.now().strftime('%B %d, %Y %I:%M %p')
        }

        return dummy_github_data

    def _get_wakatime_data(self) -> Dict:
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Format dates as "June 29, 2025"
        start_date = start_of_week.strftime("%B %d, %Y")
        end_date = end_of_week.strftime("%B %d, %Y")
        best_day_date = (today - timedelta(days=1)).strftime("%B %d, %Y") if today.weekday() == 0 else today.strftime("%B %d, %Y")

        return {
            'start_date': start_date,
            'end_date': end_date,
            'daily_average': '1 hrs 56 mins',
            'this_week_coding': '13 hrs 35 mins',
            'best_day_date': best_day_date,
            'best_day_coding': '3 hrs 45 mins',
            'all_time_start': 'January 1, 2023',
            'all_time_coding': '1,277 hrs 41 mins',
            'last_update_time': '1 hour ago',
            'top_3_languages': [
                {'name': 'C#', 'percent': 45},
                {'name': 'Python', 'percent': 30},
                {'name': 'MQL', 'percent': 25}
            ],
            'top_1_category': [
                {'name': 'Coding', 'percent': 100}
            ],
            'top_2_os': [
                {'name': 'Windows', 'percent': 70},
                {'name': 'Mac', 'percent': 30}
            ]
        }

