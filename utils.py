import fitz  # PyMuPDF

def extract_text_by_section(pdf_path, outline):
    doc = fitz.open(pdf_path)
    section_texts = []

    for item in outline:
        page_num = item["page"] - 1  # zero-based index
        section_title = item["text"]
        if page_num < len(doc):
            page = doc[page_num]
            text = page.get_text()
            section_texts.append({
                "doc_name": pdf_path.split("/")[-1],
                "page": page_num + 1,
                "text": text,
                "section_title": section_title
            })

    return section_texts
