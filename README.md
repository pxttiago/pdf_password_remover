# Removedor de Senha para arquivos PDF
<br>

### Introdução
O Removedor de Senha de PDF é uma aplicação simples que permite remover senhas de arquivos PDF. Desenvolvido em Python, o programa utiliza a biblioteca Tkinter para a interface gráfica e a biblioteca PyPDF2 para manipulação de arquivos PDF.
<br><br>

### Funcionalidades
Selecionar Arquivo PDF:
O usuário pode selecionar um arquivo PDF usando a interface gráfica.
A caixa de texto exibe o caminho do arquivo selecionado.

Inserir Senha:
O usuário insere a senha necessária para desbloquear o arquivo PDF.

Remover Senha:
Ao clicar no botão "Remover Senha", o programa tenta remover a senha do PDF.

Feedback ao Usuário:
O programa exibe mensagens de sucesso ou erro em pop-ups usando a biblioteca tkinter.messagebox.

Salvar Novo PDF:
Se a senha for removida com sucesso, o novo PDF sem senha é salvo na mesma pasta do arquivo original.
<br><br>

### Requisitos do Sistema
Python 3.x instalado.
Bibliotecas necessárias: Tkinter, PyPDF2.
<br><br>

### Instalação
Clone o repositório:
<pre>
git clone https://github.com/seu-usuario/seu-repositorio.git
</pre>

Instale as dependências:
<pre>
 pip install -r requirements.txt
</pre>
<br><br>

### Como Usar
Execute o script Python app.py:
<pre>
 python app.py
 </pre>

Selecione o arquivo PDF desejado.

Insira a senha do PDF.

Clique no botão "Remover Senha".

Aguarde o feedback do programa.
<br><br>

### Estrutura do Projeto
app.py: Script principal que contém a interface gráfica e a lógica do programa.
requirements.txt: Arquivo contendo as dependências do projeto.
<br><br>

### Observações
Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o programa.
Este projeto utiliza a biblioteca Tkinter para a interface gráfica e PyPDF2 para manipulação de arquivos PDF.
Mensagens informativas e de erro são exibidas em pop-ups para fornecer feedback ao usuário.
