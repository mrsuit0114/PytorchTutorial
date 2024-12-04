import torch
import numpy as np

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data) # 기본이 int64
print(x_data)
print("="*50,'\n')

np_array = np.array(data)
x_np = torch.from_numpy(np_array) # 기본이 int32
print(x_np)
print("="*50,'\n')

x_ones = torch.ones_like(x_data) # x_data의 속성을 유지합니다.
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # x_data의 속성을 덮어씁니다.
print(f"Random Tensor: \n {x_rand} \n")
print("="*50,'\n')

shape=(2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")
print("="*50,'\n')

tensor = torch.rand(3,4,)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")
print("="*50,'\n')

if torch.cuda.is_available():
    tensor = tensor.to("cuda")

tensor = torch.ones(4,4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:,0]}")
print(f"Last Column: {tensor[...,-1]}")
tensor[...,1] = 0
print(tensor)
print("="*50,'\n')

t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1.shape)
print("="*50,'\n')

# 행렬의 곱
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)
y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out=y3)
print(y1, y2, y3,sep='\n')
print("="*50,'\n')

# 요소별 곱
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand(2,3) # 크기에 상관없이 torch면 덮어씌워짐
 # 메모리 할당을 줄이고 효율성을 높이기 위해 이미 생성된 Tensor객체에 덮어쓰도록 설계됨
 # 리사이즈에도 메모리 재할당을 유발할 수 있으므로 크기를 맞추는게 좋다.
z4 = torch.mul(tensor,tensor, out=z3)
print(z1, z2, z3, z4,sep='\n')
print("="*50,'\n')

agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))
print("="*50,'\n')

# in-place연산(접미사_)는 피연산자를 변경하여 메모리 절약이 가능하지만
# 기록이 즉시 삭제되어 도함수 계산 문제 위험이 있어 사용을 권장하지 않음
tensor.add_(5)
print(tensor)
print("="*50,'\n')

t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")
print("="*50,'\n')

k = t.add(1)
t.add_(1)
print(f"k: {k}")
print(f"t: {t}")
print("="*50,'\n')


n = np.ones(5)
t = torch.from_numpy(n)

tmp = np.add(n, 1, out = n)
print(f"t: {t}")
print(f"n: {n}")
print(f"tmp: {tmp}")
print("="*50,'\n')
