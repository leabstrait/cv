import os
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa

import cv
import cover_letter

def generate_html(template_name, data):
    # Set up Jinja environment
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))

    # Load Jinja2 template
    template = env.get_template(template_name)

    # Render HTML using data
    html_output = template.render(data)

    return html_output


def generate_pdf(html_content, pdf_path):
    # Generate PDF
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

    if pisa_status.err:
        print("PDF generation failed:", pisa_status.err)
        return False
    else:
        print(f"PDF generated and saved at {pdf_path}")
        return True


# Example usage
if __name__ == "__main__":
    # CV data
    cv_data = cv.data  # Your CV data dictionary
    # Cover letter data
    cover_letter_data = cover_letter.data  # Your cover letter data dictionary

    # Generate CV HTML
    cv_html = generate_html("cv.j2", cv_data)

    # Save CV HTML
    cv_html_path = "index.html"
    with open(cv_html_path, "w") as cv_html_file:
        cv_html_file.write(cv_html)
    print(f"CV HTML saved as: {cv_html_path}")

    # Generate and save CV PDF
    cv_pdf_path = "labin-ojha-cv.pdf"
    generate_pdf(cv_html, cv_pdf_path)

    # Generate cover letter HTML
    cover_letter_html = generate_html("cover-letter.j2", cover_letter_data)

    # Save cover letter HTML
    cover_letter_html_path = "cover-letter.html"
    with open(cover_letter_html_path, "w") as cover_letter_html_file:
        cover_letter_html_file.write(cover_letter_html)
    print(f"Cover letter HTML saved as: {cover_letter_html_path}")

    # Generate and save cover letter PDF
    cover_letter_pdf_path = "labin-ojha-cover-letter.pdf"
    generate_pdf(cover_letter_html, cover_letter_pdf_path)
