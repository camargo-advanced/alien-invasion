import sys
import pygame
from nave import Nave
from projetil import Projetil
from alien import Alien
from estatisticas import Estatisticas
from time import sleep
from botao import Botao
from placar import Placar

def rodar_jogo():
	pygame.init()
	janela = pygame.display.set_mode((900,600))
	pygame.display.set_caption("Invasao Alienigena")
	
	nave = Nave(janela)
	projeteis = []
	aliens = []
	criar_frota_alienigena(janela, aliens, nave)
	direcao_frota = 1 # direita
	estats = Estatisticas()
	botao = Botao(janela, "Jogar")
	placar = Placar(janela, estats)
	clock = pygame.time.Clock() # objeto relogio

	while True:
		# Tempo decorrido entre frame anterior e esse
		tempo_decorrido = clock.tick(60) / 1000.0

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sys.exit()
			elif evento.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if not estats.jogo_ativo and \
					obtem_mouse_colidiu_botao(mouse_x, mouse_y, botao):
						estats.jogo_ativo = True
						estats.reiniciar()
						pygame.mouse.set_visible(False)
						Alien.inicializar_velocidade()
						Projetil.inicializar_velocidade()
			elif evento.type == pygame.KEYDOWN:
				if estats.jogo_ativo:
					if evento.key == pygame.K_RIGHT:
						nave.movendo_direita = True
					if evento.key == pygame.K_LEFT:
						nave.movendo_esquerda = True
					if evento.key == pygame.K_SPACE:
						if len(projeteis) < 3:
							novo_projetil = Projetil(janela, nave)
							projeteis.append(novo_projetil)
			elif evento.type == pygame.KEYUP:
				if estats.jogo_ativo:
					if evento.key == pygame.K_RIGHT:
						nave.movendo_direita = False
					if evento.key == pygame.K_LEFT:
						nave.movendo_esquerda = False
		
		placar.atualizar()
		
		if estats.jogo_ativo:
			#atualizando posicionamentos na janela
			nave.atualizar(tempo_decorrido)
			
			for projetil in projeteis:
				projetil.atualizar(tempo_decorrido)
				
			for projetil in projeteis.copy():
				if projetil.retangulo.bottom <= 0:
					projeteis.remove(projetil)
			
			for alien in aliens:
				if alien.atingiu_borda():
					direcao_frota *= -1
					break
			
			for alien in aliens:
				alien.atualizar(tempo_decorrido, direcao_frota)
				
			if len(aliens) == 0:
				projeteis.clear()
				criar_frota_alienigena(janela, aliens, nave)
				direcao_frota = 1
				Alien.aumentar_velocidade()
				Projetil.aumentar_velocidade()
				
			colisoes = obtem_colisoes_projeteis_aliens(projeteis, aliens)
			if len(colisoes):
				estats.pontos += 50 * len(colisoes) * Alien.multiplicador_velocidade
			remove_colisoes_projeteis_aliens(colisoes, projeteis, aliens)
				
			alien_colidiu_nave = obtem_alien_colidiu_nave(aliens, nave)
			alien_fim_janela = obtem_alien_fim_janela(aliens, nave)
			
			if alien_colidiu_nave or alien_fim_janela:
				projeteis.clear()
				aliens.clear()
				criar_frota_alienigena(janela, aliens, nave)
				direcao_frota = 1
				nave.centralizar()
				if estats.naves_disponiveis > 0:
					estats.naves_disponiveis -= 1
					sleep(1)
					clock.tick()
				else:
					estats.naves_disponiveis = 0
					estats.jogo_ativo = False
					pygame.mouse.set_visible(True)
					
		# desenhando no buffer
		janela.fill((230, 230, 230))
		nave.desenhar()
		for projetil in projeteis:
			projetil.desenhar()
		for alien in aliens:
			alien.desenhar()
		if not estats.jogo_ativo:
			botao.desenhar()	
		placar.desenhar()
		
		pygame.display.flip()
	
def criar_frota_alienigena(janela, aliens, nave):
	alien = Alien(janela)
	largura_alien = alien.retangulo.width
	altura_alien = alien.retangulo.height
	largura_janela, altura_janela = pygame.display.get_surface().get_size()
	altura_nave = nave.retangulo.height
	
	espaco_disponivel_x = largura_janela - 2 * largura_alien
	numero_aliens_x = int(espaco_disponivel_x / (2 * largura_alien))
	
	espaco_disponivel_y = altura_janela - altura_nave - 3 * altura_alien
	numero_aliens_y = int(espaco_disponivel_y / (2 * altura_alien))
	
	for numero_do_alien in range(numero_aliens_x):
		for numero_linha in range(numero_aliens_y):
			alien = Alien(janela)
			alien.x = largura_alien + 2 * largura_alien * numero_do_alien
			alien.retangulo.x = alien.x 
			
			alien.y = altura_alien + 2 * altura_alien * numero_linha
			alien.retangulo.y = alien.y
	
			aliens.append(alien)

def obtem_colisoes_projeteis_aliens(projeteis, aliens):
	colisoes = {}
	for projetil in projeteis:
		for alien in aliens:
			if projetil.retangulo.centerx >= alien.retangulo.left and \
				projetil.retangulo.centerx <= alien.retangulo.right and \
				projetil.retangulo.top >= alien.retangulo.top and \
				projetil.retangulo.top <= alien.retangulo.bottom:
					colisoes[projetil] = alien
	return colisoes
	
def remove_colisoes_projeteis_aliens(colisoes, projeteis, aliens):
	for projetil in list(set(colisoes.copy().keys())):
		projeteis.remove(projetil)
		
	for alien in list(set(colisoes.copy().values())):
		aliens.remove(alien)

def obtem_alien_colidiu_nave(aliens, nave):
	for alien in aliens:
		if alien.retangulo.centerx >= nave.retangulo.left and \
			alien.retangulo.centerx <= nave.retangulo.right and \
			alien.retangulo.bottom >= nave.retangulo.top:
				return alien
				
def obtem_alien_fim_janela(aliens, nave):
	for alien in aliens:
		if alien.retangulo.bottom >= nave.retangulo.bottom:
			return alien

def obtem_mouse_colidiu_botao(mouse_x, mouse_y, botao):
	if mouse_x >= botao.retangulo.left and \
		mouse_x <= botao.retangulo.right and \
		mouse_y >= botao.retangulo.top and \
		mouse_y <= botao.retangulo.bottom:
			return True

# programa principal
rodar_jogo()
