from newspaper import Article
import fitz  # PyMuPDF

def extract_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def extract_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

