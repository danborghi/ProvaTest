# As importações são necessárias para execução de código não nativo
# em Python base.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicialização dos drivers previamente importados
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Try é a função de chamada para iniciar o teste
# O código apresenta elementos de delay para garantir o funcionamento da automação
try:
    url = "https://www.hankeds.com.br/prova/login.html"
    driver.get(url)

    time.sleep(2)

    def digitar_lento(elemento, texto, delay=0.25):
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(delay)

    # Este trecho define os tempos de espera e ação ao detectar os elementos "usuario, senha, e botao"
    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    senha = driver.find_element(By.ID, "password")
    botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")

    digitar_lento(usuario, "admin")
    time.sleep(1)
    digitar_lento(senha, "admin123456")
    time.sleep(1)

    botao.click()
    time.sleep(4)

    # Sistema de condicionais simples para informar se a URL almejada foi acessada ou não ao fim do teste
    if "destino.html" in driver.current_url:
        print(" Teste passou: redirecionado corretamente.")
    else:
        print(" Teste falhou: redirecionamento não ocorreu.")

    time.sleep(5)

# Com o Try previamente definido, caso haja alguma exceção/erro, ela será capturada e exibida aqui
except Exception as e:
    print(" Erro durante o teste:", str(e))

finally:
    driver.quit()