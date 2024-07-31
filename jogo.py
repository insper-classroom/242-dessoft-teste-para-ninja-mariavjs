import pygame
import sys
import time
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
vidas = 3
tempo_jogo = 60  # 1 minuto
inicio_tempo = None
estado_jogo = "inicio"
pontuacao = 0
q1 = (x_pos - quadrado // 2, y_pos - 2 * quadrado)
q2 = (x_pos - quadrado // 2, y_pos - quadrado)
q3 = (x_pos - quadrado // 2, y_pos)


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
    
    # Desenha vidas e tempo restante
    texto_vidas = fonte.render(f"VIDAS: {vidas}", True, preto)
    tela.blit(texto_vidas, (largura - 150, 10))
    tempo_restante = max(0, tempo_jogo - int(time.time() - inicio_tempo))
    texto_tempo = fonte.render(f"TEMPO: {tempo_restante}s", True, preto)
    tela.blit(texto_tempo, (largura - 150, 50))
    
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

# Função para desenhar a tela de início
def desenha_tela_inicio():
    tela.fill(branco)
    texto = fonte.render("CLIQUE PARA INICIAR", True, preto)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 2))
    pygame.display.flip()

# Função para desenhar a tela de perdeu
def desenha_tela_fim():
    tela.fill(branco)
    texto = fonte.render(f"FIM DE JOGO! SCORE: {pontuacao}", True, preto)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 2))
    pygame.display.flip()

# inicialização
fonte = pygame.font.Font(None, 36)
numeros, quadrados_visiveis = reiniciar_jogo()

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if estado_jogo == "inicio":
                estado_jogo = "jogo"
                inicio_tempo = time.time()
            elif estado_jogo == "jogo":
                clique = verifica_clique(event.pos, quadrados_visiveis)
                if clique != -1:
                    if clique == numeros[4]:  
                        mensagem = "CORRETO!"
                        pontuacao += 1
                    else:
                        mensagem = "ERRRADO!"
                        vidas -= 1
                    quadrados_visiveis[clique] = False
                    desenha_jogo(numeros, quadrados_visiveis)
                    texto = fonte.render(mensagem, True, preto)
                    quadrados = [q1, q2, q3]
                    tela.blit(texto, (quadrados[clique][0], quadrados[clique][1]))
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    numeros, quadrados_visiveis = reiniciar_jogo()
    
    if estado_jogo == "inicio":
        desenha_tela_inicio()
    elif estado_jogo == "jogo":
        desenha_jogo(numeros, quadrados_visiveis)
        if vidas <= 0 or time.time() - inicio_tempo >= tempo_jogo:
            estado_jogo = "fim"
    elif estado_jogo == "fim":
        desenha_tela_fim()

pygame.quit()
sys.exit()