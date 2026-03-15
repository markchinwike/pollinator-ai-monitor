import torch
import cv2
import ultralytics

print("--- SYSTEM CHECK ---")
print(f"PyTorch Version: {torch.__version__}")
print(f"OpenCV Version: {cv2.__version__}")
print(f"YOLOv8 Version: {ultralytics.__version__}")
print("--------------------")
print("Status: ENGINE ONLINE")