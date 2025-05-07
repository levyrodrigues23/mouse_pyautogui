import pyautogui as escolha_opcao

opcao = escolha_opcao.confirm('clique no botao desejado', buttons=['Excel', 'Word', 'Notepad']) # o confirm abre uma janela de confirmacao, ou um alert, com os botoes que passamos como parametro, e o usuario pode clicar em um deles. O valor retornado e o nome do botao clicado.

if opcao == 'Excel':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.write('excel', interval=0.09)
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.moveTo(254, 187)
    escolha_opcao.sleep(2)
    escolha_opcao.click(254, 187)
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite("escolhi abrir com excel")
    print("vc escolheu o Excel")
elif opcao == 'Word':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.write('winword', interval=0.09)
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite("escolhi abrir com word")
    print("vc escolheu o Excel")
else:
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.write('notepad', interval=0.09)
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.typewrite("escolhi abrir com notepad")
    print("vc escolheu o Excel")