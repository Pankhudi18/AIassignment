import json
import os
from utils import is_question, classify_images_by_area

INPUT_JSON = "output_data/extracted_content.json"
OUTPUT_JSON = "final_output/final_questions.json"

def generate_question_json(json_input_path, final_output_path):
    with open(json_input_path, 'r') as f:
        pages = json.load(f)

    final_data = []

    for page in pages:
        text = page.get('text', '')
        image_paths = page.get('images', [])

        if not is_question(text):
            continue  

        question_img, options = classify_images_by_area(image_paths)

        final_data.append({
            "question": text,
            "images": question_img,
            "option_images": options
        })

    os.makedirs(os.path.dirname(final_output_path), exist_ok=True)
    with open(final_output_path, 'w') as f:
        json.dump(final_data, f, indent=2)

    print(f"[✓] Final structured question JSON saved to: {final_output_path}")


if __name__ == "__main__":
    generate_question_json(INPUT_JSON, OUTPUT_JSON)
