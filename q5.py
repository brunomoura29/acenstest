def telefoneValido(lista):
	for i in range(6):
		if lista[i]==lista[i+1]:
			return False
	if lista[0]==lista[5]:
		return False

	return true

arquivo = open("telefones.txt", "r")
telefones = arquivo.read()

#while (telefones.getString()!='\n'):
#	print(telefones)
#	print("\n")