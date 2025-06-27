import os
from src.solver import solve_captcha

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)  # get path of current file

    img_path = os.path.join(base_path, "data", "test", "images", "37735.jpg")
    model_path = os.path.join(base_path, "model", "weights", "best.pt")

    result = solve_captcha(img_path, model_path)
    print("CAPTCHA result:", result)
