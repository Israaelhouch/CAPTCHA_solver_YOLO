import os, sys
from src.solver import solve_captcha

model_path = "/Users/macmini/Desktop/CAPATCHA_solver/model/weights/best.pt"
directory = "/Users/macmini/Desktop/CAPATCHA_solver/data/test/images"
path = "/Users/macmini/Desktop/CAPATCHA_solver/data/test/images"

dir = os.listdir( path )

correct_labels=[]
predicted_labels=[]

for file in dir:
   correct_labels.append(os.path.splitext(file)[0])
   predicted_labels.append(solve_captcha(path+"/"+file,model_path))
   
   


correct_count = 0

for i in range(len(correct_labels)):
    if correct_labels[i] == predicted_labels[i]: 
        correct_count += 1
    else:
        print(i)
        
accuracy = correct_count / len(correct_labels) 
print("Accuracy:", accuracy)