# Como usar em localhost

1. Abra um terminal na raiz do projeto e digite **`npm run back`**
2. Abra outro termnial, também na raiz do projeto, e execute **`npm run front`**
3. Acesse http://localhost:3000 para ver funcionando. Se tudo estiver certo, aparecerá *"Hello, Flask!"*

## Executar apenas Flask (backend)
Alternativamente, você pode querer executar apenas o backend. Para isso, siga estes passos:

1. Abra um terminal na raiz do projeto e execute **`cd backend`**
2. Após isso, ative o ambiente virtual, usando: **`. venv/bin/activate`**
3. E por último, execute **`flask run`**

Agora o Flask estará em execução na porta 5000.

## Executar apenas React (frontend)
Alternativamente, você pode querer executar apenas a aplicação React (frontend). Para isso, siga estes passos:

1. Abra um terminal na raiz do projeto e execute **`cd frontend`**
2. Execute **`npm start`**

Agora o React estará em execução na porta 3000.

<br/>

**ATENÇÃO!**
<br/>
Certifique-se de ter todas as dependências instaladas.