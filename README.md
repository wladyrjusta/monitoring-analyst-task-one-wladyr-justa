<h1>Sales Monitoring App</h1>

<p>Este é um aplicativo Python Flask que gera gráficos a partir de dados do banco de dados MySQL e os exibe em páginas HTML. O aplicativo também é configurado para ser executado em um contêiner Docker.</p>

 <h2>Pré-requisitos</h2>

  <p>Certifique-se de ter o seguinte instalado no seu sistema:</p>
   <ul>
     <li>Docker: <a href="https://docs.docker.com/get-docker/">Instalação do Docker</a></li>
      <li>Python 3.x: <a href="https://www.python.org/downloads/">Instalação do Python</a></li>
  </ul>

  <li>Clone o repositório do projeto:</li>
 </ol>

 <pre><code>git clone git@github.com:wladyrjusta/monitoring-analyst-task-one-wladyr-justa.git</code></pre>

 <ol start="2">
    <li>Navegue até o diretório do projeto:</li>
 </ol>
 <pre><code>cd monitoring-analyst-task-one-wladyr-justa</code></pre>

<h2>Criando um Ambiente Virtual (Recomendado)</h2>

<p>Recomendamos que você crie e ative um ambiente virtual Python antes de instalar as dependências. Isso ajuda a isolar as dependências do projeto e evita conflitos com outras versões de pacotes Python instalados globalmente no seu sistema. Siga estas etapas:</p>
<ol start="1">

 <ol>
    <li>Crie um novo ambiente virtual:</li>
 </ol>

 <pre><code>python -m venv venv</code></pre>
 <p>OU</p>
  <pre><code>python3 -m venv venv</code></pre>

 <ol start="2">
   <li>Ative o ambiente virtual (no Windows):</li>
 </ol>

<pre><code>venv\Scripts\activate</code></pre>

<p>Ou ative o ambiente virtual (no macOS e Linux):</p>

<pre><code>source venv/bin/activate</code></pre>

<p>Depois de ativar o ambiente virtual, seu terminal deve mostrar o nome do ambiente entre parênteses, indicando que está ativo.</p>

<h2>Configuração do Contêiner Docker</h2>

<p>Este aplicativo usa um contêiner Docker para executar um servidor MySQL. Siga estas etapas para configurar o contêiner:</p>

 <ol start="3">
  <li>Crie o contêiner Docker com o seguinte comando:</li>
 </ol>

<pre><code>docker build -t sales-monitoring-app .</code></pre>

 <ol start="4">
  <li>Execute o contêiner Docker:</li>
 </ol>

 <pre><code>docker run -d -p 3306:3306 --name sales-monitoring-container sales-monitoring-app</code></pre>

 <p>Isso iniciará o servidor MySQL em um contêiner Docker. O servidor MySQL será acessível na porta 3306.</p>

 <h2>Executando o Aplicativo</h2>

 <ol start="1">
   <li>Instale as dependências Python:</li>
 </ol>

<pre><code>pip install -r requirements.txt</code></pre>

<ol start="2">
 <li>Inicie o aplicativo Flask:</li>
</ol>

<pre><code>python app.py</code></pre>

<p>O aplicativo estará acessível em:</p>

<ul>
 <li>Página com gráficos da "checkout_1": <a href="http://localhost:5000/generate_graphic/checkout_1">http://localhost:5000/generate_graphic/checkout_1</a></li>
 <li>Página com gráficos da "checkout_2": <a href="http://localhost:5000/generate_graphic/checkout_2">http://localhost:5000/generate_graphic/checkout_2</a></li>
</ul>

<h2>Explorando os Dados</h2>

<p>Com dados hipotéticos de vendas em caixas registradoras, nosso objetivo é entender se há algum comportamento anômalo.</p>

<p>Vamos analisar os dados fornecidos e apresentar nossas conclusões. Além dos dados da planilha, faremos consultas SQL e criaremos gráficos a partir delas, tentando explicar o comportamento anômalo encontrado.</p>

<p>No arquivo CSV, temos o número de vendas de caixas registradoras por hora, comparando as vendas por hora de hoje, ontem e a média de outros dias. Com isso, podemos analisar o comportamento de hoje e compará-lo com outros dias.</p>