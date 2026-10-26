import torch

vector = torch.tensor([1, 2, 3])
print(torch.matmul(vector, vector))
print(vector @ vector)  # same as above