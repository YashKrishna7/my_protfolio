# from django.shortcuts import render

# def index(request):
#     context = {
#         'name': 'Yash Krishna K P',
#         'location': 'Malappuram, Kerala, India',
#         'email': 'yashvalsaraj@gmail.com',
#         'phone': '+91 7594948245',
#         'linkedin': 'https://www.linkedin.com/in/yash-krishna-081bb6255?utm_source=share_via&utm_content=profile&utm_medium=member_android',
#         'github': 'https://github.com/YashKrishna7',
#         'summary': [
#             'Information Technology student with skills in Python, Django, Flutter, HTML, Tailwind CSS, and MySQL.',
#             'Knowledge of Data Structures & Algorithms (DSA) and basic Machine Learning concepts.',
#             'Experience building web and mobile applications and developing backend systems using Django.',
#             'Familiar with RESTful API integration, data preprocessing, and Python-based ML libraries.',
#             'Interested in software development, web development, and mobile app development.',
#         ],
#         'education': [
#             {
#                 'degree': 'BTech in Information Technology',
#                 'institution': 'Institute of Engineering and Technology, University of Calicut',
#                 'location': 'Thenhipalam, Kerala',
#                 'year': '2022 – 2026',
#             },
#             {
#                 'degree': 'Higher Secondary',
#                 'institution': 'MVHSS Ariyallur',
#                 'location': 'Kerala',
#                 'year': '2022',
#             },
#         ],
#         'experience': [
#             {
#                 'role': 'Intern',
#                 'company': 'Bridgeon',
#                 'period': 'December 2024',
#                 'location': 'Kozhikode',
#                 'points': [
#                     'Developed a responsive e-commerce web application using Django and Tailwind CSS.',
#                     'Integrated APIs to connect front-end and back-end services; reduced load time by 20%.',
#                     'Built an E-Commerce platform with user and admin modules including product, order, and user management.',
#                     'Built a weather web application using a public weather API for real-time global weather data.',
#                 ],
#             }
#         ],
#         'projects': [
#             {
#                 'name': 'FEAST',
#                 'subtitle': 'Smart Hostel Mess Management Web Application',
#                 'period': 'January 2025 – May 2025',
#                 'description': 'A hostel mess management system for expense tracking with a responsive UI and automated daily/monthly expense calculations.',
#                 'tech': ['Python', 'Django', 'HTML', 'Tailwind CSS'],
#                 'icon': '🍽️',
#                 'color': '#e86c3a',
#             },
#             {
#                 'name': 'PREVIDICT',
#                 'subtitle': 'AI-Based YouTube Shorts Performance Prediction System',
#                 'period': 'June 2025 – March 2026',
#                 'description': 'An AI-powered web and mobile application that predicts expected view counts for YouTube Shorts and provides content optimization suggestions. Includes video frame and audio analysis.',
#                 'tech': ['Python', 'Dart', 'Django', 'Flutter', 'MySQL'],
#                 'icon': '📊',
#                 'color': '#4a9eff',
#             },
#         ],
#         'skills': {
#             'Programming Languages': ['Python', 'HTML5', 'CSS3', 'SQL', 'C', 'Java (Basic)', 'JavaScript (Basic)'],
#             'Frontend': ['Tailwind CSS', 'Responsive Design'],
#             'Backend': ['Django', 'RESTful APIs', 'JWT Authentication'],
#             'Database': ['MySQL', 'SQLite'],
#             'Security & Architecture': ['MVT Pattern', 'Auth & Authorization'],
#             'Tools & Platforms': ['Git', 'GitHub', 'VS Code', 'PyCharm'],
#             'Concepts': ['DSA (Basic)', 'CRUD Operations', 'API Integration', 'Component Reusability'],
#         },
#     }
#     return render(request, 'portfolio/index.html', context)


# from django.shortcuts import render

# def index(request):
#     context = {
#         'name': 'Yash Krishna K P',
#         'location': 'Malappuram, Kerala, India',
#         'email': 'yashvalsaraj@gmail.com',
#         'phone': '+91 7594948245',
#         'linkedin': 'https://linkedin.com',
#         'github': 'https://github.com',
#         'summary': [
#             'Information Technology student with skills in Python, Django, Flutter, HTML, Tailwind CSS, and MySQL.',
#             'Knowledge of Data Structures & Algorithms (DSA) and basic Machine Learning concepts.',
#             'Experience building web and mobile applications and developing backend systems using Django.',
#             'Familiar with RESTful API integration, data preprocessing, and Python-based ML libraries.',
#             'Interested in software development, web development, and mobile app development.',
#         ],
#         'education': [
#             {
#                 'degree': 'BTech in Information Technology',
#                 'institution': 'Institute of Engineering and Technology, University of Calicut',
#                 'location': 'Thenhipalam, Kerala',
#                 'year': '2022 – 2026',
#             },
#             {
#                 'degree': 'Higher Secondary',
#                 'institution': 'MVHSS Ariyallur',
#                 'location': 'Malappuram,Kerala',
#                 'year': '2022',
#             },
#             {
#                 'degree': 'High School',
#                 'institution': 'MVHSS Ariyallur',
#                 'location': 'Malappuram,Kerala',
#                 'year': '2022',
#             },
#         ],
#         'experience': [
#             {
#                 'role': 'Intern',
#                 'company': 'Bridgeon',
#                 'period': 'December 2024',
#                 'location': 'Kozhikode',
#                 'points': [
#                     'Developed a responsive e-commerce web application using Django and Tailwind CSS.',
#                     'Integrated APIs to connect front-end and back-end services; reduced load time by 20%.',
#                     'Built an E-Commerce platform with user and admin modules including product, order, and user management.',
#                     'Built a weather web application using a public weather API for real-time global weather data.',
#                 ],
#             }
#         ],
#         'projects': [
#             {
#                 'name': 'FEAST',
#                 'subtitle': 'Smart Hostel Mess Management Web Application',
#                 'period': 'January 2025 – May 2025',
#                 'description': 'A hostel mess management system for expense tracking with a responsive UI and automated daily/monthly expense calculations.',
#                 'tech': ['Python', 'Django', 'HTML', 'Tailwind CSS'],
#                 'icon': '🍽️',
#                 'color': '#e86c3a',
#                 'tag': 'Academic',
#             },
#             {
#                 'name': 'PREVIDICT',
#                 'subtitle': 'AI-Based YouTube Shorts Performance Prediction System',
#                 'period': 'June 2025 – March 2026',
#                 'description': 'An AI-powered web and mobile application that predicts expected view counts for YouTube Shorts and provides content optimization suggestions. Includes video frame and audio analysis.',
#                 'tech': ['Python', 'Dart', 'Django', 'Flutter', 'MySQL'],
#                 'icon': '📊',
#                 'color': '#4a9eff',
#                 'tag': 'Academic',
#             },
#             {
#                 'name': 'ShopEase',
#                 'subtitle': 'Full-Stack E-Commerce Web Application',
#                 'period': 'December 2024',
#                 'description': 'A responsive e-commerce platform built during internship at Bridgeon with full user and admin modules. Features product management, order tracking, and user management. Integrated APIs to connect front-end and back-end, improving load time by 20%.',
#                 'tech': ['Python', 'Django', 'Tailwind CSS', 'RESTful APIs'],
#                 'icon': '🛒',
#                 'color': '#34d399',
#                 'tag': 'Internship',
#             },
#             {
#                 'name': 'WeatherNow',
#                 'subtitle': 'Real-Time Global Weather Web App',
#                 'period': 'December 2024',
#                 'description': 'A weather web application built during internship at Bridgeon that fetches and displays real-time weather data for any location worldwide using a public weather API.',
#                 'tech': ['Python', 'Django', 'Weather API', 'HTML', 'CSS'],
#                 'icon': '🌤️',
#                 'color': '#a78bfa',
#                 'tag': 'Internship',
#             },
#         ],
#         'skills': {
#             'Programming Languages': ['Python', 'HTML5', 'CSS3', 'SQL', 'C', 'Java (Basic)', 'JavaScript (Basic)'],
#             'Frontend': ['Tailwind CSS', 'Responsive Design'],
#             'Backend': ['Django', 'RESTful APIs', 'JWT Authentication'],
#             'Database': ['MySQL', 'SQLite'],
#             'Security & Architecture': ['MVT Pattern', 'Auth & Authorization'],
#             'Tools & Platforms': ['Git', 'GitHub', 'VS Code', 'PyCharm'],
#             'Concepts': ['DSA (Basic)', 'CRUD Operations', 'API Integration', 'Component Reusability'],
#         },
#     }
#     return render(request, 'portfolio/index.html', context)

# from django.shortcuts import render

# def index(request):
#     context = {
#         'name': 'Yash Krishna K P',
#         'location': 'Malappuram, Kerala, India',
#         'email': 'yashvalsaraj@gmail.com',
#         'phone': '+91 7594948245',
#         'linkedin': 'https://www.linkedin.com/in/yash-krishna-081bb6255?utm_source=share_via&utm_content=profile&utm_medium=member_android',
#         'github': 'https://github.com/YashKrishna7',
#         'summary': [
#             'Information Technology student with skills in Python, Django, Flutter, HTML, Tailwind CSS, and MySQL.',
#             'Knowledge of Data Structures & Algorithms (DSA) and basic Machine Learning concepts.',
#             'Experience building web and mobile applications and developing backend systems using Django.',
#             'Familiar with RESTful API integration, data preprocessing, and Python-based ML libraries.',
#             'Interested in software development, web development, mobile app development, and UI/UX design.',
#         ],
#         'education': [
#             {
#                 'degree': 'BTech in Information Technology',
#                 'institution': 'Institute of Engineering and Technology, University of Calicut',
#                 'location': 'Thenhipalam, Kerala',
#                 'year': '2022 - 2026',
#             },
#             {
#                 'degree': 'Higher Secondary',
#                 'institution': 'MVHSS Ariyallur',
#                 'location': 'Malappuram, Kerala',
#                 'year': '2022',
#             },
#             {
#                 'degree': 'High School',
#                 'institution': 'MVHSS Ariyallur',
#                 'location': 'Malappuram, Kerala',
#                 'year': '2020',
#             },
#         ],
#         'experience': [
#             {
#                 'role': 'Intern',
#                 'company': 'Bridgeon',
#                 'period': 'December 2024',
#                 'location': 'Kozhikode',
#                 'points': [
#                     'Developed a responsive e-commerce web application using Django and Tailwind CSS.',
#                     'Integrated APIs to connect front-end and back-end services; reduced load time by 20%.',
#                     'Built an E-Commerce platform with user and admin modules including product, order, and user management.',
#                     'Built a weather web application using a public weather API for real-time global weather data.',
#                 ],
#             }
#         ],
#         'projects': [
#             {
#                 'name': 'FEAST',
#                 'subtitle': 'Smart Hostel Mess Management Web Application',
#                 'period': 'January 2025 - May 2025',
#                 'description': 'A hostel mess management system for expense tracking with a responsive UI and automated daily/monthly expense calculations.',
#                 'tech': ['Python', 'Django', 'HTML', 'Tailwind CSS'],
#                 'icon': '\U0001f37d\ufe0f',
#                 'color': '#e86c3a',
#                 'tag': 'Academic',
#             },
#             {
#                 'name': 'PREVIDICT',
#                 'subtitle': 'AI-Based YouTube Shorts Performance Prediction System',
#                 'period': 'June 2025 - March 2026',
#                 'description': 'An AI-powered web and mobile application that predicts expected view counts for YouTube Shorts and provides content optimization suggestions. Includes video frame and audio analysis.',
#                 'tech': ['Python', 'Dart', 'Django', 'Flutter', 'MySQL'],
#                 'icon': '\U0001f4ca',
#                 'color': '#4a9eff',
#                 'tag': 'Academic',
#             },
#             {
#                 'name': 'ShopEase',
#                 'subtitle': 'Full-Stack E-Commerce Web Application',
#                 'period': 'December 2024',
#                 'description': 'A responsive e-commerce platform built during internship at Bridgeon with full user and admin modules. Features product management, order tracking, and user management. Integrated APIs connecting front-end and back-end, improving load time by 20%.',
#                 'tech': ['Python', 'Django', 'Tailwind CSS', 'RESTful APIs'],
#                 'icon': '\U0001f6d2',
#                 'color': '#34d399',
#                 'tag': 'Internship',
#             },
#             {
#                 'name': 'WeatherNow',
#                 'subtitle': 'Real-Time Global Weather Web App',
#                 'period': 'December 2024',
#                 'description': 'A weather web application built during internship at Bridgeon that fetches and displays real-time weather data for any location worldwide using a public weather API.',
#                 'tech': ['Python', 'Django', 'Weather API', 'HTML', 'CSS'],
#                 'icon': '\U0001f324\ufe0f',
#                 'color': '#a78bfa',
#                 'tag': 'Internship',
#             },
#         ],
#         'skills': {
#             'Programming Languages': ['Python', 'HTML5', 'CSS3', 'SQL', 'C', 'Java (Basic)', 'JavaScript (Basic)'],
#             'Frontend': ['Tailwind CSS', 'Responsive Design'],
#             'Backend': ['Django', 'RESTful APIs', 'JWT Authentication'],
#             'Database': ['MySQL', 'SQLite'],
#             'Security & Architecture': ['MVT Pattern', 'Auth & Authorization'],
#             'Tools & Platforms': ['Git', 'GitHub', 'VS Code', 'PyCharm'],
#             'Design & UI/UX': ['Figma (Basic)', 'Canva', 'UI/UX Design', 'Poster Design'],
#             'Concepts': ['DSA (Basic)', 'CRUD Operations', 'API Integration', 'Component Reusability'],
#         },
#         'posters': [
#             {
#                 'title': 'SILVER JUBILEE',
#                 'description': 'Brief description of what this poster is about.',
#                 'image': 'portfolio_project/static/poster/sponsorship inside.jpeg',
#                 'tool': 'Canva',
#                 'color': '#f472b6',
#             },
#             {
#                 'title': 'SILVER JUBILEE INSIDE',
#                 'description': 'Brief description of what this poster is about.',
#                 'image': 'portfolio_project/static/posters/Sponsorship outside.jpeg',
#                 'tool': 'Canva',
#                 'color': '#fb923c',
#             },
#             {
#                 'title': 'WOMEN EMPOWERMENT ',
#                 'description': 'Brief description of what this poster is about.',
#                 'image': 'portfolio_project/static/posters/women empowerment.jpeg',
#                 'tool': 'Canva',
#                 'color': '#a78bfa',
#             },
#         ],
#     }
#     return render(request, 'portfolio/index.html', context)


from django.shortcuts import render

def index(request):
    context = {
        'name': 'Yash Krishna K P',
        'location': 'Malappuram, Kerala, India',
        'email': 'yashvalsaraj@gmail.com',
        'phone': '+91 7594948245',
        'linkedin': 'https://www.linkedin.com/in/yash-krishna-081bb6255?utm_source=share_via&utm_content=profile&utm_medium=member_android',
        'github': 'https://github.com/YashKrishna7',
        'summary': [
            'Information Technology student with skills in Python, Django, Flutter, HTML, Tailwind CSS, and MySQL.',
            'Knowledge of Data Structures & Algorithms (DSA) and basic Machine Learning concepts.',
            'Experience building web and mobile applications and developing backend systems using Django.',
            'Familiar with RESTful API integration, data preprocessing, and Python-based ML libraries.',
            'Interested in software development, web development, mobile app development, and UI/UX design.',
        ],
        'education': [
            {
                'degree': 'BTech in Information Technology',
                'institution': 'Institute of Engineering and Technology, University of Calicut',
                'location': 'Thenhipalam, Kerala',
                'year': '2022 - 2026',
            },
            {
                'degree': 'Higher Secondary',
                'institution': 'MVHSS Ariyallur',
                'location': 'Malappuram, Kerala',
                'year': '2022',
            },
            {
                'degree': 'High School',
                'institution': 'MVHSS Ariyallur',
                'location': 'Malappuram, Kerala',
                'year': '2020',
            },
        ],
        'experience': [
            {
                'role': 'Intern',
                'company': 'Bridgeon',
                'period': 'December 2024',
                'location': 'Kozhikode',
                'points': [
                    'Developed a responsive e-commerce web application using Django and Tailwind CSS.',
                    'Integrated APIs to connect front-end and back-end services; reduced load time by 20%.',
                    'Built an E-Commerce platform with user and admin modules including product, order, and user management.',
                    'Built a weather web application using a public weather API for real-time global weather data.',
                ],
            }
        ],
        'projects': [
            {
                'name': 'FEAST',
                'subtitle': 'Smart Hostel Mess Management Web Application',
                'period': 'January 2025 - May 2025',
                'description': 'A hostel mess management system for expense tracking with a responsive UI and automated daily/monthly expense calculations.',
                'tech': ['Python', 'Django', 'HTML', 'Tailwind CSS'],
                'icon': '\U0001f37d\ufe0f',
                'color': '#e86c3a',
                'tag': 'Academic',
            },
            {
                'name': 'PREVIDICT',
                'subtitle': 'AI-Based YouTube Shorts Performance Prediction System',
                'period': 'June 2025 - March 2026',
                'description': 'An AI-powered web and mobile application that predicts expected view counts for YouTube Shorts and provides content optimization suggestions. Includes video frame and audio analysis.',
                'tech': ['Python', 'Dart', 'Django', 'Flutter', 'MySQL'],
                'icon': '\U0001f4ca',
                'color': '#4a9eff',
                'tag': 'Academic',
            },
            {
                'name': 'ShopEase',
                'subtitle': 'Full-Stack E-Commerce Web Application',
                'period': 'December 2024',
                'description': 'A responsive e-commerce platform built during internship at Bridgeon with full user and admin modules. Features product management, order tracking, and user management. Integrated APIs connecting front-end and back-end, improving load time by 20%.',
                'tech': ['Python', 'Django', 'Tailwind CSS', 'RESTful APIs'],
                'icon': '\U0001f6d2',
                'color': '#34d399',
                'tag': 'Internship',
            },
            {
                'name': 'WeatherNow',
                'subtitle': 'Real-Time Global Weather Web App',
                'period': 'December 2024',
                'description': 'A weather web application built during internship at Bridgeon that fetches and displays real-time weather data for any location worldwide using a public weather API.',
                'tech': ['Python', 'Django', 'Weather API', 'HTML', 'CSS'],
                'icon': '\U0001f324\ufe0f',
                'color': '#a78bfa',
                'tag': 'Internship',
            },
        ],
        'skills': {
            'Programming Languages': ['Python', 'HTML5', 'CSS3', 'SQL', 'C', 'Java (Basic)', 'JavaScript (Basic)'],
            'Frontend': ['Tailwind CSS', 'Responsive Design'],
            'Backend': ['Django', 'RESTful APIs', 'JWT Authentication'],
            'Database': ['MySQL', 'SQLite'],
            'Security & Architecture': ['MVT Pattern', 'Auth & Authorization'],
            'Tools & Platforms': ['Git', 'GitHub', 'VS Code', 'PyCharm'],
            'Design & UI/UX': ['Figma (Basic)', 'Canva', 'UI/UX Design', 'Poster Design'],
            'Concepts': ['DSA (Basic)', 'CRUD Operations', 'API Integration', 'Component Reusability'],
        },
        'posters': [
             {
                'title': 'SILVER JUBILEE OUTSIDEE',
                'description': 'Silver Jubilee sponsorship Brochure for IETCU (OUTSIDE LOOK).',
                'image': 'poster/Sponsorship outside.jpeg',
                'tool': 'Canva',
                'color': '#fb923c',
            },

            {
                'title': 'SILVER JUBILEE INSIDE',
                'description': 'Silver Jubilee sponsorship Brochure for IETCU (INSIDE LOOK).',
                'image': 'poster/sponsorship inside.jpeg',
                'tool': 'Canva',
                'color': '#f472b6',
            },
           
            {
                'title': 'WOMEN EMPOWERMENT',
                'description': '“Secured 1st Prize in the Poster Making Competition conducted by the Innovation and Entrepreneurship Development Centre (IEDC) in connection with the Silver Jubilee celebrations of the Institute of Engineering and Technology, University of Calicut.Theme: Women in Engineering – Empowering the Future.',
                'image': 'poster/women empowerment.jpeg',
                'tool': 'Canva',
                'color': '#a78bfa',
            },
        ],
    }
    return render(request, 'portfolio/index.html', context)