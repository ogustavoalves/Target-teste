

fibonacci = [0, 1] # início da sequência

# entrada de número
user_num = int(input("Digite um número: "))

# populando a lista 
x = 0

while (user_num >= fibonacci[x]):
    num_fibo = fibonacci[x] + fibonacci[x-1]
    fibonacci.append(num_fibo)
    x = x + 1

print(str(fibonacci)) # exibir sequência
print(len(fibonacci))

# procura o número na sequência
if user_num in fibonacci:
    print(f"o número {user_num} está na sequencia")
else:
    print(f"número {user_num} não encontrado")
    


# tentar contemplar todos os casos segundo o input do usuário
