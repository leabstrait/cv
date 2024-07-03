from datetime import datetime

data = {
    "last_updated": datetime.now().strftime("%d-%m-%Y"),
    "personal_information": {
        "name": "Labin Ojha",
        "profile": "Software Developer",
        "phone": "+44 7463 751853",
        "email": "kontaktlabin@gmail.com",
        "github": "https://github.com/leabstrait",
        "location": "London, United Kingdom",
    },
    "work_experience": [
        {
            "company": "Pi Tech Info Pvt. Ltd.",
            "description": "Fintech startup that provides trading analytics for the Nepalese Stock market",
            "location": "Kathmandu, Nepal",
            "positions": [
                {
                    "title": "Software Developer",
                    "start_date": "Dec 2021",
                    "end_date": "Sept 2022",
                },
            ],
            "responsibilities": [
                "Full-Stack Developer and acting team lead for their product called 'Chukul' which offers fundamental analysis and technical analysis of stocks as a service.",
                "Worked with Django, Vue.js, Quasar UI, TradingView",
                "Launched the product in a short timeframe and helped the company break even after about 4 months of launch.",
            ],
        },
        {
            "company": "Beta Analytics Pvt. Ltd.",
            "description": "Fintech Startup that provides a range of tools and services for stock traders and brokers in the Nepalese Stock Market",
            "location": "Kathmandu, Nepal",
            "positions": [
                {
                    "title": "Software Developer",
                    "start_date": "Feb 2020",
                    "end_date": "Sept 2021",
                }
            ],
            "responsibilities": [
                "Full-Stack Developer on their in-house data entry and reporting system.",
                "Full-Stack Developer on a web application framework for stockbrokers. The framework allowed for multiple revenue streams for the company while having to maintain a single codebase. It had features like: Integration with Stock Market Data and Stats API, Managing downloadable content, Creating and updating notices and blog posts, User Registration System that integrated with the Nepal Stock Exchange Trading Management System.",
                "Developed a browser extension to automate filling up forms.",
            ],
        },
        {
            "company": "Sudreeshya IT Training Academy",
            "description": "An IT training institute that provide software development and other IT courses.",
            "location": "Kathmandu, Nepal",
            "positions": [
                {
                    "title": "Python Instructor",
                    "start_date": "Jan 2020",
                    "end_date": "Feb 2020",
                }
            ],
            "responsibilities": [
                "Delivered a course in Python programming to 3rd-year college students.",
                "Each student was assigned an end-of-course project and they demonstrated considerable understanding of the concepts. Many of them are employed now in good companies.",
            ],
        },
        {
            "company": "Innovative Engineering and Construction Technologies Pvt. Ltd.",
            "description": "A civil engineering firm providing survey, design and construction services",
            "location": "Kathmandu, Nepal",
            "positions": [
                {
                    "title": "Information Systems Officer",
                    "start_date": "Feb 2018",
                    "end_date": "Dec 2019",
                }
            ],
            "responsibilities": [
                "Managed and oversaw the development of their website - Meroghar Website and mobile app",
                "Maintained and Monitored the organisation’s ERP software(Bitrix24)",
                "Setup, Operation and Troubleshooting of computing and network equipment like Routers and Switches, CCTV, Access Control and Attendance Systems, IVR",
                "Tested and evaluated new tools and technologies. Proposed hardware/software solutions to accomplish the company's business objectives",
                "Negotiated pricing and fees with various software providers and equipment vendors to cut down the operation costs of the organization.",
                "Documented & Reported findings and observations for Business Process Optimization.",
            ],
        },
        {
            "company": "Bajra Technologies Pvt. Ltd.",
            "description": "A tech consulting firm designing and building solutions for a vast array of clients, national and international",
            "location": "Kathmandu, Nepal",
            "positions": [
                {
                    "title": "Software Development Intern",
                    "start_date": "Sept 2017",
                    "end_date": "Dec 2017",
                }
            ],
            "responsibilities": [
                "Built a backend module in Golang for one of their in-house project named 'Sitehawk' which is a website monitoring service",
                "The module utilized Bing Search API to determine rankings of our client's websites which was quite useful and appreciated.",
            ],
        },
    ],
    "tech_skills": {
        "programming": ["Python", "Javascript", "LaTeX"],
        "web_frameworks": ["Flask", "Django"],
        "js_frameworks": ["Vue.js", "TradingView"],
        "databases": ["PostgreSQL"],
        "systems": ["Linux", "Docker"],
        "dev_tools": ["git", "tmux", "Makefile"],
    },
    "education": [
        {
            "institution": "Tribhuvan University",
            "location": "Kathmandu, Nepal",
            "degree": "BSc. Computer Science and Information Technology",
            "start_date": "2014",
            "end_date": "2018",
            "details": [""],
        },
    ],
    "references": [
        # {
        #     "name": "Bimod Dev Panta",
        #     "company": "Pitech Info Pvt. Ltd.",
        #     "description": "Pitech Info Pvt. Ltd.",
        #     "location": "Kathmandu, Nepal",
        #     "phone": "+977 9849895805",
        #     "email": ["bdevpanta@gmail.com", "connect@pitechinfo.com"],
        # },
        # {
        #     "name": "Rohit Man Amatya",
        #     "company": "Beta Analytics Pvt. Ltd.",
        #     "description": "Beta Analytics Pvt. Ltd.",
        #     "location": "Lalitpur, Nepal",
        #     "phone": "+977 9843063261",
        #     "email": ["rho.rhoit@gmail.com"],
        # },
        # {
        #     "name": "Dipesh Deuja",
        #     "company": "LogicVent Technology Pvt. Ltd.",
        #     "description": "LogicVent Technology Pvt. Ltd.",
        #     "location": "Bhaktapur, Nepal",
        #     "phone": "+977 9860896508",
        #     "email": ["deujadipesh1407@gmail.com", "contact@logicvent.com"],
        # },
        # {
        #     "name": "Bonaventure Fereira",
        #     "company": "Roland House Apartments",
        #     "description": "Roland House Apartments",
        #     "location": "South Kensington, London",
        #     "phone": "+44 (0)20 7341 6800",
        #     "email": ["office@rolandhouseapartments.co.uk"],
        # },
    ],
}
