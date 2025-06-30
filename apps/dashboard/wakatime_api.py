"""
Wakatime API client for fetching coding activity data.
Separated from views for better organization and reusability.
"""

import logging
import requests
import pytz
from datetime import datetime
from typing import Dict, Optional
from django.utils import timezone

logger = logging.getLogger(__name__)


class WakatimeClient:
    """Client for interacting with Wakatime API."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://wakatime.com/api/v1"
        self.timeout = 10
    
    def get_activity_data(self) -> Optional[Dict]:
        """Fetch Wakatime activity data for last 7 days and all time."""
        try:
            last_7_days_url = f"{self.base_url}/users/current/stats/last_7_days?api_key={self.api_key}"
            all_time_url = f"{self.base_url}/users/current/all_time_since_today?api_key={self.api_key}"
            
            last_7_days_response = requests.get(last_7_days_url, timeout=self.timeout)
            all_time_response = requests.get(all_time_url, timeout=self.timeout)
            
            last_7_days_response.raise_for_status()
            all_time_response.raise_for_status()
            
            return {
                'last_7_days': last_7_days_response.json(),
                'all_time': all_time_response.json()
            }
        except requests.RequestException as e:
            logger.error(f"Wakatime API error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in Wakatime API: {e}")
            return None


class WakatimeStatsCalculator:
    """Calculator for processing Wakatime API data into statistics."""
    
    @staticmethod
    def _convert_to_gmt7(iso_string: str) -> datetime:
        """Convert ISO string to GMT+7 timezone."""
        try:
            utc_dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
            utc_dt = utc_dt.replace(tzinfo=pytz.UTC)
            gmt7 = pytz.timezone('Asia/Jakarta')  # GMT+7
            return utc_dt.astimezone(gmt7)
        except Exception as e:
            logger.error(f"Error converting timezone: {e}")
            return timezone.now()
    
    @staticmethod
    def _format_time(seconds: float) -> str:
        """Format seconds into hours and minutes."""
        try:
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            return f"{hours} hrs {minutes} mins"
        except (TypeError, ValueError):
            return "0 hrs 0 mins"
    
    @staticmethod
    def calculate_stats(data: Dict) -> Optional[Dict]:
        """Calculate comprehensive Wakatime statistics."""
        if not data or 'last_7_days' not in data or 'all_time' not in data:
            return None
        
        try:
            last_7_days = data['last_7_days']['data']
            all_time = data['all_time']['data']
            
            # Calculate time differences
            modified_at = WakatimeStatsCalculator._convert_to_gmt7(last_7_days['modified_at'])
            now_gmt7 = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
            time_diff = now_gmt7 - modified_at
            hours_ago = max(0, int(time_diff.total_seconds() / 3600))
            
            # Process top languages
            top_languages = []
            for lang in last_7_days.get('languages', [])[:3]:
                top_languages.append({
                    'name': lang.get('name', 'Unknown'),
                    'percent': lang.get('percent', 0),
                    'time': lang.get('text', '0 mins')
                })
            
            # Process top category
            top_category = []
            for category in last_7_days.get('categories', [])[:1]:
                top_category.append({
                    'name': category.get('name', 'Unknown'),
                    'percent': category.get('percent', 0),
                    'time': category.get('text', '0 mins')
                })
            
            # Process top operating systems
            top_os = []
            for os in last_7_days.get('operating_systems', [])[:2]:
                top_os.append({
                    'name': os.get('name', 'Unknown'),
                    'percent': os.get('percent', 0),
                    'time': os.get('text', '0 mins')
                })
            
            return {
                'created_at': WakatimeStatsCalculator._convert_to_gmt7(
                    last_7_days.get('created_at', '')
                ).strftime('%B %d, %Y'),
                'updated_at': WakatimeStatsCalculator._convert_to_gmt7(
                    last_7_days.get('modified_at', '')
                ).strftime('%B %d, %Y'),
                'start_date': WakatimeStatsCalculator._convert_to_gmt7(
                    last_7_days.get('start', '')
                ).strftime('%B %d, %Y'),
                'end_date': WakatimeStatsCalculator._convert_to_gmt7(
                    last_7_days.get('end', '')
                ).strftime('%B %d, %Y'),
                'daily_average': WakatimeStatsCalculator._format_time(
                    last_7_days.get('daily_average_including_other_language', 0)
                ),
                'this_week_coding': WakatimeStatsCalculator._format_time(
                    last_7_days.get('total_seconds_including_other_language', 0)
                ),
                'best_day_date': WakatimeStatsCalculator._convert_to_gmt7(
                    last_7_days.get('best_day', {}).get('date', '')
                ).strftime('%B %d, %Y'),
                'best_day_coding': last_7_days.get('best_day', {}).get('text', '0 mins'),
                'top_3_languages': top_languages,
                'top_1_category': top_category,
                'top_2_os': top_os,
                'all_time_coding': all_time.get('text', '0 mins'),
                'all_time_start': WakatimeStatsCalculator._convert_to_gmt7(
                    all_time.get('range', {}).get('start', '')
                ).strftime('%B %d, %Y'),
                'all_time_end': WakatimeStatsCalculator._convert_to_gmt7(
                    all_time.get('range', {}).get('end', '')
                ).strftime('%B %d, %Y'),
                'last_update_time': f"{hours_ago} hours ago"
            }
        
        except Exception as e:
            logger.error(f"Error calculating Wakatime stats: {e}")
            return None