from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as chains
# Import
from test_data import TestData
from locators import Locators

class BasePage():
    """
        Kelas ini akan jadi parent untuk kelas lainnya
        Kelas ini akan memuat element dan fungsi yang dapat digunakan di kelas lain
    """
    def __init__(self, driver):
        self.driver = driver

    # Fungsi untuk click locator yang diberikan
    def click(self, locator):
        WDW(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()

    # Fungsi enter teks
    def enter_text(self, locator, text):
        WDW(self.driver, 30).until(EC.element_to_be_clickable(locator)).send_keys(text)

    # Fungsi untuk memperoleh teks dari suatu locator
    def get_text(self, locator):
        return WDW(self.driver, 30).until(EC.visibility_of_element_located(locator)).text

    # Fungsi untuk mengecek visibility suuatu element
    def is_visible(self, locator):
        try:
            element = WDW(self.driver, 30).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False
    # fungsi untuk mouse hover and click elemet yang di hover
    def hover_to_click(self, locator):
        element = WDW(self.driver, 30).until(EC.presence_of_element_located(locator))
        chains(self.driver).move_to_element(element).click().perform()

    # fungsi untuk mouse hover and click element yang muncul setelah di hover
    def hover_to_click_element(self, locator1, locator2):
        element = WDW(self.driver,30).until(EC.presence_of_element_located(locator1))
        chains(self.driver).move_to_element(element).perform()
        WDW(self.driver, 10).until(EC.visibility_of_element_located(locator2)).click()

class HomePage(BasePage):
    """
    Kelas untuk halaman home
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def redirect_home_page_success(self):
        self.click(Locators.HOME_PAGE_SLIDER)
        self.is_visible(Locators.HOME_PAGE_TITLE)

class WelcomePage(BasePage):
    """
    Kelas untuk halaman selamat datang
    """
    def __init__(self, driver):
        super().__init__(driver)

    def redirect_welcome_page_success(self):
        self.click(Locators.WELCOME_PAGE_SLIDER)
        self.is_visible(Locators.WELCOME_PAGE_TITLE)

class AdvantagesPage(BasePage):
    """
    Kelas untuk halaman keuntungan
    """
    def __init__(self, driver):
        super().__init__(driver)

    def redirect_advantages_page_success(self):
        self.click(Locators.ADVANTAGES_PAGE_SLIDER)
        self.is_visible(Locators.ADVANTAGES_PAGE_TITLE)

class MainFeaturePage(BasePage):
    """
    Kelas untuk halaman fitur utama
    """
    def __init__(self, driver):
        super().__init__(driver)

    def redirect_main_feature_page_success(self):
        self.click(Locators.MAIN_FEATURE_PAGE_SLIDER)
        self.is_visible(Locators.MAIN_FEATURE_PAGE_TITLE)



class SecurityPage(BasePage):
    """
    Kelas untuk halaman keamanan
    """
    def __init__(self, driver):
        super().__init__(driver)

    def redirect_security_page_success(self):
        self.click(Locators.SECURITY_PAGE_SLIDER)
        self.is_visible(Locators.SECURITY_PAGE_TITLE)

class DownloadPage(BasePage):
    """
    Kelas untuk halaman download
    """
    def __init__(self, driver):
        super().__init__(driver)

    def redirect_download_page(self):
        self.click(Locators.DOWNLOAD_PAGE_SLIDER)
        self.is_visible(Locators.DOWNLOAD_PAGE_TITLE)