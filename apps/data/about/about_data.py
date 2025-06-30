from django.utils import timezone
from django.conf import settings

class AboutData:
    @staticmethod
    def is_working_hours():
        now = timezone.localtime()
        
        is_weekday = now.weekday() < 5
        is_work_hour = 9 <= now.hour < 15

        return is_weekday and is_work_hour

    @classmethod
    def get_about_data(cls):
        return {
            "name": "Hardik Baraiya",
            "first_name": "Hardik",
            "last_name": "Baraiya",
            "username": "hardix02",
            "image_url": f"{settings.BASE_URL}/static/img/hardix.webp",
            #   D:\Projects\Portfolio's\ridwaanhall-com\staticfiles\img\hardikbaraiya.webp
            "personal_website": "https://hardikbaraiya.com",
            "cv": "https://drive.google.com/file/d/1ZExKiINAXcA3FZk9NAJ-oV6wgeUns0Vf/view?usp=sharing",
            "cv_template": "https://docs.google.com/document/d/1Sv2VQ95fDn-0a_8lOZxBuFAZ--gJrw7u5EQ-_SLUfpo",
            "role": "Software Engineer",
            "is_active": cls.is_working_hours(),
            # "is_active": False,
            "short_description": "Coding by day, memorizing Shreemad Bhagvat Gita by heart—who else but me?",
            "short_bio": "I'm a passionate C# programmer with a love for Python, web development, and open-source. I focus on building practical Applications that solves real problems.",
            "short_cta": "Let's whip up something epic that'll leave everyone stunned!",
            "long_description": "I'm a machine learning engineer and web developer, building AI apps and slick websites that solve real problems. I've memorized nearly 30 Juz of the Gita, which has wired me for grit, focus, and discipline. I've mentored 50+ coders at DBS Foundation's Coding Camp and guided 100+ interns at GAOTek Inc. I've shipped 30+ projects using TensorFlow, PyTorch, and more. I'm all in on using AI to tackle big challenges fast, growing Copilot ID, and dropping value in open-source communities.",
            "stories": [
                "Hi, I'm Hardik also known as hardix — a C# programmer, MQL Experts, and open-source contributor with a focus on Desktop and web development. Based in Central Java, Indonesia, I lead Copilot ID, where I build intelligent systems and modern web apps using Django, Flask, and cutting-edge AI tools to solve real-world problems with purpose.",
                "On a personal note, I've memorized nearly 30 days. It's not just about verses—it's wired me for grit, focus, and discipline, the same energy I pour into every line of code and mentoring session.",
                "I've had some dope gigs. I mentored 50+ coders at DBS Foundation's Coding Camp, leveling up their Python and people skills. At GAOTek Inc., I guided 100+ interns to crush it. Oh, and I've shipped 30+ projects—AI models, web apps, you name it—using TensorFlow, PyTorch, and more.",
                "My roots? I studied at Shree Sachchidanand gurukul, sihor, then snagged a Bachelor of Engineering from Kalol Institute of Technology at gandhinagar, geeking out on Machine Learning breakthroughs.",
                "What's next? I'm all in on using AI to tackle big challenges fast, growing Copilot ID, and dropping value in open-source communities. Plus, I'm playing the long game with investments to fuel innovation that lasts.",
                "Got a wild idea or just wanna vibe on tech? Hit me up—let's build something epic together! 🚀"
            ],
            "location": {
                "regency": "Sihor",
                "residency": "Bhavnagar",
                "province": "Gujarat",
                "prov": "Gujarat",
                "country": "India",
                "flag": "🇮🇳"
            },
            "social_media": {
                "github": "https://github.com/hardix02",
                "linkedin": "https://li.hardik-baraiya.com",
                "follow_linkedin": "https://linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=hardik-baraiya-b9a4ba327",
                "x": "https://x.com/hardiix02",
                "instagram": "https://www.instagram.com/hardix02",
                "email": "hardikbaraiy50@gmail.com"
            },
            "donate": [
                {
                    "github_sponsor": "https://github.com/sponsors/hardix02",
                    "donate_text": "Back me on GitHub Sponsors"
                },
            ],
            "skills": [
                "Python",
                "Django",
                "TensorFlow",
                "PyTorch",
                # "Flask"
            ],
        }
