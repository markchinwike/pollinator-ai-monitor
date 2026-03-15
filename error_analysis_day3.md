

# Day 3 Error Analysis: Taxonomic Disambiguation

## Model Performance Summary
- **Base Model (train10):** 0.985 mAP (Single class: Bee)
- **Fine-Tuned Model (train11):** 0.615 mAP (Two classes: Bee, Hoverfly)
## Observations & Error Patterns
1. **Mimicry Confusion:** The model frequently confuses *Eristalis tenax* (Drone Fly) with *Apis mellifera* (Honeybee). This is expected due to biological mimicry.
2. **Confidence Drop:** Adding the second class forced the model to be more "skeptical," leading to lower confidence scores but higher taxonomic accuracy.
3. **Small Object Detection:** Detections are less stable when insects are far away; accuracy improves significantly with the "Zoom" shots in the video data.

## Ecological Impact
The current model (train11) allows for the calculation of the **Shannon Diversity Index (H)**. While mAP is lower, the biological validity of the data is higher because we are no longer over-counting bees by misidentifying flies.