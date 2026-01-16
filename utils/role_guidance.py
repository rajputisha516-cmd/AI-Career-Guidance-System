def get_role_specific_guidance(role, level):
    guidance = {
        "ML Engineer": {
            "Beginner": (
                "Start with Python fundamentals, basic Machine Learning algorithms, "
                "and core Statistics. Avoid jumping directly into Deep Learning."
            ),
            "Intermediate": (
                "Work on ML projects, understand model evaluation, and improve "
                "Statistics. Start exploring Deep Learning basics."
            ),
            "Ready": (
                "You are ready for ML Engineer roles. Focus on internships, "
                "real-world datasets, and model deployment basics."
            )
        },

        "Data Analyst": {
            "Beginner": (
                "Focus on SQL, Excel, and basic Statistics. Learn how to analyze "
                "datasets before moving to advanced tools."
            ),
            "Intermediate": (
                "Build dashboards, work on data analysis projects, and strengthen "
                "Python for data analysis."
            ),
            "Ready": (
                "You are ready for Data Analyst roles. Start applying and improve "
                "storytelling with data."
            )
        },

        "Backend Developer": {
            "Beginner": (
                "Strengthen Python basics, understand databases, and learn how "
                "backend systems work."
            ),
            "Intermediate": (
                "Work on backend projects, APIs, and improve database design skills."
            ),
            "Ready": (
                "You are ready for Backend Developer roles. Focus on system design "
                "and real-world backend applications."
            )
        },

        "Business Analyst": {
            "Beginner": (
                "Focus on Excel, basic Statistics, and understanding business problems."
            ),
            "Intermediate": (
                "Work on case studies, dashboards, and business-focused analysis."
            ),
            "Ready": (
                "You are ready for Business Analyst roles. Improve communication and "
                "stakeholder interaction skills."
            )
        },

        "AI Engineer": {
            "Beginner": (
                "Focus on Python basics, Machine Learning foundations, and basic Deep Learning concepts."
            ),
            "Intermediate": (
                "Work on Deep Learning and NLP projects. Improve model training and evaluation skills."
            ),
            "Ready": (
                "You are ready for AI Engineer roles. Focus on advanced DL, NLP, and real-world AI systems."
            )
        },

        "Data Scientist": {
            "Beginner": (
                "Focus on Python, Statistics, and data analysis fundamentals."
            ),
            "Intermediate": (
                "Work on end-to-end data science projects and improve ML skills."
            ),
            "Ready": (
                "You are ready for Data Scientist roles. Focus on real-world problem solving and research."
            )
        }

    }

    return guidance.get(role, {}).get(
        level,
        "Keep improving your skills and gaining practical experience."
    )
