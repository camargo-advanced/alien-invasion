import pygame

class Botao():
	def __init__(self, janela, texto):
		self.janela = janela
		self.retangulo_janela = janela.get_rect()
		
		self.retangulo = pygame.Rect(0,0,200,50)
		self.retangulo.center = self.retangulo_janela.center
		
		self.fonte = pygame.font.SysFont(None, 48)
		self.cor_fundo = (255, 165, 0) # laranja
		self.cor_texto = (255, 255, 255) # branco
		self.imagem_texto = self.fonte.render(texto, True, \
			self.cor_texto, self.cor_fundo)
			
		self.retangulo_texto = self.imagem_texto.get_rect()
		self.retangulo_texto.center = self.retangulo.center
		
	def desenhar(self):
		self.janela.fill(self.cor_fundo, self.retangulo)
		self.janela.blit(self.imagem_texto, self.retangulo_texto)
		
