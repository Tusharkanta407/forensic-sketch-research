# Literature Review: Text-to-Sketch and Facial Identification

This document compiles the academic landscape surrounding our research:

## 1. Text-to-Image and Text-to-Face Synthesis
* **GAN-based Models:** Models like AttnGAN and ControlGAN use attention mechanisms to refine specific regions of an image based on words.
* **Latent space manipulation:** Using StyleGAN's mapping network to map text descriptors to latent variables ($w$).
* **Diffusion Models:** Latent Diffusion Models (LDMs) show superior high-fidelity synthesis and are highly controllable via cross-attention.

## 2. Face Recognition and Metric Learning
* **FaceNet (2015):** Utilizes triplet loss to map faces to a 128-dimensional space where L2 distance matches face similarity.
* **ArcFace (2019):** Adds an additive angular margin to the target logit to maximize inter-class variance and minimize intra-class variance.

## 3. Sketch Rendering and Neural Style Transfer
* **NST:** Using VGG-19 features to separate content (photograph) from style (pencil sketch).
* **Pix2Pix / CycleGAN:** Image-to-image translation models trained on Photo-Sketch datasets (like CUHK).\n