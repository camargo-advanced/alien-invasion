# alien-invasion
Implementação simples do jogo de invasão alienígena com fins didáticos.

Para criar esse jogo passo a passo, siga a série de vídeos no link abaixo:

<https://www.youtube.com/playlist?list=PLiu4wMrYDH6IvwMPVABUF4W0MFESxw0S_>

Para executar, basta clonar o repositório e executar:
python3 aliens.py

*****

Preparação de ambiente RaspberryPi

1 – Abra o terminal e instale/atualize o python:  
`sudo apt update`  
`sudo apt upgrade`  
`sudo apt install python3 python3-venv`  

2 – Atualize as bibliotecas SDL necessárias, como exemplo para carregar imagens PNG:  
`sudo apt install libsdl-gfx1.2-5 libsdl-image1.2 libsdl-kitchensink1 libsdl-mixer1.2 libsdl-sound1.2 libsdl-ttf2.0-0 libsdl1.2debian libsdl2-2.0-0 libsdl2-gfx-1.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0`  

3 - Instale o Visual Studio Code:  
`sudo apt install code`  
Abra o vscode (NÃO atualize o idioma !)  
Selecione “open folder”  
Selecione o caminho onde quer colocar o projeto  
Crie um diretório chamado “cip” e abra-o  
Confie nos autores desse diretório  
Instale a extensão para Python  

4 - Crie o ambiente virtual python para o projeto:  
`python3 -m venv .venv`  

5 - Configure o vscode para o novo ambiente virtual:  
Selecione View -> Command Palette -> Select interpreter -> Enter interpreter path…  
Selecione a opção do venv (recomendada)  
Abra uma nova janela no terminal para entrar no ambiente virtual  
Feche as janelas antigas do terminal  

6 - Instale a biblioteca Pygame digitando:  
`python3 -m pip install -U pygame`  
Caso receba mensagem de upgrade do pip, pode fazer  

7 - Teste o novo ambiente com um jogo de exemplo do pygame:  
`python3 -m pygame.examples.aliens`  
