// Importa funções essenciais do Selenium webdriver.
const { Builder, By } = require('selenium-webdriver');

(async function testeHanked() {
  const url = 'https://www.hankeds.com.br/prova/login2.html';
  // Cria um novo driver do Chrome.
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    await driver.get(url); // Navega para a URL indicada.
    await driver.sleep(2000); // Espera página carregar.

    // Localiza os campos do formulário.
    const username = await driver.findElement(By.id('username'));
    const password = await driver.findElement(By.id('password'));
    const botao = await driver.findElement(By.xpath("//button[contains(text(),'Entrar')]"));

    // Função para digitar lentamentea.
    for (const letra of 'admin') {
      await username.sendKeys(letra);
      await driver.sleep(250);
    }
    await driver.sleep(1000);

    for (const letra of 'admin123456') {
      await password.sendKeys(letra);
      await driver.sleep(250);
    }

    await driver.sleep(1000);
    await botao.click();  // Clica para enviar formulário.
    await driver.sleep(4000);

    const urlAtual = await driver.getCurrentUrl();

    // Verifica o redirecionamento após login.
    if (urlAtual.includes('destino.html')) {
      console.log('Teste passou: redirecionado corretamente.');
    } else {
      console.log('Teste falhou: não houve redirecionamento.');
    }

    await driver.sleep(5000);

  } catch (err) {
    console.error('Erro durante o teste:', err);
  } finally {
    await driver.quit(); // Fecha navegador.
  }
})();
