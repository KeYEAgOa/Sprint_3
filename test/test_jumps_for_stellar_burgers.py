from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class TestJumpsForStellarBurgers:

    def setup(self):
        self.user = "oleg123@yandex.ru"
        self.password = "pwd12345"

    # Проверка переход по клику на «Личный кабинет»
    def test_jumps_to_own_cabinet(self):
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
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text() = 'Выход']")))

        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка перехода из личного кабинета в конструктор по клику на «Конструктор» и на логотип Stellar Burgers
    def test_jump_from_own_cabinet_to_constructor(self):
        result = True

        self.open()
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/account']"))).click()

            # jump to constructor
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/']"))).click()

            # check that h1 Соберите бургер присутствует
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))

        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка перехода из конструктора к разделу «Булки»
    def test_jump_from_constructor_to_bulki(self):
        result = True

        self.open()
        try:
            # jump to constructor
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/']"))).click()

            # jump to Начинки
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//span[ text() = 'Начинки']"))).click()

            # jump to Булки
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//span[ text() = 'Булки']"))).click()

            # check that h2 Булки присутствует
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Булки']")))

        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка перехода из конструктора к разделу «Соусы»
    def test_jump_from_constructor_to_sousi(self):
        result = True

        self.open()
        try:
            # jump to constructor
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/']"))).click()

            # jump to Соусы
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//span[ text() = 'Соусы']"))).click()

            # check that h2 Соусы присутствует
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Соусы']")))

        except TimeoutException:
            result = False

        self.close()
        assert result

    # Проверка перехода из конструктора к разделу «Начинки»
    def test_jump_from_constructor_to_nachinki(self):
        result = True

        self.open()
        try:
            # jump to constructor
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/']"))).click()

            # jump to Начинки
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//span[ text() = 'Начинки']"))).click()

            # check that h2 Начинки присутствует
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Начинки']")))

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
