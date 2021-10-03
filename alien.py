import pygame

class Alien():
	multiplicador_velocidade = 1
	
	@classmethod
	def inicializar_velocidade(cls):
		cls.multiplicador_velocidade = 1
	
	@classmethod
	def aumentar_velocidade(cls):
		cls.multiplicador_velocidade *= 2
	
	def __init__(self, janela):
		self.janela = janela
		self.imagem = pygame.image.load('imagens/alien.bmp')

		self.retangulo = self.imagem.get_rect()
		self.retangulo_janela = self.janela.get_rect()
		
		self.x = float(self.retangulo.x)
		self.y = float(self.retangulo.y)
		
		self.direcao = 1 # alien se movendo para direita
		
	def atualizar(self, direcao_frota):
		if self.direcao != direcao_frota:
			self.y += 15
			self.direcao = direcao_frota
			
		self.x += 0.1 * self.direcao * Alien.multiplicador_velocidade
		self.retangulo.x = self.x
		self.retangulo.y = self.y
		
	def desenhar(self):
		self.janela.blit(self.imagem, self.retangulo)
		
	def atingiu_borda(self):
		if self.retangulo.right >= self.retangulo_janela.right:
			return True
		elif self.retangulo.left <= 0:
			return True
		return False
