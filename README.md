# XSS Vulnerability Scanner & Lab 🛡️🐍

Este projeto é uma ferramenta de segurança desenvolvida em **Python** para fins **estritamente educacionais**. O objetivo é demonstrar o funcionamento de vulnerabilidades Cross-Site Scripting (XSS) e como automatizar a detecção de falhas em ambientes de teste.

> ⚠️ **AVISO LEGAL:** O uso desta ferramenta contra alvos sem permissão expressa é ilegal. O autor não se responsabiliza pelo uso indevido. Destinado apenas a laboratórios de CTF e Pentest.

## 🛡️ Funcionalidades (Python Powered)

- [x] **Análise Dinâmica**: Envio de payloads via requisições HTTP (`requests`).
- [x] **Parsing de HTML**: Identificação de reflexão de scripts no DOM usando `BeautifulSoup`.
- [x] **Automação de Payloads**: Dicionário customizável de vetores de ataque.
- [x] **Detecção de Filtros**: Verifica se caracteres como `< > /` estão sendo sanitizados pelo servidor.

## 🛠 Tecnologias e Bibliotecas

* **Python 3**
* **Requests**: Para manipulação de requisições HTTP.
* **BeautifulSoup4**: Para analisar a resposta HTML do alvo.
* **Colorama**: Para logs coloridos e legíveis no terminal.
