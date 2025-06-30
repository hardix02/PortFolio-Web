from django.conf import settings

class EducationData:
    education = [
        {
            "degree": "Information Technology",
            "alias": "Bachelor of Engineering",
            "date": {
                "start": {
                    "year": 2024,
                    "month": "Sep"
                },
                "end": {
                    "year": "",
                    "month": "Present"
                }
            },
            "institution": "Kalol Institute of Technology & Research Center",
            "website": "https://kirc.ac.in/",
            "logo": f"{settings.BASE_URL}/static/img/logo/kirc.webp",
            "is_last": True,
            "location": {
                "regency": "Ahmedabad",
                "province": "Gujarat",
                "prov": "Gujarat",
                "country": "India",
                "flag": "🇮🇳",
                "map_url": "https://maps.google.com/maps?width=683&amp;height=630&amp;hl=en&amp;q=kalol institute of &amp;t=&amp;z=18&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"

            },
            "achievements": [
            "Completed projects using .NET Core, ASP.NET MVC, and SQL Server, gaining strong backend development experience.",
            "Built and deployed multiple full-stack web applications in coursework, practicing modern coding standards.",
            "Participated in coding hackathons and tech fests, securing top-3 finishes in inter-college competitions.",
            "Mastered data structures, algorithms, and software design patterns through academic projects and team collaborations.",
            "Explored cloud deployment techniques and modern DevOps tools for CI/CD workflows."
            ]
        },
        {
            "degree": "Diploma Engineering (Information Technology)",
            "years": "2019 - 2021",
            "institution": "Sir BPTI Bhavnagar",
            "website": "https://sites.google.com/view/itdeptsirbpti",
            "logo": f"{settings.BASE_URL}/static/img/logo/bpti.webp",
            "is_last": False,
            "location": {
                "regency": "Bhavnagar",
                "province": "Gujarat",
                "prov": "Gujarat",
                "country": "India",
                "flag": "🇮🇳",
                "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d839.8902086006083!2d110.81010211911801!3d-7.583671478356138!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e7a161053e2e49b%3A0xa3c304c347094dd4!2sPondok%20Pesantren%20Al%20Mukmin!5e1!3m2!1sen!2sid!4v1746378601521!5m2!1sen!2sid"
            },
            "achievements": [
            "Developed CRUD web applications with .NET Framework, strengthening understanding of MVC architecture.",
            "Learned core database design principles, building normalized schemas in SQL Server.",
            "Created mini-projects in Windows Forms and ASP.NET, focusing on user-friendly UI and clean code.",
            "Participated in seminars and workshops on .NET technologies and secure coding practices."
            ]

        },
        {
            "degree": "Higher School",
            "years": "2017 - 2019",
            "institution": "Sihor, Bhavnagar",
            "logo": f"{settings.BASE_URL}/static/img/logo/sdit_al_mannan.webp",
            "is_last": False,
            "location": {
                "regency": "Sihor",
                "province": "Bhavnagar",
                "prov": "Gujarat",
                "country": "India",
                "flag": "🇮🇳",
                "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d839.8741719724507!2d110.63054034044244!3d-7.540896804194124!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e7a6bf96222c533%3A0x1eac3559e081d4e2!2sSDIT%20Al%20Mannan%20Mojosongo!5e1!3m2!1sen!2sid!4v1746378437547!5m2!1sen!2sid"
            },
            "achievements": [
            "Completed Gujarat Board curriculum with consistent exam performance.",
            "Participated in school-level academic activities.",
            "Focused on core subjects including mathematics, science, and languages."
        ]
        },
        {
            "degree": "Primary School",
            "years": "2009 - 2016",
            "institution": "Ramnagar, Gundala",
            "logo": f"{settings.BASE_URL}/static/img/logo/tkit_al_mannan_ori.webp",
            "is_last": False,
            "location": {
                "regency": "Sihor",
                "province": "Bhavnagar",
                "prov": "Gujarat",
                "country": "India",
                "flag": "🇮🇳",
                "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1009.2575066395403!2d110.63296114927637!3d-7.544367428472007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e7a6b777ddce74d%3A0x5963db2cb6db1f07!2sTKIT%20AL-MANNAN!5e1!3m2!1sen!2sid!4v1746378514204!5m2!1sen!2sid"
            },
            "achievements": [
            "Attended classes regularly and completed primary education under Gujarat Board.",
            "Participated in basic co-curricular activities and class events.",
            "Built fundamental reading, writing, and arithmetic skills."
        ]
        }
    ]
