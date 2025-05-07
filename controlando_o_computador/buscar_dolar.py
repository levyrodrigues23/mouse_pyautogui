import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#o pyautogui é uma biblioteca que simula o mouse e o teclado, ou seja, ele consegue clicar em posicoes especificas do computador e escrever palavras
#ele simula qualquer automacao que envolva a interface do usuario

tempoEspera.sleep(2)  #aguarda um segundo, ou seja, um tempo de espera para que o computador possa pensar

'''
para determinar uma posicao, escreve um print posicaoMouse.position() e depois coloca a posicao desejada no lugar do (21, 877)
'''

#move o botao
posicaoMouse.moveTo(21, 877)

tempoEspera.sleep(3)  #aguarda um segundo, ou seja, um tempo de espera para que o computador possa pensar

#clica na posicao em que o mouse esta posicionado
posicaoMouse.click(21, 877)

tempoEspera.sleep(3)  

posicaoMouse.write('google chrome', interval=0.25) 

tempoEspera.sleep(3)  

posicaoMouse.press('enter') # o press pressiona algo, no caso o enter

tempoEspera.sleep(3)

posicaoMouse.write('dolar hoje', interval=0.25) #escreve 'dolar hoje' com um intervalo de 0.25 segundos entre cada letra

tempoEspera.sleep(3)

posicaoMouse.press('enter') 



