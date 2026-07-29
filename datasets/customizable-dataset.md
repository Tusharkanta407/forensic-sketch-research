# Customizable Dataset Integration

This document outlines how the team can integrate custom face-sketch paired datasets or custom descriptive datasets for model fine-tuning and evaluation.

## 👥 Custom Dataset Structure

To use a custom dataset for training the generative model (Module 3) or evaluation (Module 5), organize the files as follows:

```
custom-dataset/
├── metadata.json
├── photos/
│   ├── 00001.png
│   ├── 00002.png
│   └── ...
└── sketches/
    ├── 00001.png
    ├── 00002.png
    └── ...
```

### 📄 Metadata File Format (`metadata.json`)
The metadata file maps each image pair to structured facial attributes, which are used to train the Natural Language Understanding parser (Module 1) and condition the generator (Module 3).

```json
[
  {
    "id": "00001",
    "photo_path": "photos/00001.png",
    "sketch_path": "sketches/00001.png",
    "description": "A middle-aged male with an oval face, thick eyebrows, brown eyes, and a small scar on the left cheek.",
    "attributes": {
      "gender": "male",
      "age": 45,
      "face_shape": "oval",
      "eye_color": "brown",
      "eyebrows": "thick",
      "scar": "left_cheek"
    }
  }
]
```

## 🛠️ Data Preparation and Augmentation
1. **Alignment:** Ensure all photos and sketches are aligned using facial landmarks (e.g. eye centers positioned at the same horizontal line).
2. **Resolution:** Resize to standard sizes:
   * Generator: $1024 \times 1024$ (StyleGAN2) or $512 \times 512$.
   * Evaluation: $112 \times 112$ (ArcFace ResNet input).
3. **Data Augmentation:** Since forensic sketch datasets are typically small (e.g., CUHK has only 606 pairs), apply:
   * Horizontal flipping (re-mapping left/right attributes like "scar on left cheek" to "scar on right cheek").
   * Subtle affine rotations.
   * Contrast adjustments (especially on sketch styles).

## 📝 User Notes
*Use this section to document custom dataset loading problems, annotation guidelines, or custom data sources as they are developed.*
