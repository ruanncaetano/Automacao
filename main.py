import pyautogui
import time
import pandas
import numpy
import openpyxl


pyautogui.PAUSE = 0.5

# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# acessando o sistema disponivel 
time.sleep(2) # esperando um tempo pro crome ABRIR
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

# apos acessar o site pode ter uma demora para acessar o site
time.sleep(2)

pyautogui.click(x=811, y=470)

#digitando o e-mail

pyautogui.write("email.teste@gamil.com")
pyautogui.press("tab")
pyautogui.write("naotemsenha")
pyautogui.press("tab") 
pyautogui.press("enter")

# lendo dase de dados
tabelas_prod = pandas.read_csv("produtos.csv")
#print(tabelas_prod)

# cadastrar os produtos
for linha in tabelas_prod.index:

    

    # clica no primeiro campo
    time.sleep(2)
    pyautogui.click(x=684, y=325)
    codigo = str(tabelas_prod.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    
    pyautogui.write(str(tabelas_prod.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabelas_prod.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabelas_prod.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabelas_prod.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabelas_prod.loc[linha, "custo"]))
    pyautogui.press("tab")
    if(str(tabelas_prod.loc[linha, "obs"]) != "nan"):
        pyautogui.write(str(tabelas_prod.loc[linha, "obs"]))
        pyautogui.press("tab")
    else:
        pyautogui.press("tab")
    # cadastra o prod da o enter final
    pyautogui.press("enter")

    # rolar a tela pra cima de novo
    pyautogui.scroll(5000) # quantidade alta pois os valores de scroll são pequenos, colocar negativo pra ir pra baixo
    
