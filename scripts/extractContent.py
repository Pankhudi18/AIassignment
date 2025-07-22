import fitz  # PyMuPDF
import os
import json
from PIL import Image

def extract_pdf_content(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    content = []

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text = page.get_text()
        images = []

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page{page_number+1}_image{img_index+1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            images.append(image_path)

        content.append({
            "page": page_number + 1,
            "text": text.strip(),
            "images": images
        })

    with open(os.path.join(output_dir, "extracted_content.json"), "w") as json_file:
        json.dump(content, json_file, indent=2)

    print("Extraction complete!")


extract_pdf_content("class1.pdf", "output_data")
