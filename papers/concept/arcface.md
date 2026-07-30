# Paper Name: ArcFace: Additive Angular Margin Loss for Deep Face Recognition

## Authors
* Jiankang Deng, Jia Guo, Niannan Xue, Stefanos Zafeiriou

## Year
* 2019

## Problem
* Face recognition models need highly discriminative features. Traditional Softmax loss only focuses on separating different classes but does not maximize the margin between classes in feature space.

## Architecture
* Deep Convolutional Neural Network (e.g., ResNet-50 or ResNet-100) mapping faces to a hypersphere embedding.

## Loss Function
* **Additive Angular Margin Loss:**
  $$\mathcal{L} = -\frac{1}{N} \sum_{i=1}^{N} \log \frac{e^{s \cos(\theta_{y_i} + m)}}{e^{s \cos(\theta_{y_i} + m)} + \sum_{j \neq y_i} e^{s \cos \theta_j}}$$
  Where $m$ is the angular margin, $s$ is the scale parameter, and $\theta$ is the angle between embedding and weight.

## Input & Output
* **Input:** Aligned face images ($112 \times 112$).
* **Output:** 512-dimensional face embedding vector on a hypersphere.

## Advantages
* Extremely high discriminative power.
* Geometrically intuitive optimization directly on angles.
* Easy to implement with low overhead.

## Limitations
* Highly sensitive to image alignment and noise in label datasets.

## How can we use it?
* In **Module 5 (Evaluation)**, we use pretrained ArcFace models to extract face embeddings of the generated sketches and check similarity to the ground truth photos to verify identity preservation.

## Implementation Status
* **Completed** (Prototype evaluation script set up in `prototypes/arcface/`).

## Notes
* Provides excellent performance for evaluating how close a generated sketch is to a reference photo.\n