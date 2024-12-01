# XSS Detector

Um script em Python que automatiza a detecção de vulnerabilidades **Cross-Site Scripting (XSS)** em sites, utilizando o Selenium para encontrar campos de entrada e testar payloads.

## Índice
1. Funcionalidades
2. Requisitos
3. Instalação
4. Como Usar
5. Aviso Legal
6. Licença
7. Próximos Passos

## Funcionalidades
- Detecta automaticamente campos de entrada em páginas web.
- Injeta payloads XSS para identificar vulnerabilidades.
- Exibe respostas do site no terminal para análise.
- Mantém o navegador aberto para observação manual.

## Requisitos
- **Python 3.10+**
- **Selenium**
- **Google Chrome**
- **ChromeDriver** (compatível com a versão do navegador)

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/LeonardoCides/system-xss
   cd xss-detector
