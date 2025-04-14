from ultralytics import YOLO
import cv2
from .utils import sort_detections

def solve_captcha(image_path, model_path):
    model = YOLO(model_path)
    img = cv2.imread(image_path)
    results = model(img)[0]

    boxes = results.boxes
    digits = sort_detections(boxes)

    captcha = ''.join(str(int(cls.item())) for _, cls in digits)
    return captcha
