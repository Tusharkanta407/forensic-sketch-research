# Paper Name: Analyzing and Improving the Image Quality of StyleGAN (StyleGAN2)

## Authors
* Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen, Timo Aila

## Year
* 2020

## Problem
* StyleGAN suffered from characteristic artifacts, such as water-droplet-like blobs and perspective misalignment.

## Architecture
* **StyleGAN2:** Discards AdaIN normalization in favor of weight demodulation. Replaces progressive growing with skip connections in the generator and residual connections in the discriminator. Uses path length regularization.

## Loss Function
* Non-saturating logistic loss with R1 regularization.

## Input & Output
* **Input:** $512$-dimensional random latent vector $z \in \mathcal{Z}$.
* **Output:** Photorealistic synthesized face image ($1024 \times 1024$).

## Advantages
* Unmatched visual quality of synthesized human faces.
* Clean, customizable latent space ($W$-space) suitable for attribute manipulation.

## Limitations
* High computational resource requirements for training.
* Susceptible to mode collapse if trained on small datasets.

## How can we use it?
* In **Module 3 (Generator)**, we utilize StyleGAN2's generator network to project parsed facial attributes into latent $w$-vectors and synthesize the high-fidelity suspect face.

## Implementation Status
* **In Progress** (Evaluating stylegan2-ada pre-trained weights for custom conditioning).

## Notes
* StyleGAN2 is the current gold standard for high-fidelity facial generation in our research context.\n