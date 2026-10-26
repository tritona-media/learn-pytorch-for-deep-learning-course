import torch

range_tensor = torch.arange(start=0, end=10, step=1)
print(range_tensor)

print(torch.zeros_like(input=range_tensor))
print(torch.ones_like(input=range_tensor))