import pdfplumber
import docx


def read_resume(path: str) -> str:
    """
    Reads resume text from PDF or DOCX file.
    """

    if path.lower().endswith(".pdf"):
        text = ""

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        return text.strip()

    elif path.lower().endswith(".docx"):
        doc = docx.Document(path)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text.strip()

    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")