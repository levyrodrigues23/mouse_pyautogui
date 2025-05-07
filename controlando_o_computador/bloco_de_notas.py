import pyautogui as posicaoAbrir

# mesma coisa que pressionar as teclas do teclado
# ele abre a tela do executar
posicaoAbrir.hotkey('win', 'r')
posicaoAbrir.sleep(2) 
posicaoAbrir.write('notepad', interval=0.25) 

posicaoAbrir.sleep(2)
posicaoAbrir.press('enter') 

posicaoAbrir.sleep(2)
posicaoAbrir.write('ola, tudo bem...eu acabei de abrir o meu bloco de notas usando um robo automatico com pyautogui', interval=0.15)

#o getActiveWindow() retorna a janela ativa no momento, ou seja, o bloco de notas que acabamos de abrir 
fecharBlocoDeNotas = posicaoAbrir.getActiveWindow()
posicaoAbrir.sleep(2)
fecharBlocoDeNotas.close() #fecha a janela ativa, ou seja, o bloco de notas que acabamos de abrir

posicaoAbrir.sleep(2)

#tecla tab para ir no botao do meio
posicaoAbrir.press('tab') 
posicaoAbrir.sleep(2)
posicaoAbrir.press('enter') #pressiona o enter para confirmar o fechamento do bloco de notas

print("automacao executada com sucesso")


