import random

vet1 = []
vet2 = []
vet3 = []

for i in range(0,10):
	vet1.append(random.randrange(1,101)) 
	vet2.append(random.randrange(1,101))

for i,j in zip(vet1, vet2):
	vet3.append(i)
	vet3.append(j)

print("Elementos do vetor 1")
for i in range(0,10):
	print(vet1[i], end=' ')

print("\n\nElementos do vetor 2")
for i in range(0,10):
	print(vet2[i], end=' ')

print("\n\nElementos do vet1 e vet2 intercalados no vet3")
for i in range(0,20):
	print(vet3[i], end=' ')