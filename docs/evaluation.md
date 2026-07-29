# Evaluation Metrics

To measure model effectiveness during the research phase, we utilize three main evaluation domains:

## 1. Face Generation Quality
* **Fréchet Inception Distance (FID):** Measures semantic similarity between generated and real images. Lower is better.
* **Inception Score (IS):** Evaluates image sharpness and diversity.

## 2. Text-Image Alignment
* **CLIP Score:** Evaluates how well the generated image matches the input natural language description.
* **Attribute Consistency:** Measuring the percentage of generated images that correctly display the requested attributes (e.g., gender, eye color).

## 3. Identity Preservation (Evaluation Module)
To check if the generator retains the identity details:
$$\text{Similarity Score} = \cos(\theta) = \frac{\mathbf{e}_1 \cdot \mathbf{e}_2}{\|\mathbf{e}_1\| \|\mathbf{e}_2\|}$$
Where $\mathbf{e}_1$ is the ArcFace embedding of the generated sketch, and $\mathbf{e}_2$ is the embedding of the ground truth photo.\n