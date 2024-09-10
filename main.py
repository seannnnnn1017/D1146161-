from ultralytics import YOLO
import cv2
import os 

model = YOLO('models/yolov9s.pt')
results = model('inputs/test.jpg')


img = cv2.imread('inputs/test.jpg')


annotated_img = results[0].plot()


if not os.path.exists('outputs'):
    os.makedirs('outputs')
cv2.imwrite('outputs/result.jpg', annotated_img)

