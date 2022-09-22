from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'woocommerce-product-search-field-0')
    SEARCH_ICON_HEADER = (By.CSS_SELECTOR, '.header-search.header-search-dropdown') #icon present on main page
    SEARCH_ICON = (By.XPATH, "//button[@value='Search']//i[@class='icon-search']")
    LAPTOP_CATEGORY = (By.ID,'menu-item-468')
    CATEGORY_LINKS = (By.CSS_SELECTOR, "a.nav-top-link[href*='https://gettop.us/product-category']")

    def open_gittop_page(self):
        self.driver.get('https://gettop.us/')

    def verify_search_ui_elements(self):
        self.driver.find_element(*self.SEARCH_FIELD)
        self.driver.find_element(*self.SEARCH_ICON)
        self.driver.find_element(*self.SEARCH_ICON_HEADER)

    def hover_search_icon_in_header(self):
        search_icon = self.wait.until(EC.presence_of_element_located(self.SEARCH_ICON_HEADER))
        actions = ActionChains(self.driver)
        actions.move_to_element(search_icon)
        actions.perform()

    def enter_product_search_field(self, product):
        self.wait.until(
            EC.presence_of_element_located(self.SEARCH_FIELD)
        ).send_keys(product)
        self.click(*self.SEARCH_ICON)

    def click_laptop_category(self):
        self.find_element(*self.LAPTOP_CATEGORY).click()

    # def click_category_link(self):
    #     all_links = self.find_element(*self.CATEGORY_LINKS)
    #     print(all_links)
    #     for i in range(len(all_links)):
    #         link_to_click = self.driver.find_elements(*self.CATEGORY_LINKS)[i]
    #         link_to_click.click()





