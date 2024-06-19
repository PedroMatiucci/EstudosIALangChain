Como Configurar e Usar um Ambiente Virtual (venv) com Jupyter Notebooks
Este guia irá orientá-lo na criação de um ambiente virtual usando venv, ativá-lo e configurá-lo para uso com Jupyter Notebooks, além de instalar pacotes listados em um arquivo requirements.txt.

Passo 1: Criar um Ambiente Virtual
Windows, macOS e Linux
Abrir o terminal (ou Prompt de Comando no Windows).

Navegar até o diretório onde deseja criar o ambiente virtual.

Criar o ambiente virtual:

bash
Copiar código
python -m venv venv
Isso criará uma pasta chamada venv no diretório atual.

Passo 2: Ativar o Ambiente Virtual
Windows
Ativar o ambiente virtual:

bash
Copiar código
.\venv\Scripts\activate
macOS e Linux
Ativar o ambiente virtual:

bash
Copiar código
source venv/bin/activate
Você verá que o prompt do terminal mudará para indicar que o ambiente virtual está ativado, geralmente precedido pelo nome do ambiente ((venv)).

Passo 3: Instalar Pacotes do requirements.txt
Certifique-se de que o ambiente virtual está ativado (veja o Passo 2).

Criar ou copiar um arquivo requirements.txt no diretório do seu projeto.

Instalar os pacotes listados no requirements.txt:

bash
Copiar código
pip install -r requirements.txt
Isso instalará todas as bibliotecas e pacotes listados no arquivo requirements.txt.

Passo 4: Instalar o Jupyter no Ambiente Virtual
Certifique-se de que o ambiente virtual está ativado (veja o Passo 2).

Instalar o Jupyter:

bash
Copiar código
pip install jupyter
Passo 5: Instalar o IPython Kernel no Ambiente Virtual
Instalar o IPython kernel:

bash
Copiar código
pip install ipykernel
Adicionar o ambiente virtual como um kernel disponível no Jupyter:

bash
Copiar código
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
Passo 6: Iniciar o Jupyter Notebook
Iniciar o Jupyter Notebook:

bash
Copiar código
jupyter notebook
No navegador, crie ou abra um novo notebook.

Vá para o menu "Kernel" e selecione "Change kernel".

Escolha "Python (venv)" da lista de kernels disponíveis.

Finalização
Agora, seu notebook estará usando o ambiente venv configurado. Todas as bibliotecas instaladas nesse ambiente estarão disponíveis para uso no Jupyter Notebook.

Desativar o Ambiente Virtual
Quando terminar de usar o ambiente virtual, você pode desativá-lo com:

bash
Copiar código
deactivate
Isso retorna o prompt do terminal ao estado original.
