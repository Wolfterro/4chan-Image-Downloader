# 4chan Image Downloader
#### Um simples programa em Python + PyQt4 que baixa imagens e vídeos do 4chan!

### Descrição:

###### Este é um simples programa escrito em Python e utiliza PyQt4 para a utilização de uma interface gráfica (GUI) simples e leve.

###### Este programa realiza o download de imagens (.jpg, .png e .gif) e vídeos (.webm) do tópico escolhido em uma board específica do 4chan.

###### Ao escolher a board e o tópico desejado, o programa irá fazer uma varredura para determinar a quantidade de imagens e vídeos disponíveis. Ele então irá fazer o download de todos os arquivos do tópico para a pasta que você tenha escolhido ou para a pasta 4chan do usuário atual, caso não tenha escolhido nenhuma pasta de destino.

![4chan Image Downloader](https://raw.githubusercontent.com/Wolfterro/wolfterro.github.io/master/posts/img/imagens_de_projetos/4chan_image_downloader.png)

### Requisitos:

#### Compilando:
- Python 2.7
- PyQt4 para Python 2.7
- PyInstaller

###### Execute o PyInstaller para compilar o programa:

      - Linux:
      pyinstaller --icon="Icon.ico" --noconsole --onefile "4chan Image Downloader.py"
      
      - Windows
      pyinstaller --icon="Icon.ico" --noconsole --onefile "4chan Image Downloader.pyw"

#### Binário:
- Pode ser executado diretamente, sem qualquer requisito ou dependência.

### Download e Execução:
- Utilizando o git:

            git clone https://github.com/Wolfterro/4chan-Image-Downloader.git

#### Linux: https://github.com/Wolfterro/4chan-Image-Downloader/releases/tag/v1.0-Linux

#### Windows: https://github.com/Wolfterro/4chan-Image-Downloader/releases/tag/v1.0-Windows

###### Caso não possua o git e queira também baixar o repositório por completo, baixe através deste [Link](https://github.com/Wolfterro/4chan-Image-Downloader/archive/master.zip) ou clique em "Clone or Download", no topo da página.
