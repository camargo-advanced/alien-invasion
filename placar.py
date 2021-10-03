import pygame.font
from nave import Nave

class Placar():
	def __init__(self, janela, estats):
		self.janela = janela
		self.retangulo_janela = janela.get_rect()
		self.estats = estats
		
		self.cor_texto = (30,30,30)
		self.fonte = pygame.font.SysFont(None, 48)
		
	def atualizar(self):
		# atualiza o placar de pontos
		pontos_arredondados = int(round(self.estats.pontos, -1))
		pontos_str = "{:,}".format(pontos_arredondados)
	
		self.imagem = self.fonte.render(pontos_str, True, \
			self.cor_texto, (230,230,230))
		self.retangulo = self.imagem.get_rect()
		self.retangulo.right = self.retangulo_janela.right - 20
		self.retangulo.top = 20
		
		# atualizar o placar de vidas
		self.naves = []
		for numero_nave in range(self.estats.naves_disponiveis):
			nave = Nave(self.janela)
			nave.retangulo.x = 10 + numero_nave * nave.retangulo.width
			nave.retangulo.y = 10
			self.naves.append(nave)
		
	def desenhar(self):
		self.janela.blit(self.imagem, self.retangulo)
		for nave in self.naves:
			nave.desenhar()
