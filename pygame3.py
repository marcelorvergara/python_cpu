import pygame, cpuinfo,psutil

PRETO = (0,0,0)
BRANCO = (255,255,255)
CINZA = (100,100,100)
VERMELHO = (255,0,0)
AZUL = (0,0,255)

LARGURA_TELA = 800
ALTURA_TELA = 600

def mostra_info_cpu():
    s1.fill(BRANCO)
    mostra_texto(s1, "Nome:", "brand_raw", 10)
    mostra_texto(s1, "Arquitetura:", "arch", 30)
    mostra_texto(s1, "Palavra (bits):", "bits", 50)
    mostra_texto(s1, "Frequência (Mhz):", "freq", 70)
    mostra_texto(s1, "Núcleos (físicos):", "nucleos", 90)
    tela.blit(s1, (0, 0))

def mostra_texto(s1, nome, chave, pos_Y):
    text = font.render(nome, True, PRETO)
    s1.blit(text, (10, pos_Y))
    if(chave == "freq"):
        s = str(round(psutil.cpu_freq().current, 2))
    elif(chave == "nucleos"):
        s = str(psutil.cpu_count())
        s += " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        s = str(info_cpu[chave])
    text = font.render(s, True, CINZA)
    s1.blit(text, (160, pos_Y))

def mostra_uso_cpu(s,l_cpu_percent):
    s.fill(CINZA)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - (2 * y)
    larg = (s.get_width() - (2 * y) - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    #imprimir as barras
    for i in l_cpu_percent:
        print(i)
        pygame.draw.rect(s,VERMELHO, (d, y, int(larg), int(alt)))
        pygame.draw.rect(s,AZUL, (d, y, int(larg), int(((1 - (i / 100)) * alt))))
        d += larg + desl
    tela.blit(s, (0,int(ALTURA_TELA / 5)))

info_cpu = cpuinfo.get_cpu_info()

# tela
tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()

# surface
s1 = pygame.surface.Surface((LARGURA_TELA,ALTURA_TELA))
# parte das barras
s2 = pygame.surface.Surface((LARGURA_TELA,ALTURA_TELA))

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
            mostra_info_cpu()
            l_cpu_percent = psutil.cpu_percent(percpu=True)
            mostra_uso_cpu(s2,l_cpu_percent)
            cont = 0
        # update da tela
        pygame.display.update()
        clock.tick(60)
        cont += 1

# fechar pygame
pygame.display.quit()
