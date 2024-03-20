# Define sender information
sender_name = "Labin Ojha"
sender_email = "kontaktlabin@gmail.com"
sender_phone = "+44 07463 751853"
sender_address = "London, United Kingdom"

# Define recipient information
recipient_name = "" or None
recipient_position = "The HR Manager"
recipient_company = "ABC Tech Nepal"
recipient_company_address = "Lalitpur, Nepal"

# Advertised Position
job_position = "Software Engineer (Python)"

# Define date
date = "March 12, 2024"  # You can use a function to auto-generate today's date

# Construct the subject
subject = f"Application for '{job_position}' role at {recipient_company}"

# Construct the opening
opening = f"""
    Respected Sir/Madam,

    With reference to the subject as cited above, I {sender_name}, would like to apply for a '{job_position}' role at {recipient_company}. I found the said reference through a job portal site and information provided on the company's official website.
"""

# Construct the body introduction
body_intro = f"""
    I am writing to express my interest in the '{job_position}' position at {recipient_company}. With my skills and experience in Python programming, Flask framework, and SQL databases, I am confident in my ability to contribute effectively to your team.
"""

# Define body experience
body_experience = """
    I am a graduate with a BSc. in Computer Science from Tribhuvan University and have previously worked as a full-stack software developer with Beta Analytics Pvt. Ltd. on their in-house project.
"""

# Define body proposal
body_proposal = f"""
    I am confident I can learn any new technology on the job. I also have a deep interest in emerging technologies and the businesses that they enable. I believe I can provide value to your company and also fuel my personal growth as a developer in this role available at your company.
"""

# Define body conclusion
body_conclusion = f"""
    I would very much like to discuss the aforementioned opportunity at your company. To schedule an interview, please call me at {sender_phone}. Thank you for taking the time to review my resume. I look forward to talking with you.
"""

# Define closing
closing = "Your Sincerely,"

# Define the data dictionary
data = {
    "sender_name": sender_name,
    "sender_email": sender_email,
    "sender_phone": sender_phone,
    "sender_address": sender_address,
    "recipient_name": recipient_name,
    "recipient_position": recipient_position,
    "recipient_company": recipient_company,
    "recipient_company_address": recipient_company_address,
    "job_position": "job_position",
    "date": date,
    "subject": subject,
    "opening": opening,
    "body_intro": body_intro,
    "body_experience": body_experience,
    "body_proposal": body_proposal,
    "body_conclusion": body_conclusion,
    "closing": closing,
}
