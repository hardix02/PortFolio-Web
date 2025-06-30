from django.conf import settings

class ExperiencesData:
    '''
    employment type:
    - Full-time (Pekerjaan penuh waktu)
    - Part-time (Pekerjaan paruh waktu)
    - Self-employed (Pekerjaan mandiri)
    - Freelance (Pekerjaan lepas)
    - Contract (Pekerjaan berdasarkan kontrak)
    - Internship (Magang)
    - Apprenticeship (Pelatihan kerja atau magang kejuruan)
    - Seasonal (Pekerjaan musiman)
    
    location type:
    - On-site: Bekerja langsung di lokasi fisik (contoh: kantor).
    - Hybrid: Kombinasi antara bekerja dari lokasi fisik dan jarak jauh.
    - Remote: Sepenuhnya bekerja jarak jauh (contoh: dari rumah).
    '''
    
    employment_types = {
        "ft": "Full-time",
        "pt": "Part-time",
        "se": "Self-employed",
        "fr": "Freelance",
        "co": "Contract",
        "in": "Internship",
        "ap": "Apprenticeship",
        "sn": "Seasonal"
    }
    
    location_types = {
        "on": "On-site",
        "hy": "Hybrid",
        "rm": "Remote"
    }
    
    experiences = [
        {
            "id": 13,
            "title": "FullStack & MQL Developer",
            "company": "CodeSoftix InfoTech",
            "logo": f"{settings.BASE_URL}/static/img/logo/codsoftixlogo.jpg",
            "website": "https://codesoftix.com/",
            "period": "Jan 2024 - Present",
            "employment_type": employment_types["ft"],
            "location_type": location_types["on"],
            "location": "Bhavnagar, India 🇮🇳",
            "is_current": True,
            "responsibilities": [
                "Designed and developed full-stack web applications using .NET technologies with clean, maintainable codebases.",
                "Created and maintained MetaQuotes Language (MQL) scripts and Expert Advisors for trading automation in MT4/MT5.",
                "Built RESTful APIs and backend services in .NET, integrating with frontend frameworks for seamless user experiences.",
                "Optimized database queries, performed debugging, and implemented security enhancements across multiple projects.",
                "Collaborated closely with clients and team members to gather requirements and deliver high-quality software solutions on time."
            ]
        },
        {
            "id": 12,
            "title": "Software Developer",
            "company": "Sparrow Softtech",
            "logo": f"{settings.BASE_URL}/static/img/logo/sprlogo.webp",
            "website": "https://sparrowsofttech.com",
            "period": "Sep 2023 - Dec 2023",
            "employment_type": employment_types["ft"],
            "location_type": location_types["on"],
            "location": "Bhavnagar, India 🇮🇳",
            "is_current": False,
            "responsibilities": [
                "Developed and maintained .NET web applications and services with focus on scalability and performance.",
                "Built UI components and data-driven features using ASP.NET MVC and Web API frameworks.",
                "Worked with SQL Server databases for data modeling, query optimization, and reporting tasks.",
                "Participated in code reviews, testing, and deployment of production-ready applications."
            ]
        },
        {
            "id": 11,
            "title": "Software Internship",
            "company": "Sparrow Softtech - Software Department",
            "logo": f"{settings.BASE_URL}/static/img/logo/sprlogo.webp",
            "website": "https://sparrowsofttech.com",
            "period": "Jun 2023 - Sep 2023",
            "employment_type": employment_types["in"],
            "location_type": location_types["on"],
            "location": "Bhavnagar, India 🇮🇳",
            "is_current": False,
            "responsibilities": [
                "Built beefy neural nets with TensorFlow and Keras—deep learning FTW!",
                "Tackled NLP for text classification and sentiment analysis—words got no secrets.",
                "Cranked out deep learning models for time series and image classification—smooth.",
                "Explored recommendation systems and reinforcement learning—next-level stuff.",
                "Got cozy with generative AI and model deployment—ready for the real world!"
            ]
        },
        {
            "id": 10,
            "title": "Web Developer",
            "company": "Sparrow Softtech",
            "logo": f"{settings.BASE_URL}/static/img/logo/sprlogo.webp",
            "website": "https://sparrowsofttech.com",
            "period": "May 2023 - Jun 2023",
            "employment_type": employment_types["ft"],
            "location_type": location_types["on"],
            "location": "Bhavnagar, India 🇮🇳",
            "is_current": False,
            "responsibilities": [
                "Assisted in developing and testing .NET modules and components under senior developer guidance.",
                "Worked on bug fixes, UI improvements, and small feature implementations for internal applications.",
                "Learned about .NET frameworks, coding standards, and source control using Git.",
                "Participated in regular team meetings and sprint reviews to understand software development processes."
            ]
        },
        {
            "id": 9,
            "title": "Web Internship",
            "company": "Sparrow Softtech | Web Department",
            "logo": f"{settings.BASE_URL}/static/img/logo/sprlogo.webp",
            "website": "https://sparrowsofttech.com",
            "period": "Jan 2023 - May 2023",
            "employment_type": employment_types["in"],
            "location_type": location_types["on"],
            "location": "Bhavnagar, India 🇮🇳",
            "is_current": False,
            "responsibilities": [
                "Created interactive data visualizations and dashboards using Google Sheets and web-based tools.",
                "Learned core web technologies, including HTML, CSS, and JavaScript fundamentals.",
                "Practiced building JavaScript applications with basic supervised and unsupervised logic structures."
            ]
        },
        # {
        #     "id": 8,
        #     "title": "Founder",
        #     "company": "Copilot ID",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/copilot_id.webp",
        #     "website": "https://github.com/copilot-id",
        #     "period": "Jan 2023 - Present",
        #     "employment_type": employment_types["ft"],
        #     "location_type": location_types["hy"],
        #     "location": "Yogyakarta, Indonesia 🇮🇩",
        #     "is_current": True,
        #     "responsibilities": [
        #         "Living that AI life, building with Django, TensorFlow, PyTorch, and more—full-stack geek mode!"
        #     ]
        # },
        # {
        #     "id": 7,
        #     "title": "Chief Secretary",
        #     "company": "IKA-PPIM 2021",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/ikappim_21.webp",
        #     "website": "https://www.instagram.com/ikappim_21/",
        #     "period": "Sep 2021 - Present",
        #     "employment_type": employment_types["pt"],
        #     "location_type": location_types["rm"],
        #     "location": "Surakarta, Indonesia 🇮🇩",
        #     "is_current": True,
        #     "responsibilities": [
        #         "Wrangled data for 200+ alumni with slick filtering and dope graphs.",
        #         "Whipped up org docs and meeting notes—keeping it tight.",
        #         "Designed clean, user-friendly interfaces for alumni management—UX vibes!"
        #     ]
        # },
        # {
        #     "id": 6,
        #     "title": "Assistant Squad Leader of Web Developer Intern",
        #     "company": "GAOTek Inc.",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/gaotek_inc.webp",
        #     "website": "https://gaotek.com",
        #     "period": "Apr 2024 - May 2024",
        #     "employment_type": employment_types["in"],
        #     "location_type": location_types["rm"],
        #     "location": "New York, USA 🇺🇸",
        #     "is_current": False,
        #     "responsibilities": [
        #         "Led 100+ interns, keeping everyone on track like a pro.",
        #         "Ran daily huddles and kept the team vibe strong.",
        #         "Helped interns crush tech and project hurdles—teamwork makes the dream work!"
        #     ]
        # },
        # {
        #     "id": 5,
        #     "title": "Main Team of Web Developer Intern",
        #     "company": "GAOTek Inc.",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/gaotek_inc.webp",
        #     "website": "https://gaotek.com",
        #     "period": "Apr 2024 - May 2024",
        #     "employment_type": employment_types["in"],
        #     "location_type": location_types["rm"],
        #     "location": "New York, USA 🇺🇸",
        #     "is_current": False,
        #     "responsibilities": [
        #         "Jammed with the crew weekly to plan projects and swap ideas.",
        #         "Leveled up on Google Search Console, Analytics, and Tag Manager with 3 solid tasks.",
        #         "Dropped reports every weekday for a month—kept it consistent!"
        #     ]
        # },
        # {
        #     "id": 4,
        #     "title": "Web Developer Intern",
        #     "company": "GAOTek Inc.",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/gaotek_inc.webp",
        #     "website": "https://gaotek.com",
        #     "period": "Feb 2024 - Mar 2024",
        #     "employment_type": employment_types["in"],
        #     "location_type": location_types["rm"],
        #     "location": "New York, USA 🇺🇸",
        #     "is_current": False,
        #     "responsibilities": [
        #         "Joined late-night team huddles (11:30 PM EST) to debug and plan—grind mode!",
        #         "Went ham on WooCommerce—added 30+ products, built a contact form, and 30+ product pages.",
        #         "Smashed 7+ tasks faster than most interns in just 2 months.",
        #         "Churned out daily reports for 2 months—never missed a beat!"
        #     ]
        # },
        # {
        #     "id": 3,
        #     "title": "Machine Learning Intern",
        #     "company": "YoungDev",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/youngdev.webp",
        #     "website": "https://youngdevinterns.net",
        #     "period": "Apr 2024 - May 2024",
        #     "employment_type": employment_types["in"],
        #     "location_type": location_types["rm"],
        #     "location": "Islamabad, Pakistan 🇵🇰",
        #     "is_current": False,
        #     "responsibilities": [
        #         "Built predictive models with Python and Scikit-Learn—data’s my playground.",
        #         "Cooked up classification and regression models that hit the mark!"
        #     ]
        # },
        # {
        #     "id": 2,
        #     "title": "Machine Learning Intern",
        #     "company": "iNeuron.ai",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/ineuron.webp",
        #     "website": "https://ineuron.ai",
        #     "period": "Jan 2024 - Jan 2024",
        #     "employment_type": employment_types["in"],
        #     "location_type": location_types["rm"],
        #     "location": "Karnataka, India 🇮🇳",
        #     "is_current": False,
        #     "responsibilities": [
        #         "Tackled a phishing domain detection project—cybersecurity meets ML!",
        #         "Used ML to beef up online defenses—pretty dope mission."
        #     ]
        # },
        # {
        #     "id": 1,
        #     "title": "Deputy of Da'wah",
        #     "company": "Imaarotu Syu'unith Tholabah",
        #     "logo": f"{settings.BASE_URL}/static/img/logo/ist.webp",
        #     "website": "https://istngruki.org",
        #     "period": "Sep 2019 - Sep 2020",
        #     "employment_type": employment_types["ft"],
        #     "location_type": location_types["on"],
        #     "location": "Surakarta, Indonesia 🇮🇩",
        #     "is_current": False,
        #     "responsibilities": [
        #         "Rallied 50 boarding school students to teach in local villages—community vibes!",
        #         "Teamed up to run epic competitions for 500+ students—energy was unreal.",
        #         "Kept the boarding school’s discipline game tight and inspiring."
        #     ]
        # }
    ]
