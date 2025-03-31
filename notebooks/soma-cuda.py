import torch
# Tamanho das matrizes
N = 32

# Verificar se CUDA está disponível
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Usando dispositivo: {device}')
# Cria as matrizes na memória da CPU
matrix_a = torch.rand((N, N))
matrix_b = torch.rand((N, N))

# Move os dados para a GPU
matrix_a = matrix_a.to(device)
matrix_b = matrix_b.to(device)

# Soma das matrizes
matrix_sum = matrix_a + matrix_b

# Transferir o resultado para a CPU
matrix_sum_cpu = matrix_sum.cpu()

print("\nSoma das Matrizes (na CPU):")
print(matrix_sum_cpu)