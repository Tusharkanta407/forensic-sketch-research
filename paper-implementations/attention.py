import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        # TODO: Initialize projections for Q, K, V and output projection
        pass
        
    def forward(self, q, k, v, mask=None):
        # TODO: Implement scaled dot-product attention and multi-head merging
        return None, None

# Test block
if __name__ == "__main__":
    print("MultiHeadAttention template ready for implementation.")
