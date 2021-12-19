import pygame

class Nave():
	def __init__(self, janela):
		self.janela = janela
		self.imagem = pygame.image.load('imagens/nave.png').convert_alpha()
		
		self.retangulo = self.imagem.get_rect()
		self.retangulo_janela = self.janela.get_rect()
		
		self.centerx = float(self.retangulo_janela.centerx) # posiciona centro
		self.retangulo.centerx = self.centerx
		self.retangulo.bottom = self.retangulo_janela.bottom # posiciona baixo
		self.v = 350 # velocidade em pixels por segundo 
		
		self.movendo_direita = False
		self.movendo_esquerda = False
	
	def centralizar(self):
		self.centerx = float(self.retangulo_janela.centerx)
		self.retangulo.centerx = self.centerx
		
	def atualizar(self, tempo_decorrido):
		distancia = tempo_decorrido * self.v # distancia percorrida em pixels 
		if self.movendo_direita and self.retangulo.right < self.retangulo_janela.right:
			self.centerx += distancia
			self.retangulo.centerx = self.centerx
		if self.movendo_esquerda and self.retangulo.left > 0:
			self.centerx -= distancia
			self.retangulo.centerx = self.centerx
	
	def desenhar(self):
		self.janela.blit(self.imagem, self.retangulo)
		
