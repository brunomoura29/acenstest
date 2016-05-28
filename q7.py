#tecnica simples usando shift
def cifraCesar(frase,shift):

	alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	dic={}
	for i in range(0,len(alfabeto)):
		dic[alfabeto[i]]=alfabeto[(i+shift)%len(alfabeto)]

	cifrado=""
	for l in frase.lower():
		if l in dic:
			l=dic[l]
		cifrado+=l
	
	return cifrado

def decifrar(frase,shift):

	alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	dic={}
	for i in range(0,len(alfabeto)):
		dic[alfabeto[i]]=alfabeto[(i-shift)%len(alfabeto)]

	cifrado=""
	for l in frase.lower():
		if l in dic:
			l=dic[l]
		cifrado+=l

	return cifrado

frase="A uece esta de greve"
print ("frase original:", frase)
print ("Frase cifrada:", cifraCesar(frase ,3))

fraseCifrada = cifraCesar(frase,3)
print ("Frase decifrada:", decifrar(fraseCifrada,3))
