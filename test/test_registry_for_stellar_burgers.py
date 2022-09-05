import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope="class")
def correct_account():
    return {"name": "oleg", "mail": "oleg151@ya.ru", "password": "pwd12345"}


@pytest.fixture(scope="class")
def not_correct_account():
    return {"name": "oleg", "mail": "oleg152@ya.ru", "password": "pwd12"}


@pytest.mark.usefixtures("correct_account", "not_correct_account")
class TestRegistryForStellarBurgers:

    # Проверка успешной регистрации
    def test_successful_registration(self, correct_account):
        result = True

        name = correct_account['name']
        mail = correct_account['mail']
        password = correct_account['password']

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Войти в аккаунт']"))).click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href = '/register']"))).click()

            self.registration(name, mail, password)

            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//button[text() = 'Войти']")))

        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка на Ошибку для некорректного пароля
    def test_failed_registration_by_wrong_password(self, not_correct_account):
        result = True

        name = not_correct_account['name']
        mail = not_correct_account['mail']
        password = not_correct_account['password']

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Войти в аккаунт']"))).click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href = '/register']"))).click()

            self.registration(name, mail, password)

            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']")))

        except TimeoutException:
            result = False

        self.close()
        assert result

    def registration(self, name, email, password):
        # Найди поле "Имя" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Имя']/following::input").send_keys(name)
        # Найди поле "Email" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Email']/following::input").send_keys(email)
        # Найди поле "Пароль" и заполни его
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        # Найди кнопку "Зарегистрироваться" и кликни по ней
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def close(self):
        self.driver.quit()
