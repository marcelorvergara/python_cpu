import pygame, cpuinfo,psutil

PRETO = (0,0,0)
BRANCO = (255,255,255)
CINZA = (100,100,100)

LARGURA_TELA = 800
ALTURA_TELA = 600

info_cpu = cpuinfo.get_cpu_info()

# tela
tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()

# surface
s1 = pygame.surface.Surface((LARGURA_TELA,ALTURA_TELA))

# font
pygame.font.init()
font = pygame.font.Font(None, 24)

# relógio - clock
clock = pygame.time.Clock()
cont = 60

# loop principal
terminou = False
while(not terminou):
    #checar eventos
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            terminou = True
        if(cont == 60):
            # exibir informações
            cont = 0
        # update da tela
        pygame.display.update()
        clock.tick(60)
        cont += 1

# fechar pygame
pygame.display.quit()
