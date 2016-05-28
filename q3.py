def taxaA(arg):
	return arg + (arg*0.03)

def taxaB(arg):
	return arg + (arg*0.015)

popA = 80000
popB = 200000
tempo = 0

while popA < popB:
	popA = taxaA(popA)
	POPB = taxaB(popB)
	tempo = tempo + 1

print(tempo)
