import torch

vector = torch.tensor([1, 2, 3])
print(vector + 10)
print(vector * 10)
print(vector - 10)
print(vector / 10)

vector = vector * vector
print(vector)