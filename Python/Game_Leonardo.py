import pygame as pg

#Verifica se houve algum erro na importação do módulo
try:
    pg.init()
except:
    print('O Módulo pygame não foi inicializado com sucesso!')

largura=640
altura = 480

#Abre Janela do Jogo
pg.display.set_mode((largura,altura))
#Muda o Tituto
pg.display.set_caption('Leonardo Chorão')

sair = True

while sair:
    #Verifica todos os eventos do display aberto
    for event in pg.event.get():
        #Se user clicar em sair, a variável sair muda para false saindo do loop
        if event.type == pg.QUIT:
            sair = False
     


    #Atualiza a Tela
    pg.display.update()

#quit()
#Fecha e sai do Jogo
pg.quit()