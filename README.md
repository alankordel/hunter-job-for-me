# Hunter Job for Me

Projeto de aprendizado em Python e Engenharia de Dados que coleta vagas reais,
avalia a compatibilidade com o perfil de Alan e gera um CSV para revisão.

O projeto ainda é um protótipo. Ele não realiza candidaturas automáticas e não
coleta LinkedIn, Gupy, Indeed ou páginas protegidas por login, CAPTCHA ou
mecanismos antibot.

## Estado atual

O pipeline usa a [API pública da Remotive](https://remotive.com/api/remote-jobs).
Ela foi escolhida porque oferece vagas remotas reais em JSON, sem autenticação.
O exemplo antigo com `books.toscrape.com` foi retirado porque era apenas uma
simulação e não representava vagas reais.

O pipeline consulta a API, converte os registros para `Job`, calcula o score,
remove duplicados, ordena os resultados e grava `data/processed/jobs.csv`.

## Tecnologias

- Python
- Requests
- Beautiful Soup
- Pandas
- Pytest

## Instalação no Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Execução e testes

```powershell
python main.py
python -m pytest
```

O terminal mostra quantas vagas foram recebidas, ignoradas, filtradas e
deduplicadas. O CSV usa UTF-8 com BOM para preservar acentos no Excel. Os
testes usam dados simulados e não acessam a internet.

## Como personalizar a busca

Edite `src/config/settings.py`:

- `POSITIVE_KEYWORDS`: tecnologias e cargos desejados;
- `INTEREST_LOCATIONS`: localidades de interesse;
- `NEGATIVE_TITLE_TERMS`: senioridades que recebem penalização;
- `MINIMUM_MATCH_SCORE`: pontuação mínima para aparecer no CSV.

A pontuação soma 3 pontos por termo no título, 1 por termo na descrição,
2 por localização de interesse e 2 por vaga remota. Termos incompatíveis
no título retiram 3 pontos. Um termo negativo apenas na descrição não exclui
a vaga.

## Colunas do CSV

`title`, `company`, `location`, `work_model`, `source`, `url`,
`technologies`, `match_score`, `matched_keywords` e `published_at`.

## Limitações

- usa apenas uma fonte, voltada principalmente a vagas remotas globais;
- o filtro por palavras-chave pode produzir falsos positivos;
- não há banco de dados, dashboard ou notificações;
- a disponibilidade e o formato da API dependem da Remotive;
- o projeto não faz candidatura automática.

## Roadmap

- [x] Consumir uma fonte pública de vagas reais
- [x] Filtrar e pontuar vagas pelo perfil
- [x] Remover duplicados e exportar CSV
- [x] Adicionar testes unitários básicos
- [ ] Adicionar novas fontes públicas
- [ ] Criar banco de dados
- [ ] Criar dashboard
- [ ] Enviar notificações
- [ ] Automatizar atualizações
