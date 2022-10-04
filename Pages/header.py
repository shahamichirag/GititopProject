from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'woocommerce-product-search-field-0')
    SEARCH_ICON_HEADER = (By.CSS_SELECTOR, '.header-search.header-search-dropdown') #icon present on main page
    SEARCH_ICON = (By.XPATH, "//button[@value='Search']//i[@class='icon-search']")
    LAPTOP_CATEGORY = (By.ID,'menu-item-468')
    CATEGORY_LINKS = (By.CSS_SELECTOR, "a.nav-top-link[href*='https://gettop.us/product-category']")
    CATEGORY_PAGE_TITLE = (By.CSS_SELECTOR,'.woocommerce-breadcrumb.breadcrumbs.uppercase')

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
        sleep(12)
        self.click(*self.SEARCH_ICON)

    def click_laptop_category(self):
        self.wait.until(EC.presence_of_element_located(self.LAPTOP_CATEGORY)).click()

    def click_category_link(self):
        all_links = self.find_elements(*self.CATEGORY_LINKS)
        for i in range(len(all_links)):
            link_to_click = self.find_elements(*self.CATEGORY_LINKS)[i]
            link_text = 'HOME ' + '/ ' + link_to_click.text
            sleep(12)
            link_to_click.click()
            header_text = self.find_element(*self.CATEGORY_PAGE_TITLE).text
            print(header_text)
            if link_text in header_text:
                return True




