from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class TestEntryExitForStellarBurgers:

    def setup(self):
        self.user = "oleg123@yandex.ru"
        self.password = "pwd12345"

    # Проверка входа по кнопке «Войти в аккаунт» на главной
    def test_login_by_button_entry(self):
        result = True

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Войти в аккаунт']"))).click()

            self.login()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка входа через кнопку «Личный кабинет»
    def test_login_by_button_own_cabinet(self):
        result = True

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/account']"))).click()

            self.login()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка входа через кнопку в форме регистрации
    def test_login_by_form_registration(self):
        result = True

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/account']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[text()= 'Зарегистрироваться']"))).click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()= 'Войти']"))).click()

            self.login()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_by_button_in_form_restore_password(self):
        result = True

        self.open()

        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/account']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[@href = '/forgot-password']"))).click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()= 'Войти']"))).click()

            self.login()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))
        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка выхода по кнопке «Выйти» в личном кабинете.
    def test_by_exit_button_in_own_cabinet(self):
        result = True

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Войти в аккаунт']"))).click()

            self.login()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Оформить заказ']")))

            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href = '/account']"))).click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Выход']"))).click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Войти']")))
        except TimeoutException:
            result = False

        self.close()
        assert result

    def login(self):
        # Найди поле "Email" и заполни его
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(self.user)
        # Найди поле "Пароль" и заполни его
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.password)
        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def close(self):
        self.driver.quit()
