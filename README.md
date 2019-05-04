# Desafio Técnico de Automação de Testes

Implementação com a linguagem Python e framework Selenium Webdrive.

#### Caso de teste
-> Realizar uma compra com sucesso.

	1. Acessar o site: www.automationpractice.com.
	2. Escolha um produto qualquer na loja.
	3. Adicione o produto escolhido ao carrinho.
	4. Prossiga para o checkout.
	5. Valide se o produto foi corretamente adicionado ao carrinho e prossiga caso esteja tudo certo.
	6. Realize o cadastro do cliente preenchendo todos os campos obrigatórios dos formulários.
	7. Valide se o endereço está correto e prossiga.
	8. Aceite os termos de serviço e prossiga.
	9. Valide o valor total da compra.
	10. Selecione um método de pagamento e prossiga.
	11. Confirme a compra e valide se foi finalizada com sucesso


#### Configuração
+ Python 3.7 
	+ Biblioteca Selenium 3.141.0
	+ Biblioteca HtmlTestRunner 1.2
+ Pip 19.1
+ Navegador Firefox 66.0.3

Para execução dos testes é necessario a instalação das dependências listadas em requirements.txt e do driver para interagir com o navegador.

Para instalar as dependências faça: 

`$ pip install -r requirements.txt`

Para configuração do driver utilizado pelo framework Selenium é necessário a realização do procedimento apresentado na página de Instalaçao do [Selenium Python](https://selenium-python.readthedocs.io/installation.html).


#### Execução

`$ python  testsuite_main.py`

#### Resultados

O resultado da suite de testes é armazenado em um arquivo HTML em  `/reports`
