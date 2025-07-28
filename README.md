# Adobe India Hackathon 2025 - Connecting the Dots

## 🧠 Project Title: PDF Intelligence Engine

### Round 1A: PDF Outline Extractor

---

### 🔍 Overview

This project extracts a structured outline from PDF documents. Given a PDF with up to 50 pages, it outputs a JSON with the document title and headings (H1, H2, H3) along with their page numbers and levels. The tool runs fully offline inside a Docker container and is optimized for AMD64 architecture.

---

### 🔎 Problem Statement

> Extract a clean hierarchical structure (Title, H1, H2, H3) from a PDF for intelligent document analysis.

---

### ✅ Features

* Supports PDFs up to 50 pages
* Extracts Title, H1, H2, H3 with page numbers
* Outputs valid JSON structure
* Runs fully offline
* Fast execution (under 10s)
* AMD64-compatible Docker container

---

### 🔹 Output Format

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

### 🔬 Tech Stack

* Python 3.10
* PyMuPDF (fitz) for PDF parsing
* heuristics for heading classification (size, font, style)
* Docker (Linux/AMD64)

---

### 📊 Accuracy Techniques

* Font size & font style heuristics
* Visual positioning
* Bolding/Capitalization detection
* Avoids hardcoding by generalizing heading detection logic

---

### 📅 Sample Folder Structure

```
connecting-the-dots/
├── Dockerfile # Docker image configuration
├── requirements.txt # Python dependencies
├── sample_input/ # Sample test PDFs (for local use only)
│ └── sample.pdf
├── output/ # Will be populated with JSON output files
├── src/ # All source code goes here
│ ├── extract_outline.py # Core logic for heading extraction
│ ├── main.py # Entry point for Docker container execution
│ ├── rank_sections.py # (Used in Round 1B for ranking logic)
│ └── utils.py # Utility functionsconnecting-the-dots/
├── input/
│   └── sample.pdf
├── output/
│   └── sample.json
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

### ⚡ How to Run

#### 1. Build Docker Image:

```bash
docker build --platform linux/amd64 -t pdf-outline-app .
```

#### 2. Run Docker Container:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outline-app
```

---

### 📊 Performance

| Metric          | Value                                               |
| --------------- | --------------------------------------------------- |
| Execution Time  | < 10 seconds                                        |
| Offline Support | ✅ Yes                                               |
| Model Used      | None                                                |
| Language        | English (Optional multilingual support coming soon) |
| Compatibility   | CPU only, AMD64, No internet                        |

---

### 🔺 Constraints Met

* [x] Executes under 10s
* [x] < 200MB container
* [x] Works fully offline
* [x] Docker compatible for AMD64
* [x] No hardcoding / No API calls

---

### 🧪 Future Scope for Round 1B

* Persona-specific summarization
* Job-to-be-done relevance ranking
* Cross-document section linking

---

### 📄 Files Included

* `main.py`: PDF outline extractor logic
* `requirements.txt`: PyMuPDF
* `Dockerfile`: For building the image
* `README.md`: This file
* `approach_explanation.md`: For Round 1B (separately prepared)

---

### 🔗 Git Instructions

1. Create a private GitHub repo
2. Push all files
3. Submit the link (keep private until deadline)

---

### 🚀 Credits

Built by Sarvu Varshitha for Adobe India Hackathon 2025.

---

### 📊 Round 1B Preparation Status

* [ ] persona\_handler.py
* [ ] section\_ranker.py
* [ ] json\_builder.py
* [ ] docker-compose.yml
* [x] `approach_explanation.md` *(in-progress)*
* [ ] `challenge1b_output.json`

---

Let’s rethink reading. Let’s connect the dots. ✨
# Adobe
