# Python Backend Lab

Laboratório prático para transição e aprofundamento em Python com foco em engenharia de backend.

## Objetivo

Praticar Python em nível profissional por meio de desafios progressivos envolvendo:

- Python idiomático
- collections e estruturas de dados
- typing
- orientação a objetos
- iterators e generators
- decorators e context managers
- tratamento de erros
- asyncio e concorrência
- testes com pytest
- debugging e refactoring
- APIs e arquitetura backend
- performance e system design

## Stack do laboratório

- Python 3.13
- uv
- pytest
- pytest-cov
- Ruff
- mypy
- GitHub Codespaces
- GitHub Actions

## Abrindo no Codespaces

No GitHub:

1. Clique em **Code**.
2. Abra a aba **Codespaces**.
3. Clique em **Create codespace on main**.
4. Aguarde o ambiente terminar de configurar.

O container instala o `uv` e executa `uv sync` automaticamente.

## Comandos úteis

Validar o ambiente:

```bash
uv run pytest tests -q
```

Executar um desafio específico:

```bash
uv run pytest challenges/challenge_001 -q
```

Lint:

```bash
uv run ruff check .
```

Formatação:

```bash
uv run ruff format .
```

Tipagem:

```bash
uv run mypy .
```

## Fluxo de estudo

Cada desafio possui um enunciado, um arquivo `solution.py` e testes públicos.

Fluxo recomendado:

1. Leia somente o `README.md` do desafio.
2. Implemente a solução sem pesquisar a resposta.
3. Execute os testes públicos.
4. Rode Ruff e mypy.
5. Faça commit da solução.
6. Peça ao ChatGPT um code review.
7. Após o review, refatore se necessário.

Além dos testes públicos, a revisão pode considerar casos de borda adicionais para avaliar a interpretação da especificação.

## Diagnóstico inicial

Os primeiros desafios servem para mapear lacunas na transição para Python:

1. Collections e transformação de dados
2. Mutabilidade e referências
3. Dict, Set e hashing
4. Iterators e generators
5. Exceptions e context managers
6. Decorators
7. Typing e dataclasses
8. OO idiomático
9. Asyncio
10. Problema backend integrado

A dificuldade dos desafios seguintes será ajustada com base no desempenho.

## Challenge atual

### Challenge 001 — Deduplicação de eventos

Abra:

```text
challenges/challenge_001/README.md
```

Implemente a função em:

```text
challenges/challenge_001/solution.py
```

Depois execute:

```bash
uv run pytest challenges/challenge_001 -q
```

Quando todos os testes passarem, faça commit e peça um code review do Challenge 001.
