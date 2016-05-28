from bs4 import BeautifulSoup
import urllib.request

url = "http://siasdo.com.br/"
pagina = urllib.request.urlopen(url).read()

soup = BeautifulSoup(pagina, "html.parser")

print(pagina)



