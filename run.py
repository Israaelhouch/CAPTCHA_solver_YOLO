from src.solver import solve_captcha

if __name__ == "__main__":
    img_path = "/Users/macmini/Desktop/CAPATCHA_solver/data/test/images/captcha_945_png.rf.c5697ca3bb57cebf5835d71154f1dfe8.jpg"
    model_path = "/Users/macmini/Desktop/CAPATCHA_solver/model/weights/best.pt"
    
    result = solve_captcha(img_path, model_path)
    print("CAPTCHA result:", result)
