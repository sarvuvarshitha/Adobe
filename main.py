import os
import json
from extract_outline import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(INPUT_DIR, file)
            title, outline = extract_outline(file_path)
            output_data = {
                "title": title,
                "outline": outline
            }
            output_file = os.path.splitext(file)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_file)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2)

    print("✅ Finished processing all PDFs.")

if __name__ == "__main__":
    main()
