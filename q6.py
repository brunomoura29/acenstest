from bs4 import BeautifulSoup
import urllib.request

url = "http://siasdo.com.br/"
pagina = urllib.request.urlopen(url).read()

soup = BeautifulSoup(pagina, "html.parser")

print(pagina)
#o caminho seria section/div/ul/li mas n consegui pegar




