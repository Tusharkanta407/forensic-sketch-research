# Research Roadmap

Our research path is divided into five milestones:

## Milestone 1: Literature and Data Setup
* Review StyleGAN2, ArcFace, and Transformer architectures.
* Download and clean CelebA and FFHQ datasets.

## Milestone 2: Natural Language parser
* Train/fine-tune small transformer or LLM classifier to parse descriptions into JSON attribute maps.
* Build mapping layer to convert JSON classes into latent code ranges.

## Milestone 3: Attribute-Conditioned Generation
* Research mapping networks that direct text latents into StyleGAN $w$-space.
* Validate generated visual quality using FID.

## Milestone 4: Forensic Sketch Rendering
* Implement pencil sketch shaders using OpenCV.
* Train/evaluate CycleGAN or Pix2Pix for neural style transfer.

## Milestone 5: Identity Evaluation & Verification
* Setup ArcFace model pipeline.
* Evaluate cosine similarity between generated sketch, generated photo, and ground truth photo.\n