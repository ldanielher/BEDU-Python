# Inicializa variables y lista con números
fibo = [0]
i = 0
num = 1

#Genera ciclo
while num < 1000:
	fibo.append(num)
	i += 1
	num = fibo[i] + fibo[i-1]

#Imprime resultado
for num in fibo:
	print(num)