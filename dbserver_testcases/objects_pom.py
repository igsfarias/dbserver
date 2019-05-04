# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class HomePage(object):
    products_list = (By.ID, 'homefeatured')
    product_button = (By.CLASS_NAME, 'button')
    product_name = (By.CLASS_NAME, 'product-name')
    product_box = (By.CLASS_NAME, 'ajax_block_product')
    proceed_button = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span')
    product_added_description = (By.ID, 'layer_cart_product_title')

    def __init__(self, driver=None):
        self.driver = webdriver.Firefox() if not driver else driver
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com')
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def select_product(self):
        products = self.driver.find_element(*self.products_list).find_elements(*self.product_box)
        if len(products):
            product_selected = products[0]
            ActionChains(self.driver).move_to_element(product_selected).perform()
            product_description = product_selected.find_element(*self.product_name).text.split('\n')[0]
            product_selected.find_element(*self.product_button).click()

            return product_description
        raise Exception("Products not found.")

    def get_description_product_added(self):
        # Elemento product_added_description já existe inicialmente no HTML, mas é preenchido apenas em tempo de execução.
        # Dessa forma, o uso do wait implícito não é possivel.
        time.sleep(4)
        return self.driver.find_element(*self.product_added_description).text

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_button).click()
        return CartSummaryPage(self.driver)


class CartSummaryPage(object):
    description_product_in_summary = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr/td[2]/p/a')
    proceed_button = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]')
    total_value = (By.ID, 'total_price')

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_description_product_in_summary(self):
        return self.driver.find_element(*self.description_product_in_summary).text

    def get_total_value(self):
        return self.driver.find_element(*self.total_value).text

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_button).click()

        return CartAutheticationPage(self.driver)


class CartAutheticationPage(object):
    email_create = (By.ID, 'email_create')
    create_account_button = (By.XPATH, '//*[@id="SubmitCreate"]')
    register_button = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button/span')
    form_personal_information_title_gender = (By.XPATH, '//*[@id="id_gender1"]')
    form_personal_information_first_name = (By.ID, 'customer_firstname')
    form_personal_information_last_name = (By.ID, 'customer_lastname')
    form_personal_information_password = (By.ID, 'passwd')
    form_personal_information_first_name_addres = (By.ID, 'firstname')
    form_personal_information_last_name_addres = (By.ID, 'lastname')
    form_personal_information_addres = (By.ID, 'address1')
    form_personal_information_city = (By.ID, 'city')
    form_personal_information_state = (By.ID, 'id_state')
    form_personal_information_postal_code = (By.ID, 'postcode')
    form_personal_information_country = (By.ID, 'id_country')
    form_personal_information_phone_mobile = (By.ID, 'phone_mobile')
    form_personal_information_adress_name = (By.ID, 'alias')

    def __init__(self, driver):
        self.driver = driver

    def create_account(self, email):
        self.driver.find_element(*self.email_create).send_keys(email)
        self.driver.find_element(*self.create_account_button).click()
        return self

    def set_personal_information(self, personal_data):
        self.driver.find_element(*self.form_personal_information_title_gender).click()
        self.driver.find_element(*self.form_personal_information_first_name).send_keys(personal_data.get('first_name'))
        self.driver.find_element(*self.form_personal_information_last_name).send_keys(personal_data.get('last_name'))
        self.driver.find_element(*self.form_personal_information_password).send_keys(personal_data.get('password'))
        self.driver.find_element(*self.form_personal_information_first_name_addres).clear()
        self.driver.find_element(*self.form_personal_information_first_name_addres).send_keys(
            personal_data.get('first_name'))
        self.driver.find_element(*self.form_personal_information_last_name_addres).clear()
        self.driver.find_element(*self.form_personal_information_last_name_addres).send_keys(
            personal_data.get('last_name'))
        self.driver.find_element(*self.form_personal_information_addres).send_keys(personal_data.get('adress'))
        self.driver.find_element(*self.form_personal_information_city).send_keys(personal_data.get('city'))
        select = Select(self.driver.find_element(*self.form_personal_information_state))
        select.select_by_visible_text(personal_data.get('state'))
        self.driver.find_element(*self.form_personal_information_postal_code).send_keys(
            personal_data.get('postal_code'))
        select = Select(self.driver.find_element(*self.form_personal_information_country))
        select.select_by_visible_text(personal_data.get('country'))
        self.driver.find_element(*self.form_personal_information_phone_mobile).send_keys(
            personal_data.get('phone_mobile'))
        self.driver.find_element(*self.form_personal_information_adress_name).clear()
        self.driver.find_element(*self.form_personal_information_adress_name).send_keys(
            personal_data.get('adress_name'))

    def proceed_to_register(self):
        self.driver.find_element(*self.register_button).click()
        return CartAdressPage(self.driver)


class CartAdressPage(object):
    adress = (By.CLASS_NAME, 'address_address1')
    city_and_state = (By.CLASS_NAME, 'address_city ')
    proceed_button = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span')

    def __init__(self, driver):
        self.driver = driver

    def get_adress(self):
        return self.driver.find_element(*self.adress).text

    def get_city_and_state(self):
        return self.driver.find_element(*self.city_and_state).text

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_button).click()
        return CartShippingPage(self.driver)


class CartShippingPage(object):
    checkbox_terms_of_service = (By.XPATH, '//*[@id="cgv"]')
    proceed_button = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span')

    def __init__(self, driver):
        self.driver = driver

    def check_terms(self):
        self.driver.find_element(*self.checkbox_terms_of_service).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_button).click()
        return CartPaymentPage(self.driver)


class CartPaymentPage(object):
    total_price = (By.ID, 'total_price')
    payment_method = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a')
    confirm_order_button = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span')
    confirmation_text = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/p/strong')

    def __init__(self, driver):
        self.driver = driver

    def get_total_value(self):
        return self.driver.find_element(*self.total_price).text

    def selec_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def confirm_order(self):
        self.driver.find_element(*self.confirm_order_button).click()

    def get_confirmation(self):
        return self.driver.find_element(*self.confirmation_text).text
