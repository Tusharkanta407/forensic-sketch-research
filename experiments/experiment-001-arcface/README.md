# Experiment 001: ArcFace Identity Verification on CUHK Sketches

## Objective
Evaluate how well pretrained ArcFace embeddings preserve identity when comparing a photorealistic face to a hand-drawn sketch from the CUHK dataset.

## Files
* `run_eval.py` - Evaluation script.
* `config.json` - Experiment configurations.

## Results
* **Average Cosine Similarity (Photo vs. Photo):** 0.92
* **Average Cosine Similarity (Photo vs. Sketch):** 0.72
* **Conclusion:** Sketch rendering introduces domain shifts, causing a drop in cosine similarity.

## Observations
* Sketches with exaggerated features (e.g., larger chin, thinner eyes) result in lower scores.
* Adding a style-invariant face recognizer might be needed.

## Next Steps
* Test FaceNet to see if L2 embeddings perform better under domain shift.\n