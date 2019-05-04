# coding=utf-8
import random
import unittest
from selenium import webdriver

from dbserver_testcases.objects_pom import HomePage


class TestCasesAutomationPractice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_buy_with_new_user(self):
        homepage = HomePage(self.driver)

        # Verificando se a página que foi aberta contém o titulo esperado
        self.assertIn("My Store", homepage.get_title())

        # Escolhendo o primeiro poduto da lista de produtos na página inicial
        description_selected_product = homepage.select_product()

        # verificando se o produto selecionando é o mesmo que foi para o carrinho
        self.assertIn(description_selected_product, homepage.get_description_product_added())

        # proseguindo para o checkout
        cart_summary_page = homepage.proceed_to_checkout()

        # verificando se o produto selecionando é o mesmo que esta no summary
        self.assertIn(description_selected_product, cart_summary_page.get_description_product_in_summary())

        # guardando valor da compra
        total_value = cart_summary_page.get_total_value()

        # proseguindo para o checkout
        cart_authentication_page = cart_summary_page.proceed_to_checkout()

        # defindo e-mail que será usado para cadastro de novo usuário no sistema
        new_email = "dbserver.newuser.{}@dbserver.com".format(random.randint(0, 100000))

        # iniciando registro de novo usuário
        signup_form = cart_authentication_page.create_account(new_email)

        # dados do novo usuário
        personal_data = {
            'first_name': 'Joao', 'last_name': 'Silva', 'password': '!password1',
            'adress': '464 New Lots Ave, Brooklyn', 'city': 'New York', 'state': 'New York',
            'postal_code': '11207', 'country': 'United States', 'phone_mobile': '+1 123-456-7890',
            'adress_name': 'My first address'
        }
        signup_form.set_personal_information(personal_data)

        # proseguindo para o registro com dados do novo usuário
        cart_adress_page = signup_form.proceed_to_register()

        # verificando endereço
        self.assertIn("464 New Lots Ave, Brooklyn", cart_adress_page.get_adress()),
        self.assertIn("New York, New York 11207", cart_adress_page.get_city_and_state())

        cart_shipping_page = cart_adress_page.proceed_to_checkout()

        # aceitando os termos
        cart_shipping_page.check_terms()
        cart_payment_page = cart_shipping_page.proceed_to_checkout()

        # validando valor da compra
        self.assertIn(total_value, cart_payment_page.get_total_value())

        # selecionando o primeiro meio de pagamento dos disponiveis
        cart_payment_page.selec_payment_method()

        # confirmando compra
        cart_payment_page.confirm_order()

        # varificando confirmaçao do pedido
        self.assertIn('Your order on My Store is complete.', cart_payment_page.get_confirmation())

    def tearDown(self):
        self.driver.close()
