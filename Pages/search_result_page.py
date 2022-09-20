from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import Page


class Searchresult(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
    ERROR_MESSAGE = (By.XPATH, "//div[@class='shop-container']//p[@class='woocommerce-info']")

    def verify_product_search_result(self, product_result):
        expected_result = f'HOME / SHOP / SEARCH RESULTS FOR “{product_result}”'
        actual_result = self.find_element(*self.PRODUCT_TITLE).text
        assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

    def verify_error_message_unavailable_product(self):
        expected_result = "No products were found matching your selection."
        actual_result = self.find_element(*self.ERROR_MESSAGE).text
        assert expected_result == actual_result, f'Expected to see {expected_result} but got {actual_result}'
