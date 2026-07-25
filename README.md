# venv
O venv é a ferramenta nativa do Python para criar ambientes virtuais isolados. Ele garante que as bibliotecas e dependências de um projeto não entrem em conflito com as de outros projetos ou com o sistema operacional.

```python
python -m venv .venv
```

## Ativar o venv

### Power Shell
```
.venv\Scripts\Activate.ps1
```

### Windows (CMD - Prompt de Comando)
```
.venv\Scripts\activate.bat
```

## Usar o ambiente isolado
### Instalar Pacotes
```python
pip install streamlit g4f
```

### Salvar a lista de dependências (para compartilhar o projeto)
```python
pip freeze > requirements.txt
```
### Instalar dependências a partir de um arquivo requirements.txt:
```python
pip install -r requirements.txt
``` 

## Desativar o Ambiente Virtual
Quando terminar de trabalhar no projeto e quiser voltar ao ambiente global do Python, basta executar:

```python
deactivate
``` 

# Git 
Antes de crair qualquer entrega (commit), defina o que NÃO deve ir para o GitHub (como a pasta .venv, arquivos de configuração local e senhas).

- Crie um arquivo chamado `.gitignore` na raiza do projeto.
- Adicione os caminhos que devem ser ignorados. Exemplo para este projeto Python:
```git
.venv/
__pycache__/
.env
*.pyc
.vscode/
```
- Inicialize o Git e conecte ao GitHub: 
```git
git init
git branch -M main
git remote add origin https://github.com/usuario/nome-do-repositorio.git
```

## Padrão de Entregas (Conventional Commits)
```
feat: Nova funcionalidade (feat: adiciona a criação de registros)
```
```
fix: Correção de bug (fix: corrige erro de cálculo no carrinho)
```
```
docs: Alterações na documentação (docs: atualiza o README)
```
```
style: Formatação, ponto e vírgula, sem alteração de código
```
```
refactor: Refatoração de código sem alterar regra de negócio
```
```
test: Adição ou ajuste de testes
```
Regra de Ouro: Faça commits pequenos e atômicos. Um commit deve resolver uma única coisa.

## O Fluxo de Trabalho com Branches (Ramos)

Nunca desenvolva diretamente na branch main. A main deve conter apenas código estável e pronto para produção.

- Passo 1: Crie uma nova branch para cada tarefa
```
git switch -c feature/criar-faq
```

- Passo 2: Faça o trabalho, adicione os arquivos e comite
```
git status                     # Verifique o que foi alterado
git add .                      # Prepara as alterações
git commit -m "feat: cria tela de login"
```

- Passo 3: Envie a branch para o GitHub
```
git push -u origin feature/criar-faq
```

- Passo 4. O Ciclo do Pull Request (PR)
Depois de enviar a sua branch para o GitHub:

1. Acesse o seu repositório no GitHub.
2. Clique em Compare & pull request.
3. Escreva uma breve descrição do que foi feito.
4. Se trabalhar em equipe, peça a revisão de um colega (Code Review).
5. Clique em Merge pull request para unir as alterações com a main.
6. Após o merge, exclua a branch secundária no GitHub.

- 5. Mantendo seu Ambiente Local Atualizado

Sempre que voltar a trabalhar no projeto ou finalizar uma tarefa, sincronize sua máquina local:
```
# Volte para a main
git switch main

# Baixe as atualizações do GitHub
git pull origin main

# Delete a branch antiga localmente se não for mais usá-la
git branch -d feature/login-usuario
```

# API Key

1. acesse: <https://console.groq.com>
2. Clique no ícone 🔑 (Get API Key )
3. Crie uma API Key com o nome de Chatbot SENAI
4. Na Raiz do projeto, crie:
```
faq/
├── app_faq.py
└── .streamlit/
    └── secrets.toml
```
4.1. Guardar a chave no secrets.toml
```
GEMINI_API_KEY = "sua_chave_aqui_cole_o_codigo"
GROQ_API_KEY = "gsk_sua_chave_groq_aqui"
```
4.2. 📌 Atenção: Adicionar o secrets dentro do .gitignore



