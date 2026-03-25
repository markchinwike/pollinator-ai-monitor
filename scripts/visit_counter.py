import os
import pandas as pd

# Path to your final labels
label_dir = "runs/detect/final_data/labels"
gap_threshold = 30  # Max frames between detections to count as the same visit

video_stats = []

# Get unique video names
all_files = sorted([f for f in os.listdir(label_dir) if f.endswith(".txt")])
video_groups = {}

for f in all_files:
    prefix = "_".join(f.split("_")[:-1]) # Gets IMG_XXXX
    frame = int(f.split("_")[-1].replace(".txt", ""))
    if prefix not in video_groups: video_groups[prefix] = []
    video_groups[prefix].append(frame)

for vid, frames in video_groups.items():
    frames.sort()
    visits = 0
    if frames:
        visits = 1
        for i in range(1, len(frames)):
            if frames[i] - frames[i-1] > gap_threshold:
                visits += 1
    
    video_stats.append({"Video": vid, "Unique_Visits": visits, "Total_Frames": len(frames)})

df = pd.DataFrame(video_stats)
df.to_csv("results/visit_analysis.csv", index=False)
print("--- VISIT ANALYSIS COMPLETE ---")
print(df)