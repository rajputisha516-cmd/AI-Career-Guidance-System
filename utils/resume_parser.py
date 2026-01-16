import PyPDF2
import re

# -------------------------------
# Extract raw text from PDF
# -------------------------------
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()


# -------------------------------
# Extract skills with LOW weight
# -------------------------------
def extract_skills_from_resume(text):
    """
    Resume skills are given LOW weight (0.5)
    because resumes often exaggerate skill levels.
    """

    skills = {
        "python": 0,
        "sql": 0,
        "statistics": 0,
        "ml": 0,
        "dl": 0,
        "nlp": 0,
        "excel": 0,
        "communication": 0
    }

    # ---- Technical skills ----
    if re.search(r"\bpython\b", text):
        skills["python"] = 0.5

    if re.search(r"\bsql\b", text):
        skills["sql"] = 0.5

    if re.search(r"\bstatistics\b|\bprobability\b", text):
        skills["statistics"] = 0.5

    if re.search(r"\bmachine learning\b|\bml\b", text):
        skills["ml"] = 0.5

    if re.search(r"\bdeep learning\b|\bdl\b", text):
        skills["dl"] = 0.5

    if re.search(r"\bnlp\b|\bnatural language processing\b", text):
        skills["nlp"] = 0.5

    # ---- New skills added ----
    if re.search(r"\bexcel\b|\bms excel\b|\bmicrosoft excel\b", text):
        skills["excel"] = 0.5

    if re.search(r"\bcommunication\b|\bverbal\b|\bwritten\b|\bpresentation\b", text):
        skills["communication"] = 0.5

    return skills
