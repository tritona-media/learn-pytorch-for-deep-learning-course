import torch

vector = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16, device="cpu", requires_grad=False)

print(vector, vector.shape, vector.dtype, vector.device, vector.requires_grad)
