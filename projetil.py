import pygame

class Projetil():
	multiplicador_velocidade = 1
	
	@classmethod
	def inicializar_velocidade(cls):
		cls.multiplicador_velocidade = 1
	
	@classmethod
	def aumentar_velocidade(cls):
		cls.multiplicador_velocidade *= 2
	
	def __init__(self, janela, nave):
		self.janela = janela
		
		self.retangulo = pygame.Rect(0,0,3,15)
		self.retangulo.centerx = nave.retangulo.centerx
		self.retangulo.top = nave.retangulo.top
		
		self.y = float(self.retangulo.y)
		
	def atualizar(self):
		self.y -= 0.3 * Projetil.multiplicador_velocidade
		self.retangulo.y = self.y
		
	def desenhar(self):
		pygame.draw.rect(self.janela, (60,60,60), self.retangulo)
		
		
