import cv2
from ultralytics import YOLO
import os
from datetime import datetime

# 1. Load your model
model = YOLO("runs/detect/train11/weights/best.pt")

# 2. Path to your videos folder
video_folder = "tests/field_videos/"
output_base = "runs/detect/"

# Get list of all video files
video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(('.mov', '.mp4', '.avi'))]

print(f"--- Found {len(video_files)} videos to analyze ---")

for video_name in video_files:
    video_path = os.path.join(video_folder, video_name)
    print(f"\n>> ANALYZING: {video_name}")
    
    # Run detection
    # save_txt=True creates a text file for every frame a bee is found
    results = model.predict(source=video_path, save=True, conf=0.10, stream=True)
    
    pollinator_detections = 0
    for r in results:
        pollinator_detections += len(r.boxes)
    
    print("-" * 30)
    print(f"RESULT for {video_name}: {pollinator_detections} detections found.")
    print("-" * 30)

print("\n" + "="*40)
print(f"FINISHED! All videos processed at {datetime.now().strftime('%H:%M:%S')}")
print("="*40)
