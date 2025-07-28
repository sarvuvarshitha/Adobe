from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

def rank_sections(doc_texts, persona_text, job_text, outline_list):
    all_texts = doc_texts + [persona_text + " " + job_text]
    tfidf = TfidfVectorizer(stop_words='english').fit(all_texts)
    doc_vecs = tfidf.transform(doc_texts)
    persona_job_vec = tfidf.transform([persona_text + " " + job_text])
    sims = cosine_similarity(doc_vecs, persona_job_vec).flatten()
    ranked = sorted(zip(outline_list, sims), key=lambda x: -x[1])
    output = []
    for idx, (item, score) in enumerate(ranked, start=1):
        entry = {
            "document": item.get("doc_name", ""),
            "page": item["page"],
            "section_title": item["text"],
            "importance_rank": idx
        }
        output.append(entry)
    return output
