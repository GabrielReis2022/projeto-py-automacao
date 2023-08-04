### Projeto --- Python Automação ---

# Passo 1: Entrar no sistema da empresa

import pyautogui
import time


## pyautogui.write # escrever um texto
## pyautogui.press # apertar 1 tecla do teclado
## pyautogui.click # para clicar em algum lugar da tela
## pyautogui.hotkey("ctrl", "c") # para usar comando de teclas

pyautogui.PAUSE = 0.3  # para dar tempo do computador pensar


# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)  # dar tempo a linha especifica usando o import time


# Passo 2: Fazer login
# selecionar o campo de email.
pyautogui.click(x=650, y=407)
# escrever o email
pyautogui.write("gabrielreisant.ana@gmail.com")
pyautogui.press("tab")  # passando para o proximo campo
pyautogui.write("sua senha")
pyautogui.click(x=666, y=552)  # clique no botao de login
time.sleep(3)


# passo 3: importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)
# passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de codigo
    pyautogui.click(x=527, y=277)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))

    #  passar para o proximo campo
    pyautogui.press("tab")

    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # verificar se a celular esta vazia
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # dar um scroll de tudo para cima, e depois o proximo produto
    pyautogui.scroll(5000)

# passo 5: Repetir o processo de cadastro até o fim
