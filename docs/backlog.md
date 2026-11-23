# Backlog — Big Hangus Estoque

Escopo funcional: **um CRUD — Ingredientes (estoque)**, conforme [RF02](doc-visao.md) e [UC02](doc-modelos.md).

**Legenda de repositório:** `[BE]` backend · `[FE]` frontend · `[GERAL]` aplica-se a ambos ou à documentação.
**Tamanho:** P (até 2h) · M (meio dia) · G (um dia ou mais).

---

## 1. Backlog do produto

As atividades descritas na disciplina, organizadas em itens priorizados.

| ID   | Item do backlog                                                                  | Prioridade | Sprint |
|------|----------------------------------------------------------------------------------|------------|--------|
| PB01 | Criar os repositórios do projeto no GitHub                                       | Alta       | 1      |
| PB02 | Definir a tecnologia e registrá-la no README de cada repositório                 | Alta       | 1      |
| PB03 | Criar o diretório `docs` no repositório                                          | Alta       | 1      |
| PB04 | Elaborar o documento de visão (`doc-visao.md`)                                   | Alta       | 1      |
| PB05 | Elaborar o documento de modelos (`doc-modelos.md`)                               | Alta       | 1      |
| PB06 | Preparar o ambiente de desenvolvimento (backend, Docker, banco e frontend base)  | Alta       | 1      |
| PB07 | Implementar o backend do CRUD de ingredientes                                    | Alta       | 2      |
| PB08 | Implementar o frontend do CRUD de ingredientes                                   | Alta       | 2      |
| PB09 | Testar, documentar a execução e preparar a apresentação                          | Média      | 2      |
| PB10 | (Opcional) Proteger o CRUD com autenticação do gestor — RNF05                    | Baixa      | 2 (se houver tempo) |

**Fora do escopo desta entrega:** produtos (RF01), pedidos (RF03), comanda (RF04), controle automático de estoque (RF05) e alertas de baixa (RF06).

---

## 2. Sprint 1 — Fundação e documentação

**Objetivo da sprint:** deixar repositórios, documentação e ambiente de desenvolvimento prontos, de modo que a Sprint 2 se concentre apenas na implementação do CRUD.

**Entregáveis:** dois repositórios com README, `docs/` com visão e modelos, backend subindo com Docker + PostgreSQL, frontend base em execução.

### Issues da Sprint 1

#### Issue #1 — [GERAL] Criar repositório do backend no GitHub
**Labels:** `setup`, `sprint-1` · **Tamanho:** P · **Item:** PB01

**Descrição:** criar o repositório `big-hangus-backend`, com `.gitignore` para Python e licença, e adicionar todos os integrantes como colaboradores.

**Critérios de aceite:**
- [ ] Repositório criado e acessível por toda a equipe
- [ ] `.gitignore` de Python configurado
- [ ] Branch `main` protegida (alterações via pull request)

---

#### Issue #2 — [GERAL] Criar repositório do frontend no GitHub
**Labels:** `setup`, `sprint-1` · **Tamanho:** P · **Item:** PB01

**Descrição:** criar o repositório `big-hangus-frontend`, com `.gitignore` para Node e licença, e adicionar todos os integrantes como colaboradores.

**Critérios de aceite:**
- [ ] Repositório criado e acessível por toda a equipe
- [ ] `.gitignore` de Node configurado
- [ ] Branch `main` protegida

---

#### Issue #3 — [GERAL] Configurar quadro do projeto, labels e milestones
**Labels:** `setup`, `sprint-1` · **Tamanho:** P · **Item:** PB01

**Descrição:** criar um GitHub Project (quadro Kanban) com as colunas *Backlog*, *Em andamento*, *Em revisão* e *Concluído*; criar as milestones *Sprint 1* e *Sprint 2*; criar as labels `setup`, `docs`, `backend`, `frontend`, `feature`, `test`, `sprint-1`, `sprint-2`.

**Critérios de aceite:**
- [ ] Quadro criado e ligado aos dois repositórios
- [ ] Milestones e labels criadas
- [ ] Combinado o fluxo: uma branch por issue e pull request revisado por outro integrante

---

#### Issue #4 — [BE] Escrever o README do backend com a tecnologia do projeto
**Labels:** `docs`, `backend`, `sprint-1` · **Tamanho:** P · **Item:** PB02

**Descrição:** descrever no `README.md` o objetivo do projeto e a stack: Python, FastAPI, Docker, PostgreSQL. Incluir um espaço para as instruções de execução, a serem completadas na Sprint 2.

**Critérios de aceite:**
- [ ] README com nome, objetivo e integrantes
- [ ] Seção "Tecnologias" com Python, FastAPI, Docker e PostgreSQL
- [ ] Link para o repositório do frontend
- [ ] Link para os documentos em `docs/`

---

#### Issue #5 — [FE] Escrever o README do frontend com a tecnologia do projeto
**Labels:** `docs`, `frontend`, `sprint-1` · **Tamanho:** P · **Item:** PB02

**Descrição:** descrever no `README.md` o objetivo e a stack do frontend (Vue.js), com link para o repositório do backend.

**Critérios de aceite:**
- [ ] README com nome, objetivo e integrantes
- [ ] Seção "Tecnologias" com Vue.js
- [ ] Link para o repositório do backend

---

#### Issue #6 — [BE] Criar o diretório `docs` no repositório
**Labels:** `docs`, `backend`, `sprint-1` · **Tamanho:** P · **Item:** PB03

**Descrição:** criar o diretório `docs/` no repositório de backend para guardar a documentação do projeto.

**Critérios de aceite:**
- [ ] Diretório `docs/` versionado na `main`
- [ ] README aponta para `docs/`

---

#### Issue #7 — [BE] Adicionar o documento de visão (`docs/doc-visao.md`)
**Labels:** `docs`, `backend`, `sprint-1` · **Tamanho:** M · **Item:** PB04

**Descrição:** elaborar o documento de visão com base no projeto de OSM e nos conceitos de Engenharia de Software I, seguindo o modelo da disciplina: introdução, posicionamento, partes interessadas, visão geral do produto, recursos, restrições e requisitos de qualidade.

**Critérios de aceite:**
- [ ] Arquivo `docs/doc-visao.md` na `main`
- [ ] Todos os requisitos (RF01–RF06 e RNF01–RNF06) do projeto de OSM presentes
- [ ] Escopo da entrega (CRUD de ingredientes) explicitado
- [ ] Revisado por pelo menos dois integrantes

---

#### Issue #8 — [BE] Adicionar o documento de modelos (`docs/doc-modelos.md`)
**Labels:** `docs`, `backend`, `sprint-1` · **Tamanho:** G · **Item:** PB05

**Descrição:** elaborar o documento de modelos com os conceitos de Banco de Dados e Engenharia de Software I: casos de uso (diagrama e especificação do UC02), modelo de classes, modelo entidade-relacionamento, modelo relacional com restrições, modelo da API e diagrama de sequência.

**Critérios de aceite:**
- [ ] Arquivo `docs/doc-modelos.md` na `main`
- [ ] Diagramas Mermaid renderizando corretamente no GitHub
- [ ] Modelo relacional consistente com o modelo ER e o de classes
- [ ] Especificação do caso de uso Manter ingredientes com cenários principais e alternativos
- [ ] Revisado por pelo menos dois integrantes

---

#### Issue #9 — [BE] Estruturar o projeto FastAPI
**Labels:** `setup`, `backend`, `sprint-1` · **Tamanho:** M · **Item:** PB06

**Descrição:** criar a estrutura inicial da API com separação em camadas (por exemplo: `routers`, `schemas`, `models`, `services`, `core`), arquivo `requirements.txt` (ou `pyproject.toml`) e uma rota `GET /health` retornando `{"status": "ok"}`.

**Critérios de aceite:**
- [ ] Aplicação sobe localmente com `uvicorn`
- [ ] `GET /health` responde `200`
- [ ] Documentação automática acessível em `/docs`
- [ ] Estrutura de pastas descrita no README

---

#### Issue #10 — [BE] Criar `Dockerfile` e `docker-compose.yml` com PostgreSQL
**Labels:** `setup`, `backend`, `sprint-1` · **Tamanho:** M · **Item:** PB06

**Descrição:** containerizar a API e o banco. O `docker compose up` deve subir a API e o PostgreSQL, com variáveis de ambiente em arquivo `.env` (com um `.env.example` versionado) e volume para persistência dos dados.

**Critérios de aceite:**
- [ ] `docker compose up` sobe API e banco sem passos manuais
- [ ] Credenciais fora do código, com `.env.example` no repositório
- [ ] Dados do banco persistem após reiniciar os containers
- [ ] Instruções básicas no README

---

#### Issue #11 — [BE] Configurar acesso ao banco e migração da tabela `ingredientes`
**Labels:** `setup`, `backend`, `sprint-1` · **Tamanho:** M · **Item:** PB06

**Descrição:** configurar o acesso ao PostgreSQL (SQLAlchemy) e as migrações (Alembic). Criar a primeira migração com a tabela `ingredientes`, conforme o modelo relacional do `doc-modelos.md`, incluindo as restrições (`nome` único, quantidades e preço não negativos, unidade em `kg` ou `litros`).

**Critérios de aceite:**
- [ ] Conexão com o banco configurada via variáveis de ambiente
- [ ] Migração aplicada com sucesso nos containers
- [ ] Tabela `ingredientes` criada com as colunas e restrições do modelo
- [ ] Comando para aplicar migrações documentado

---

#### Issue #12 — [FE] Criar o projeto base em Vue.js
**Labels:** `setup`, `frontend`, `sprint-1` · **Tamanho:** M · **Item:** PB06

**Descrição:** criar o projeto Vue.js (com Vite), configurar o roteador, um cliente HTTP (por exemplo, axios) com a URL da API em variável de ambiente, e um layout base com cabeçalho e navegação (item "Ingredientes").

**Critérios de aceite:**
- [ ] Projeto roda localmente com `npm run dev`
- [ ] Página inicial e rota `/ingredientes` (vazia) funcionando
- [ ] URL da API configurável por variável de ambiente
- [ ] Instruções de execução no README

---

### Revisão e retrospectiva da Sprint 1

**Revisão (demonstração):** mostrar os dois repositórios, os documentos em `docs/`, a API respondendo em `/health` via Docker e o frontend base rodando.

**Checklist de revisão**
- [ ] Todas as issues da Sprint 1 fechadas ou justificadas
- [ ] Documentos de visão e modelos na `main` do backend
- [ ] Ambiente sobe do zero seguindo apenas o README

**Retrospectiva**

| O que foi bem | O que pode melhorar | O que vamos fazer na próxima sprint |
|---------------|---------------------|--------------------------------------|
| _(preencher)_ | _(preencher)_       | _(preencher)_                        |

---

## 3. Sprint 2 — Implementação do CRUD de ingredientes

**Objetivo da sprint:** entregar o CRUD completo de ingredientes, do banco à interface, funcionando de ponta a ponta.

**Entregáveis:** API com cinco endpoints, testes automatizados, telas de listagem, cadastro/edição e exclusão, README com instruções de execução.

### Issues da Sprint 2

#### Issue #13 — [BE] Criar modelo ORM e schemas do ingrediente
**Labels:** `feature`, `backend`, `sprint-2` · **Tamanho:** M · **Item:** PB07

**Descrição:** criar o modelo SQLAlchemy `Ingrediente` e os schemas Pydantic (`IngredienteCreate`, `IngredienteUpdate`, `IngredienteResponse`), aplicando as regras RN01–RN04: nome obrigatório, preço e quantidades não negativas, unidade `kg` ou `litros`.

**Critérios de aceite:**
- [ ] Modelo mapeado para a tabela `ingredientes`
- [ ] Validações rejeitam valores negativos e unidade inválida
- [ ] Resposta inclui o campo calculado `em_baixa` (quantidade disponível menor que a mínima)

---

#### Issue #14 — [BE] Endpoint de inclusão: `POST /ingredientes`
**Labels:** `feature`, `backend`, `sprint-2` · **Tamanho:** M · **Item:** PB07

**Descrição:** criar o endpoint que cadastra um ingrediente.

**Critérios de aceite:**
- [ ] Retorna `201 Created` com o ingrediente criado
- [ ] Retorna `422` para dados inválidos
- [ ] Retorna `409` se já existir ingrediente com o mesmo nome
- [ ] Responde em até 4 segundos (RNF01)

---

#### Issue #15 — [BE] Endpoint de listagem: `GET /ingredientes`
**Labels:** `feature`, `backend`, `sprint-2` · **Tamanho:** M · **Item:** PB07

**Descrição:** criar o endpoint que lista ingredientes, com filtro opcional por nome (`nome`) e por situação de baixa (`em_baixa=true`).

**Critérios de aceite:**
- [ ] Retorna `200` com a lista (vazia quando não há registros)
- [ ] Filtro por nome busca por trecho, sem diferenciar maiúsculas de minúsculas
- [ ] Filtro `em_baixa` retorna apenas ingredientes abaixo da quantidade mínima

---

#### Issue #16 — [BE] Endpoint de consulta: `GET /ingredientes/{id}`
**Labels:** `feature`, `backend`, `sprint-2` · **Tamanho:** P · **Item:** PB07

**Descrição:** criar o endpoint que retorna um ingrediente pelo identificador.

**Critérios de aceite:**
- [ ] Retorna `200` com os dados do ingrediente
- [ ] Retorna `404` com mensagem clara se não existir

---

#### Issue #17 — [BE] Endpoint de alteração: `PUT /ingredientes/{id}`
**Labels:** `feature`, `backend`, `sprint-2` · **Tamanho:** M · **Item:** PB07

**Descrição:** criar o endpoint que altera os dados de um ingrediente.

**Critérios de aceite:**
- [ ] Retorna `200` com o ingrediente atualizado
- [ ] Retorna `404` se não existir
- [ ] Retorna `409` se o novo nome já pertencer a outro ingrediente
- [ ] Retorna `422` para dados inválidos

---

#### Issue #18 — [BE] Endpoint de exclusão: `DELETE /ingredientes/{id}`
**Labels:** `feature`, `backend`, `sprint-2` · **Tamanho:** P · **Item:** PB07

**Descrição:** criar o endpoint que remove um ingrediente.

**Critérios de aceite:**
- [ ] Retorna `204 No Content` ao excluir
- [ ] Retorna `404` se não existir
- [ ] Ingrediente deixa de aparecer na listagem

---

#### Issue #19 — [BE] Testes automatizados do CRUD
**Labels:** `test`, `backend`, `sprint-2` · **Tamanho:** G · **Item:** PB07, PB09

**Descrição:** escrever testes com `pytest` e o cliente de testes do FastAPI cobrindo os cinco endpoints, incluindo os caminhos de erro (`404`, `409`, `422`).

**Critérios de aceite:**
- [ ] Teste de sucesso para cada operação
- [ ] Testes para nome duplicado, dado inválido e item inexistente
- [ ] Testes executam com um único comando documentado no README

---

#### Issue #20 — [BE] Configurar CORS e revisar a documentação OpenAPI
**Labels:** `backend`, `sprint-2` · **Tamanho:** P · **Item:** PB07

**Descrição:** liberar a origem do frontend via CORS e revisar títulos, descrições e exemplos na documentação gerada em `/docs`.

**Critérios de aceite:**
- [ ] Frontend consegue chamar a API a partir do navegador
- [ ] Endpoints com descrição e exemplos de corpo na documentação

---

#### Issue #21 — [FE] Criar o serviço de acesso à API de ingredientes
**Labels:** `feature`, `frontend`, `sprint-2` · **Tamanho:** P · **Item:** PB08

**Descrição:** criar um módulo que encapsula as chamadas HTTP (listar, consultar, criar, alterar, excluir) e padroniza o tratamento de erros da API.

**Critérios de aceite:**
- [ ] Cinco funções, uma por operação do CRUD
- [ ] Erros `404`, `409` e `422` chegam à interface com mensagem legível

---

#### Issue #22 — [FE] Tela de listagem de ingredientes
**Labels:** `feature`, `frontend`, `sprint-2` · **Tamanho:** M · **Item:** PB08

**Descrição:** criar a página `/ingredientes` com tabela (nome, quantidade, unidade, quantidade mínima, validade), campo de busca por nome e destaque visual para ingredientes em baixa.

**Critérios de aceite:**
- [ ] Lista carregada da API
- [ ] Busca por nome funcionando
- [ ] Ingredientes em baixa destacados
- [ ] Mensagem de estado vazio quando não houver registros
- [ ] Botões de editar, excluir e "Novo ingrediente"

---

#### Issue #23 — [FE] Formulário de cadastro e edição de ingredientes
**Labels:** `feature`, `frontend`, `sprint-2` · **Tamanho:** G · **Item:** PB08

**Descrição:** criar o formulário reutilizável para incluir e alterar ingredientes, com os campos nome, preço, data de validade, quantidade disponível, unidade de medida e quantidade mínima.

**Critérios de aceite:**
- [ ] Mesmo formulário serve para cadastro (`/ingredientes/novo`) e edição (`/ingredientes/:id`)
- [ ] Validação no cliente dos campos obrigatórios e de valores negativos
- [ ] Mensagens de erro da API exibidas junto aos campos (incluindo nome duplicado)
- [ ] Após salvar, retorna à listagem com confirmação

---

#### Issue #24 — [FE] Exclusão de ingrediente com confirmação
**Labels:** `feature`, `frontend`, `sprint-2` · **Tamanho:** P · **Item:** PB08

**Descrição:** adicionar diálogo de confirmação antes de excluir um ingrediente (cenário A4 do UC02).

**Critérios de aceite:**
- [ ] Diálogo de confirmação exibido antes da exclusão
- [ ] Cancelar mantém o registro
- [ ] Confirmar remove o item e atualiza a lista

---

#### Issue #25 — [GERAL] Teste de ponta a ponta e atualização dos READMEs
**Labels:** `test`, `docs`, `sprint-2` · **Tamanho:** M · **Item:** PB09

**Descrição:** executar manualmente os cenários do UC02 (principais e alternativos) com frontend e backend integrados; completar os READMEs com instruções de instalação e execução dos dois projetos.

**Critérios de aceite:**
- [ ] Todos os cenários do UC02 verificados e registrados
- [ ] Um integrante que não escreveu o README consegue subir o sistema só com ele
- [ ] Docs revisados caso algo tenha mudado em relação ao `doc-modelos.md`

---

#### Issue #26 — [BE] _(Opcional)_ Autenticação do gestor nas rotas de escrita
**Labels:** `feature`, `backend`, `sprint-2`, `opcional` · **Tamanho:** G · **Item:** PB10

**Descrição:** proteger os endpoints de inclusão, alteração e exclusão para que somente o gestor autenticado possa usá-los (RNF05). Só deve ser iniciada se as demais issues da sprint estiverem concluídas.

**Critérios de aceite:**
- [ ] Login do gestor com token
- [ ] Rotas de escrita retornam `401`/`403` sem autenticação válida
- [ ] Consulta e listagem mantêm o comportamento definido na sprint

---

### Revisão e retrospectiva da Sprint 2

**Revisão (demonstração):** com backend e frontend rodando, executar o ciclo completo — cadastrar, listar, filtrar, editar e excluir um ingrediente — e mostrar os testes passando.

**Checklist de revisão**
- [ ] Todas as issues da Sprint 2 (exceto a opcional) fechadas ou justificadas
- [ ] CRUD funcionando de ponta a ponta
- [ ] Testes automatizados passando
- [ ] READMEs e `docs/` atualizados

**Retrospectiva**

| O que foi bem | O que pode melhorar | Ações para os próximos projetos |
|---------------|---------------------|----------------------------------|
| _(preencher)_ | _(preencher)_       | _(preencher)_                    |
