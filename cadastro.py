import pyautogui
import pandas as pd
import time

arquivo = pd.read_csv('arquivo.csv')

pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)
pyautogui.write('https://cadastro-produto.netlify.app/')
pyautogui.press('enter')

for linha in arquivo.index:
    time.sleep(2)
    pyautogui.click(x=502, y=229)
    for coluna in arquivo.columns:
        pyautogui.write(str(arquivo.loc[linha, coluna]))
        pyautogui.press('tab')
    pyautogui.press('enter')