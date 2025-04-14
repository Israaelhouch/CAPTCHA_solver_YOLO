def sort_detections(boxes):
    items = zip(boxes.xyxy, boxes.cls)
    return sorted(items, key=lambda x: x[0][0])
