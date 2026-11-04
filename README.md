# trendsIA P0 — Primeiro fluxo com LLM

Entrega de George Gomes para o projeto **P0** da residência trendsIA (Softex).

## Problema escolhido
_Uma pessoa que realiza [atividade] precisa transformar [entrada] em [saída], porque atualmente enfrenta [dificuldade]._

## Usuário ou público
_a preencher_

## Por que um LLM
_a preencher: por que uma regra fixa não resolve; o que o modelo faz que justifica seu uso_

## Como a solução funciona
Entrada textual pelo terminal → preparação da solicitação → chamada ao LLM pela API REST → tratamento da resposta → apresentação do resultado.

```
src/app/
├── __main__.py    ponto de entrada (python -m app)
├── entrada.py     captura e validação da entrada
├── config.py      carregamento da configuração e das credenciais (variáveis de ambiente)
├── solicitacao.py preparação da solicitação (prompt e parâmetros)
├── cliente_llm.py chamada ao modelo (API REST) e tratamento de erros de comunicação
├── resposta.py    interpretação/validação da resposta
└── saida.py       apresentação do resultado
```

## Limites do projeto
Execução local, um único LLM, entrada e saída textuais pelo terminal. Sem interface web/gráfica, banco de dados, RAG ou agentes.

## Instalação
Requer Python 3.12 (ver `.python-version`).
```bash
git clone https://github.com/geogomes/trendsia-p0.git
cd trendsia-p0
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Configuração do acesso ao LLM
```bash
cp .env.example .env   # preencher; o .env nunca é versionado
```
| Variável | Para quê | Obrigatória |
|---|---|---|
| `LLM_BASE_URL` | Endpoint da API | sim |
| `LLM_API_KEY` | Credencial | sim |
| `LLM_MODEL` | Identificador do modelo | sim |
| `LLM_TIMEOUT` | Timeout da chamada (s) | não (padrão 30) |
| `LLM_MAX_TOKENS` | Limite de tokens da resposta | não |
| `LLM_TEMPERATURE` | Parâmetro de geração | não |

_Provedor e modelo utilizados: a preencher (institucional ou outro, com procedimento de acesso)._

**Testes reais vs. simulados:** os testes em `tests/` **não** chamam o LLM (respostas e erros simulados). A execução real é demonstrada em `docs/evidencias/` e no vídeo.

## Execução
```bash
python -m app "texto de entrada"
# ou interativo:
python -m app
```

## Exemplos de entrada e saída
_a preencher_

## Execução dos testes
```bash
pytest -q
```

## Limitações conhecidas
_a preencher_

## Marcos
| Nível | Tag |
|---|---|
| Básico | `p0-basico` |
| Intermediário | `p0-intermediario` |
| Avançado (entrega final) | `p0-avancado` |

## Vídeo
_link (YouTube, não listado, legendas revisadas) — a informar na entrega_

## Relatório
`RELATORIO_EXECUCAO.md`
