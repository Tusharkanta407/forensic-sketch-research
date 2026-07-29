# Paper Name: FaceNet: A Unified Embedding for Face Recognition and Clustering

## Authors
* Florian Schroff, Dmitry Kalenichenko, James Philbin

## Year
* 2015

## Problem
* Learning a direct mapping from face images to a compact Euclidean space where distances directly correspond to a measure of face similarity.

## Architecture
* Deep convolutional network (ZFNet/Inception) followed by $L_2$ normalization to project features onto a 128-dimensional hypersphere.

## Loss Function
* **Triplet Loss:**
  $$\mathcal{L} = \sum_i^N \left[ \|f(x_i^a) - f(x_i^p)\|_2^2 - \|f(x_i^a) - f(x_i^n)\|_2^2 + \alpha \right]_+$$
  Minimizes distance between Anchor ($a$) and Positive ($p$), while maximizing distance between Anchor and Negative ($n$).

## Input & Output
* **Input:** Cropped and aligned face images.
* **Output:** 128-dimensional embedding vector.

## Advantages
* Learns embedding directly rather than optimizing a classification layer.
* High accuracy with low-dimensional features.

## Limitations
* Selecting semi-hard triplets is computationally expensive and slow to converge.

## How can we use it?
* Used alongside ArcFace to provide a secondary metric for identity verification of generated sketches.

## Implementation Status
* **Completed** (Model loader integrated in `prototypes/arcface/`).

## Notes
* Introduced the triplet mining technique which is crucial for custom metric learning.\n