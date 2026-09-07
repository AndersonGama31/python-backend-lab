# Challenge 001 — Deduplicação de eventos

**Nível:** Pleno  
**Tempo sugerido:** 30–45 minutos  
**Foco:** collections, mutabilidade, ordenação, complexidade e código idiomático em Python

## Cenário

Você recebe uma sequência de eventos de backend. Cada evento possui um `id` e um `timestamp`.

Eventos com o mesmo `id` representam versões diferentes do mesmo evento. Sua função deve manter apenas a versão mais recente de cada `id`.

## Implemente

```python
def deduplicate_events(events: list[dict[str, object]]) -> list[dict[str, object]]:
    ...
```

## Regras

- Eventos com o mesmo `id` são duplicados.
- Para cada `id`, mantenha o evento com o maior `timestamp`.
- O resultado final deve estar em ordem crescente de `timestamp`.
- A lista de entrada não pode ser alterada.
- Os dicionários originais também não devem ser modificados.
- `events=[]` deve retornar `[]`.
- Assuma que todo evento contém `id: str` e `timestamp: int` válidos.

## Exemplo

Entrada:

```python
[
    {"id": "A1", "timestamp": 10, "payload": "old"},
    {"id": "B2", "timestamp": 15, "payload": "only"},
    {"id": "A1", "timestamp": 20, "payload": "new"},
]
```

Saída:

```python
[
    {"id": "B2", "timestamp": 15, "payload": "only"},
    {"id": "A1", "timestamp": 20, "payload": "new"},
]
```

## Restrições

- Não use bibliotecas externas.
- Tente manter a seleção dos eventos mais recentes em `O(n)`.
- Explique mentalmente a complexidade total da sua solução, incluindo a ordenação final.

## Como executar

```bash
uv run pytest challenges/challenge_001 -q
```

Depois valide qualidade:

```bash
uv run ruff check .
uv run mypy .
```

## O que vou avaliar

- Correção
- Python idiomático
- Complexidade
- Legibilidade
- Tipagem
- Tratamento dos casos de borda

Não procure a solução antes de terminar. Quando concluir, me peça um code review do Challenge 001.
