# ProvaTest

Execução do Teste 1 Python

https://github.com/user-attachments/assets/72561ba4-e291-446e-98da-83e4b11dbaec

Execução do Teste 2 Node

https://github.com/user-attachments/assets/8bef774c-0fe5-41c9-bbd0-904c1091767a

Pergunta 4:
Python

O Selenium oferece bibliotecas específicas para Python que facilitam o controle e automação de navegadores. Ele usa WebDrivers específicos, como o ChromeDriver, que atuam como intermediários, possibilitando a comunicação eficaz entre os scripts Python e o navegador.

Node.js

Na plataforma Node.js, utiliza-se a biblioteca selenium-webdriver, uma implementação oficial e robusta do protocolo WebDriver. Assim como no Python, os comandos escritos em scripts Node.js são enviados ao navegador por meio do WebDriver, permitindo a automação completa das ações no navegador.


Jmeter Testes:

![Captura de tela 2025-04-18 130819](https://github.com/user-attachments/assets/4e39554b-5277-4783-8d79-cefdb4a9dd2c)

Análise do Resultado do JMeter:

Durante o teste inicial, o servidor respondeu de maneira estável e rápida (aproximadamente 10 segundos por solicitação).

A partir da solicitação número 4942, houve uma mudança significativa no comportamento, com aumento drástico no tempo de resposta (acima de 220 segundos por solicitação) e falhas constantes.

Isso demonstra claramente que o servidor tem uma capacidade limite próxima de 4900 usuários simultâneos. Ao ultrapassar essa carga, o desempenho se deteriora rapidamente, causando falhas nas requisições.
