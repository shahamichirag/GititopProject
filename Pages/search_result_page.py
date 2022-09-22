from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import Page
from time import sleep


class Searchresult(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
    ERROR_MESSAGE = (By.XPATH, "//div[@class='shop-container']//p[@class='woocommerce-info']")
    IMAGE_SLIDER = (By.CSS_SELECTOR,"figure[class*='product-gallery-slider'] button.flickity-button.flickity-prev-next-button.next")
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.title-wrapper')


    def verify_product_search_result(self, product_result):
        expected_result = f'HOME / SHOP / SEARCH RESULTS FOR “{product_result}”'
        actual_result = self.find_element(*self.PRODUCT_TITLE).text
        assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

    def verify_error_message_unavailable_product(self):
        expected_result = "No products were found matching your selection."
        actual_result = self.find_element(*self.ERROR_MESSAGE).text
        assert expected_result == actual_result, f'Expected to see {expected_result} but got {actual_result}'

    def click_first_product_laptop(self):
        self.driver.find_element(*self.FIRST_PRODUCT).click()


    def user_can_shuffle_images(self):
        product_preview = self.find_element(*self.IMAGE_SLIDER)
        for i in range(4):
            actions = ActionChains(self.driver)
            actions.move_to_element(product_preview).pause(1).click()
            actions.perform()

