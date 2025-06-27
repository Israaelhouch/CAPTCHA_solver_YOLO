# CAPTCHA Solver (Digit Only) 🔐

This project builds an object detection model to detect and recognize digits in CAPTCHA images. The goal is to automatically segment and classify each digit to enable further processing or CAPTCHA solving.

---

## Project Overview

- **Dataset creation:** Collected a custom dataset of CAPTCHA images.
- **Manual annotation:** Labeled every digit in the images with bounding boxes using a labeling tool in YOLO format.
- **Data organization:** Split the dataset into training, validation, and test sets.
- **Model training:** Trained a YOLO-based model on the annotated dataset.
- **Evaluation:** Assessed model performance on held-out data.
- **Inference:** Used the trained model to detect digits in new CAPTCHA images.

---

## Dataset

The dataset was manually labeled using Roboflow. Labels are in YOLO format, with 10 classes representing digits 0-9.

