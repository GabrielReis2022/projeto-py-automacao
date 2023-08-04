import time
import pyautogui
import os

# utiliza para pegar a posição do mouse
time.sleep(5)
print(pyautogui.position())


import pandas as pd


tabela = pd.read_csv("produtos.csv")
print(tabela)
