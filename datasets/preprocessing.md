# Preprocessing Pipelines

Scripts for face alignment, cropping, and landmark detection:

```python
# Placeholder for alignment preprocessing script
# To be executed on CelebA / FFHQ
def align_face(image_path, landmarks):
    """
    Aligns facial features based on eye coordinates.
    """
    pass
```

## Steps
1. **Facial Landmark Detection:** Detect eye, nose, and mouth coordinates using MTCNN or Dlib.
2. **Affine Transformation:** Rotate and scale images to align eye centers.
3. **Cropping & Resizing:** Crop to bounding box size and resize to target resolution ($112 \times 112$ for ArcFace, $1024 \times 1024$ for StyleGAN2).\n