import torch
import torch.nn as nn

class TripletLoss(nn.Module):
    def __init__(self, margin=1.0):
        super(TripletLoss, self).__init__()
        # TODO: Initialize margin parameter
        pass
        
    def forward(self, anchor, positive, negative):
        # TODO: Implement triplet loss: max(0, d(a,p) - d(a,n) + margin)
        return None

# Test block
if __name__ == "__main__":
    print("TripletLoss template ready for implementation.")
