# Paper Name: Attention Is All You Need

## Authors
* Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin

## Year
* 2017

## Problem
* Traditional sequence models (RNN, LSTM, GRU) process tokens sequentially, limiting parallelization during training and failing to capture long-range dependencies efficiently.

## Architecture
* **Transformer:** Encoder-Decoder structure entirely built on self-attention and feed-forward networks, omitting recurrence. Uses Multi-Head Attention, Scaled Dot-Product Attention, and Positional Encodings.

## Loss Function
* Label smoothed cross-entropy loss.

## Input & Output
* **Input:** Sequences of token embeddings + positional encodings.
* **Output:** Predicted token probabilities for the next sequence element.

## Advantages
* Massively parallelizable training.
* Captures global dependencies regardless of distance in sequence.
* State-of-the-art results in NLP translation tasks.

## Limitations
* High quadratic computational complexity ($O(N^2)$) relative to sequence length due to the self-attention matrix.

## How can we use it?
* We use the Encoder block of the Transformer to parse natural language descriptions of witnesses into structured JSON representation tokens (Module 1).

## Implementation Status
* **In Progress** (Prototype parser utilizing self-attention mechanism).

## Notes
* Foundational paper for all modern large language models.\n