from ultralytics import YOLO
import cv2

def sort_detections(boxes):
    """
    Sort bounding boxes from left to right based on x-coordinate.
    """
    items = zip(boxes.xyxy, boxes.cls)
    return sorted(items, key=lambda x: x[0][0])  # x[0][0] is x_min of bbox

def solve_captcha(image_path, model_path):
    """
    Solve a digit CAPTCHA image using a trained YOLO model.

    Args:
        image_path (str): Path to the CAPTCHA image.
        model_path (str): Path to the trained YOLO model (.pt file).

    Returns:
        str: The decoded CAPTCHA digits as a string.
    """
    model = YOLO(model_path)
    img = cv2.imread(image_path)

    results = model(img)[0]
    boxes = results.boxes
    digits = sort_detections(boxes)

    captcha = ''.join(str(int(cls.item())) for _, cls in digits)
    return captcha
