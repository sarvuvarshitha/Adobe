from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
import json
import os


from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextLine
import json

def extract_outline(pdf_path):
    outline = []
    title = None
    for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
        lines = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for line in element:
                    if isinstance(line, LTTextLine):
                        text = line.get_text().strip()
                        if not text: continue
                        size = line.height
                        # simplified heuristic: large size → heading
                        lines.append((text, size))
        if page_num == 1 and lines:
            title = max(lines, key=lambda t: t[1])[0]
        for text, size in lines:
            if size > 15:
                lvl = "H1"
            elif size > 13:
                lvl = "H2"
            elif size > 11:
                lvl = "H3"
            else:
                continue
            outline.append({"level": lvl, "text": text, "page": page_num})
    return title or "", outline
