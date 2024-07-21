import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Example Usage
textbook_text1 = extract_text_from_pdf("harry-potter-and-the-deathly-hallows-j.k.-rowling.pdf")
textbook_text2 = extract_text_from_pdf("harry-potter-and-the-goblet-of-fire.pdf")
textbook_text3 = extract_text_from_pdf("harry-potter-and-the-half-blood-prince-j.k.-rowling.pdf")
