# 📚 Literature Review & Paper Summaries

Every paper reviewed by the team must be summarized using the template below to maintain structured academic records.

## 📝 Documented Papers

* 📄 **Attention Is All You Need** — Transformer architecture, self-attention mechanisms.
  * [Paper Summary](./attention-is-all-you-need.md) | [Download PDF](./attention-is-all-you-need.pdf)
* 📄 **ArcFace** — Angular margin face recognition, identity evaluation.
  * [Paper Summary](./arcface.md) | [Download PDF](./arcface.pdf)
* 📄 **FaceNet** — Triplet loss embeddings, face verification.
  * [Paper Summary](./facenet.md) | [Download PDF](./facenet.pdf)
* 📄 **StyleGAN2** — Demodulated weights, high-quality face generation.
  * [Paper Summary](./stylegan2.md) | [Download PDF](./stylegan2.pdf)
* 📄 **StyleGAN (StyleGAN1)** — Style-based generator architecture.
  * [Download PDF](./stylegan.pdf)
* 📄 **Pix2Pix** — Image-to-image translation with conditional adversarial networks.
  * [Download PDF](./pix2pix.pdf)

---

## 📋 Paper Summary Template

Create a new file under `papers/<paper-name>.md` with the following template:

```markdown
# Paper Name: [Insert Title]

## Authors
* [Author 1, Author 2, ...]

## Year
* [YYYY]

## Problem Statement
* What problem is this paper trying to solve?

## Architecture
* Explain the model structure and core components.

## Loss Function
* Detail the loss functions used (with formulas if applicable).

## Input & Output
* **Input:** [Format, shape, description]
* **Output:** [Format, shape, description]

## Advantages
* Why is this approach good?

## Limitations
* What are the trade-offs or weaknesses?

## How can we use it?
* How does this apply to the Forensic Sketch Generator project?

## Implementation Status
* [Not Started | In Progress | Completed]

## Notes
* Any additional ideas, references, or experimental results.
```\n