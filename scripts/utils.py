import cv2
import pytesseract

def is_question(text: str) -> bool:
    return "?" in text.strip().lower()

def classify_images_by_area(image_paths):
    img_info = []

    for img_path in image_paths:
        try:
            img = cv2.imread(img_path)
            if img is None:
                continue
            height, width, _ = img.shape
            area = height * width
            img_info.append((img_path, area))
        except Exception as e:
            print(f"Error reading {img_path}: {e}")

    img_info.sort(key=lambda x: x[1], reverse=True)

    if not img_info:
        return None, []

    question_image = img_info[0][0]
    option_images = [img[0] for img in img_info[1:]]

    return question_image, option_images
