from selenium.webdriver.common.by import By

class Locators():
    # --- Navbar Locator ---
    HOME_NAVBAR = (By.CSS_SELECTOR, ".navbar-nav > a:nth-child(1)")
    ABOUT_NAVBAR = (By.CSS_SELECTOR, ".navbar-nav > a:nth-child(2)")

    # --- Slider Pagination Locators ---
    HOME_PAGE_SLIDER = (By.CSS_SELECTOR, ".col > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
    WELCOME_PAGE_SLIDER = (By.CSS_SELECTOR, ".col > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
    ADVANTAGES_PAGE_SLIDER = (By.CSS_SELECTOR, ".col > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)")
    MAIN_FEATURE_PAGE_SLIDER = (By.CSS_SELECTOR, ".col > div:nth-child(2) > div:nth-child(4) > div:nth-child(1)")
    SECURITY_PAGE_SLIDER = (By.CSS_SELECTOR, ".col > div:nth-child(2) > div:nth-child(5) > div:nth-child(1)")
    DOWNLOAD_PAGE_SLIDER = (By.CSS_SELECTOR, ".col > div:nth-child(2) > div:nth-child(6) > div:nth-child(1)")

    # --- Home Page Locators
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, ".promo-caption > h1:nth-child(1)")

    # --- Welcome Page Locators
    WELCOME_PAGE_TITLE = (By.CSS_SELECTOR, ".top-content > div:nth-child(1) > h2:nth-child(1)")

    # --- Advantages Page Locators
    ADVANTAGES_PAGE_TITLE = (By.CSS_SELECTOR, ".benefit > div:nth-child(1) > h2:nth-child(1)")

    # --- Main Feature Page Locators
    MAIN_FEATURE_PAGE_TITLE = (By.CSS_SELECTOR, ".main-feature > div:nth-child(1) > h2:nth-child(1)")
    MENU_TAB_MONITORING = (By.ID, "feature-tab-tab-monitoring")
    MENU_TAB_EXPENSE = (By.ID, "feature-tab-tab-manage-spending")
    MENU_TAB_EXPENSE_TITLE = (By.CSS_SELECTOR, "#feature-tab-tabpane-manage-spending > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)")
    MENU_TAB_SAVING = (By.ID, "feature-tab-tab-saving")
    MENU_TAB_SAVING_TITLE = (By.CSS_SELECTOR, "div.active:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)")

    # --- Security Page Locators
    SECURITY_PAGE_TITLE = (By.CSS_SELECTOR, "div.caption:nth-child(1) > h2:nth-child(1)")

    # --- Download Page Locators
    DOWNLOAD_PAGE_TITLE = (By.CSS_SELECTOR, ".download-details > div:nth-child(2) > h2:nth-child(1)")
    PLAYSTORE_BUTTON = (By.CSS_SELECTOR, "a.playstore:nth-child(3) > img:nth-child(1)")