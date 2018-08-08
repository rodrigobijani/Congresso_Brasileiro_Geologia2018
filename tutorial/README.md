# Tutorial de instalação:

Este repositório apresenta o procedimento de instalação das dependências necessárias para rodar o programa apresentado no curso Modelagem gravimétrica utilizando fontes pontuais formalmente publicado no 49o Congresso brasileiro de geologia de 20 a 24 de agosto no centro de convenções Sul América - Rio de Janeiro - RJ.

## Instrução para a instalação dos pacotes necessários no Windows:  

Clique em [Anaconda](https://www.continuum.io/) para ser redirecionado para a página de download. 

## Instrução para a instalação dos pacotes necessários no Linux:

Clique em [Anaconda](https://www.continuum.io/) para ser redirecionado para a página de download. 

* Ao abrir a página clique em Downloads 

<p align="center">
  <img src="Images/tut01.png" width="550"/>
</p>

* Abra um terminal digitando no teclado "Crt+Alt+T" e certifique se seu sistema operacional é 32 bits ou 64 bits com o comando "uname -m".

* Para sistemas 32 bits vá para "Python 2.7 version" clique em 

<p align="center">
  <img src="Images/tut02.png" width="550"/>
</p>

* Para sistemas 64 bits vá para "Python 2.7 version" clique em 

<p align="center">
  <img src="Images/tut03.png" width="550"/>
</p>

* Verifique a integridade do dado rodando o comando "md5sum /path/filename" ou "sha256sum /path/filename".

* Entre com o comando "bash ~/Downloads/Anaconda2-5.2.0-Linux-x86_64.sh" para instalar o Anaconda para a versão Python 2.7.

OBS: É necessário que o arquivo "Anaconda2-5.2.0-Linux-x86_64.sh" esteja na pasta de Downloads.

* Escolha a opção "Install Anaconda as a user".

* O prompt de instalação irá pedir para que o usuário leia os termos de lincença. 

* Após a leitura aperte "YES" para concordar. 

* Clique em "accept para aceitar" o local de instalação padrão. Em seguida, será mostrado no display "PREFIX=/home/<user>/anaconda<2 or 3>".
    
* Será perguntado ao usuário se o instalador pode criar a dependência do "Anaconda<2 or 3>" no caminho "home/<user>/.bashrc"

* Será perguntado ao usuário se ele deseja instalar o VS Coden da Microsoft. Escolha "YES" ou "NO".

* Depois disso a instalação será concluída. Em seguida feche e abra novamente o terminal para que a instalação tenha efeito ou digite "source ~/.bashrc".

* Confirme se a instalação foi bem sucedida digitando "anaconda-navigator", no terminal. Caso o navegador abra os pacotes e programas estão prontos para uso.


# Pacotes Extras: BASEMAP

O Basemap é um pacote open source que compila diversas fontes de dados de mapas. Para instalá-lo o usuário deve digitar no terminal "conda install basemap".
