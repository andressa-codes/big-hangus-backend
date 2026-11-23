# Documento de Modelos — Big Hangus Estoque

| Versão | Data       | Descrição                   | Autores                                                                                                               |
|--------|------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1.0    | 16/11/2026 | Versão inicial do documento | Andressa Carla da Silva, Elisson da Silva Tavares, Gabriel Victor de Souza Fernandes, Vanesca Héllen dos Santos Silva |

Este documento reúne os modelos do sistema: casos de uso, modelo de classes, modelo entidade-relacionamento e modelo relacional. Os diagramas usam Mermaid e são renderizados diretamente no GitHub. Os requisitos estão descritos no [Documento de Visão](doc-visao.md).

> **Escopo da implementação:** os modelos cobrem o sistema completo, mas o CRUD implementado nesta etapa é o de **Ingredientes (estoque)**, ligado ao caso de uso **UC02 — Manter ingredientes**.

## 1. Modelo de casos de uso

### 1.1 Atores

| Ator        | Descrição                                                              |
|-------------|------------------------------------------------------------------------|
| Gestor      | Usuário administrador: produtos, ingredientes, entradas e alertas      |
| Funcionário | Realiza, altera e cancela pedidos                                      |

### 1.2 Diagrama de casos de uso

```mermaid
flowchart LR
    G([Gestor])
    F([Funcionário])

    subgraph SISTEMA["Sistema de controle do estoque"]
        UC01((UC01<br/>Manter produtos))
        UC02((UC02<br/>Manter ingredientes))
        UC03((UC03<br/>Registrar entrada))
        UC04((UC04<br/>Verificar estoque baixo))
        UC05((UC05<br/>Realizar pedido))
        UC06((UC06<br/>Alterar pedido))
        UC07((UC07<br/>Cancelar pedido))
        UC08((UC08<br/>Verificar disponibilidade))
        UC09((UC09<br/>Calcular total))
        UC10((UC10<br/>Atualizar estoque))
        UC11((UC11<br/>Criar comanda))
    end

    G --- UC01
    G --- UC02
    G --- UC03
    G --- UC04
    F --- UC05
    F --- UC06
    F --- UC07

    UC05 -.->|include| UC08
    UC05 -.->|include| UC10
    UC06 -.->|include| UC08
    UC07 -.->|include| UC10
    UC08 -.->|include| UC09
    UC11 -.->|extend| UC10
```

### 1.3 Lista de casos de uso

| ID   | Caso de uso                   | Ator        | Requisito | Implementado agora |
|------|-------------------------------|-------------|-----------|--------------------|
| UC01 | Manter produtos               | Gestor      | RF01      | Não                |
| UC02 | **Manter ingredientes**       | Gestor      | RF02      | **Sim**            |
| UC03 | Registrar entrada de estoque  | Gestor      | RF02      | Não                |
| UC04 | Verificar estoque baixo       | Gestor      | RF06      | Não                |
| UC05 | Realizar pedido               | Funcionário | RF03, RF05 | Não               |
| UC06 | Alterar pedido                | Funcionário | RF03      | Não                |
| UC07 | Cancelar pedido               | Funcionário | RF03, RF05 | Não               |
| UC08 | Verificar disponibilidade     | Sistema     | RF05      | Não                |
| UC09 | Calcular total                | Sistema     | RF03      | Não                |
| UC10 | Atualizar estoque             | Sistema     | RF05      | Não                |
| UC11 | Criar comanda                 | Sistema     | RF04      | Não                |

### 1.4 Especificação do caso de uso UC02 — Manter ingredientes

| Item                      | Descrição                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| Nome                      | Manter ingredientes                                                                                        |
| Ator                      | Gestor                                                                                                     |
| Resumo                    | Gestão (inclusão, alteração, exclusão e consulta) dos ingredientes do estoque                              |
| Pré-condições             | Gestor com acesso ao sistema (perfil administrador, conforme RNF05, quando a autenticação for implementada) |
| Pós-condições             | As informações do ingrediente são armazenadas, atualizadas ou removidas no sistema                         |
| Requisitos não funcionais | RNF01 (desempenho), RNF05 (controle administrativo)                                                        |

**Regras de negócio**

| ID   | Regra                                                                                  |
|------|----------------------------------------------------------------------------------------|
| RN01 | O nome do ingrediente é obrigatório e único                                            |
| RN02 | A quantidade disponível e a quantidade mínima não podem ser negativas                  |
| RN03 | O preço deve ser maior ou igual a zero                                                 |
| RN04 | A unidade de medida deve ser `kg` ou `litros`                                          |
| RN05 | Um ingrediente é considerado em baixa quando a quantidade disponível está abaixo da mínima |

**Cenário principal — Inclusão**

1. O gestor informa nome, preço, data de validade, quantidade disponível, unidade de medida e quantidade mínima.
2. O sistema valida os dados.
3. O sistema salva o ingrediente e confirma a inclusão.

**Cenário principal — Consulta**

1. O gestor acessa a lista de ingredientes e, se quiser, filtra por nome.
2. O sistema exibe os ingredientes, destacando os que estão em baixa.
3. O gestor seleciona um ingrediente e o sistema exibe seus dados completos.

**Cenário principal — Alteração**

1. O gestor seleciona o ingrediente.
2. O gestor informa os novos dados e confirma.
3. O sistema valida e armazena as novas informações.

**Cenário principal — Exclusão**

1. O gestor seleciona o ingrediente e escolhe remover.
2. O sistema pede confirmação.
3. O gestor confirma e o sistema remove o registro.

**Cenários alternativos**

| ID  | Situação                                  | Resposta do sistema                                                      |
|-----|-------------------------------------------|--------------------------------------------------------------------------|
| A1  | Dado inválido ou obrigatório ausente      | Exibe mensagem indicando qual dado deve ser corrigido                    |
| A2  | Nome já cadastrado                        | Informa que já existe ingrediente com esse nome                          |
| A3  | Ingrediente não existe (consulta, alteração ou exclusão) | Exibe mensagem de item inexistente e volta à tela anterior |
| A4  | Gestor cancela a confirmação da exclusão  | Mantém o registro e volta à lista                                        |

## 2. Modelo de classes

```mermaid
classDiagram
    class Ingrediente {
        +int id
        +String nome
        +Decimal preco
        +Date dataValidade
        +Decimal quantidadeDisponivel
        +UnidadeMedida unidadeMedida
        +Decimal quantidadeMinima
        +estaEmBaixa() bool
    }

    class Produto {
        +int id
        +String nome
        +String descricao
        +Decimal preco
        +String categoria
        +StatusProduto status
    }

    class ItemReceita {
        +Decimal quantidade
    }

    class Pedido {
        +int id
        +int numeroMesa
        +Decimal valorTotal
        +DateTime dataHora
        +StatusPedido status
        +FormaPagamento formaPagamento
        +calcularTotal() Decimal
    }

    class ItemPedido {
        +int quantidade
        +Decimal precoUnitario
    }

    class Usuario {
        +int id
        +String nome
        +Perfil perfil
    }

    class UnidadeMedida {
        <<enumeration>>
        KG
        LITRO
    }

    class StatusProduto {
        <<enumeration>>
        ATIVO
        INATIVO
    }

    class StatusPedido {
        <<enumeration>>
        AGUARDANDO_PREPARO
        EM_PREPARO
        FINALIZADO
        CANCELADO
    }

    class Perfil {
        <<enumeration>>
        GESTOR
        FUNCIONARIO
    }

    Produto "1" --> "1..*" ItemReceita : é composto por
    Ingrediente "1" --> "0..*" ItemReceita : é usado em
    Pedido "1" *-- "1..*" ItemPedido : contém
    Produto "1" --> "0..*" ItemPedido : é pedido em
    Usuario "1" --> "0..*" Pedido : registra
    Ingrediente --> UnidadeMedida
    Produto --> StatusProduto
    Pedido --> StatusPedido
    Usuario --> Perfil
```

> Estados do pedido: a alteração e o cancelamento só são permitidos em `AGUARDANDO_PREPARO`, conforme a documentação do caso de uso de pedidos do projeto de OSM.

## 3. Modelo entidade-relacionamento

```mermaid
erDiagram
    INGREDIENTE ||--o{ ITEM_RECEITA : "compõe"
    PRODUTO ||--|{ ITEM_RECEITA : "possui"
    PEDIDO ||--|{ ITEM_PEDIDO : "contém"
    PRODUTO ||--o{ ITEM_PEDIDO : "é pedido em"
    USUARIO ||--o{ PEDIDO : "registra"

    INGREDIENTE {
        int id PK
        string nome UK
        decimal preco
        date data_validade
        decimal quantidade_disponivel
        string unidade_medida
        decimal quantidade_minima
    }
    PRODUTO {
        int id PK
        string nome
        string descricao
        decimal preco
        string categoria
        string status
    }
    ITEM_RECEITA {
        int produto_id PK, FK
        int ingrediente_id PK, FK
        decimal quantidade
    }
    PEDIDO {
        int id PK
        int numero_mesa
        decimal valor_total
        datetime data_hora
        string status
        string forma_pagamento
        int usuario_id FK
    }
    ITEM_PEDIDO {
        int pedido_id PK, FK
        int produto_id PK, FK
        int quantidade
        decimal preco_unitario
    }
    USUARIO {
        int id PK
        string nome
        string perfil
    }
```

## 4. Modelo relacional

```
INGREDIENTE (id PK, nome UK, preco, data_validade, quantidade_disponivel,
             unidade_medida, quantidade_minima)

PRODUTO (id PK, nome, descricao, preco, categoria, status)

ITEM_RECEITA (produto_id PK/FK -> PRODUTO.id,
              ingrediente_id PK/FK -> INGREDIENTE.id,
              quantidade)

USUARIO (id PK, nome, perfil)

PEDIDO (id PK, numero_mesa, valor_total, data_hora, status,
        forma_pagamento, usuario_id FK -> USUARIO.id)

ITEM_PEDIDO (pedido_id PK/FK -> PEDIDO.id,
             produto_id PK/FK -> PRODUTO.id,
             quantidade, preco_unitario)
```

### 4.1 Restrições de integridade

| Tabela       | Restrição                                                                        |
|--------------|----------------------------------------------------------------------------------|
| INGREDIENTE  | `nome` único e não nulo; `preco >= 0`; `quantidade_disponivel >= 0`; `quantidade_minima >= 0`; `unidade_medida IN ('kg', 'litros')` |
| PRODUTO      | `preco >= 0`; `status IN ('ativo', 'inativo')`                                   |
| ITEM_RECEITA | `quantidade > 0`; exclusão de produto remove sua receita (`ON DELETE CASCADE`)   |
| ITEM_RECEITA | exclusão de ingrediente é bloqueada se estiver em alguma receita (`ON DELETE RESTRICT`) |
| PEDIDO       | `status IN ('aguardando_preparo', 'em_preparo', 'finalizado', 'cancelado')`      |
| ITEM_PEDIDO  | `quantidade > 0`                                                                 |

### 4.2 Script SQL (apenas o necessário para o CRUD implementado)

```sql
CREATE TABLE ingrediente (
    id                    SERIAL PRIMARY KEY,
    nome                  VARCHAR(100)  NOT NULL UNIQUE,
    preco                 NUMERIC(10,2) NOT NULL CHECK (preco >= 0),
    data_validade         DATE,
    quantidade_disponivel NUMERIC(10,3) NOT NULL CHECK (quantidade_disponivel >= 0),
    unidade_medida        VARCHAR(10)   NOT NULL CHECK (unidade_medida IN ('kg', 'litros')),
    quantidade_minima     NUMERIC(10,3) NOT NULL CHECK (quantidade_minima >= 0)
);
```

## 5. Modelo da API do CRUD de ingredientes

| Operação  | Método   | Rota                    | Corpo         | Resposta de sucesso            | Erros                        |
|-----------|----------|-------------------------|---------------|--------------------------------|------------------------------|
| Incluir   | `POST`   | `/ingredientes`         | Ingrediente   | `201 Created` + ingrediente    | `409` nome duplicado, `422` dado inválido |
| Listar    | `GET`    | `/ingredientes`         | —             | `200 OK` + lista (filtro `nome`, `em_baixa`) | —              |
| Consultar | `GET`    | `/ingredientes/{id}`    | —             | `200 OK` + ingrediente         | `404` não encontrado         |
| Alterar   | `PUT`    | `/ingredientes/{id}`    | Ingrediente   | `200 OK` + ingrediente         | `404`, `409`, `422`          |
| Excluir   | `DELETE` | `/ingredientes/{id}`    | —             | `204 No Content`               | `404`, `409` se em uso       |

**Exemplo de corpo (JSON):**

```json
{
  "nome": "Queijo mussarela",
  "preco": 42.90,
  "data_validade": "2026-12-20",
  "quantidade_disponivel": 8.5,
  "unidade_medida": "kg",
  "quantidade_minima": 2
}
```

## 6. Diagrama de sequência — incluir ingrediente

```mermaid
sequenceDiagram
    actor G as Gestor
    participant FE as Frontend (Vue.js)
    participant API as Backend (FastAPI)
    participant DB as PostgreSQL

    G->>FE: Preenche o formulário e salva
    FE->>API: POST /ingredientes
    API->>API: Valida dados (RN01–RN04)
    alt dados inválidos
        API-->>FE: 422 Unprocessable Entity
        FE-->>G: Exibe campos a corrigir
    else nome já cadastrado
        API-->>FE: 409 Conflict
        FE-->>G: Informa nome duplicado
    else válido
        API->>DB: INSERT INTO ingrediente
        DB-->>API: registro criado
        API-->>FE: 201 Created
        FE-->>G: Confirma e atualiza a lista
    end
```
