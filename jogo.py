import pygame
import sys
from gerador import gera_numeros

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)

# Variáveis
x_pos = largura // 2
y_pos = altura // 2
quadrado = 50
altura_plataforma = 20
largura_plataforma = 100

# Função para criar o cenário
def desenha_jogo(numeros, quadrados_visiveis):
    tela.fill(branco)
    pygame.draw.rect(tela, cinza, (x_pos - largura_plataforma // 2, y_pos + quadrado, largura_plataforma, altura_plataforma))
    
    cores = [vermelho, verde, azul]
    quadrados = [q1, q2, q3]
    
    for i in range(3):
        if quadrados_visiveis[i]:
            pygame.draw.rect(tela, cores[i], (quadrados[i][0], quadrados[i][1], quadrado, quadrado))
            texto = fonte.render(str(numeros[i]), True, preto)
            tela.blit(texto, (quadrados[i][0] + 10, quadrados[i][1] + 10))
    
    texto = fonte.render(str(numeros[3]), True, preto)
    tela.blit(texto, (10, 10))
    pygame.display.flip()

# Função para verificar se o clique foi dentro de um quadrado
def verifica_clique(pos, quadrados_visiveis):
    quadrados = [q1, q2, q3]
    for i in range(3):
        # Verifica se o clique está dentro do quadrado
        if quadrados_visiveis[i] and quadrados[i][0] <= pos[0] <= quadrados[i][0] + quadrado and quadrados[i][1] <= pos[1] <= quadrados[i][1] + quadrado:
            return i
    return -1

# Função para reiniciar o jogo
def reiniciar_jogo():
    return gera_numeros(), [True, True, True]

# inicialização
fonte = pygame.font.Font(None, 36)
numeros, quadrados_visiveis = reiniciar_jogo()

# Coord quadrados
q1 = (x_pos - quadrado // 2, y_pos - 2 * quadrado)
q2 = (x_pos - quadrado // 2, y_pos - quadrado)
q3 = (x_pos - quadrado // 2, y_pos)

# Jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clique = verifica_clique(event.pos, quadrados_visiveis)
            if clique != -1:
                if clique == numeros[4]:  
                    mensagem = "Certo!"
                else:
                    mensagem = "Errado!"
                quadrados_visiveis[clique] = False
                desenha_jogo(numeros, quadrados_visiveis)
                texto = fonte.render(mensagem, True, preto)
                quadrados = [q1, q2, q3]
                tela.blit(texto, (quadrados[clique][0], quadrados[clique][1]))
                pygame.display.flip()
                pygame.time.wait(1000)
                numeros, quadrados_visiveis = reiniciar_jogo()
    
    desenha_jogo(numeros, quadrados_visiveis)

pygame.quit()
sys.exit()
