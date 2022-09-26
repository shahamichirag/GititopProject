from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import Page


class Searchresult(Page):

    PRODUCT_TITLE = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
    ERROR_MESSAGE = (By.XPATH, "//div[@class='shop-container']//p[@class='woocommerce-info']")
    IMAGE_SLIDER = (By.CSS_SELECTOR,"figure[class*='product-gallery-slider'] button.flickity-button.flickity-prev-next-button.next")
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.title-wrapper')
    THUMBNAIL_IMAGES = (By.CSS_SELECTOR, "div.col div[aria-selected='false'] img.attachment-woocommerce_thumbnail")
    FACEBOOK_LINK = (By.XPATH, "//div[@class='social-icons share-icons share-row relative']//i[@class='icon-facebook']")

    def __init__(self, driver):
        super().__init__(driver)
        self.original_window = None

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

    def user_can_see_thumbnail_image(self):
        images = self.find_elements(*self.THUMBNAIL_IMAGES)
        for i in range(len(images)):
            image_to_click = self.find_elements(*self.THUMBNAIL_IMAGES)[i]
            image_to_click.click()

    def store_window(self):
        self.original_window = self.driver.current_window_handle
        print('original window:', self.original_window)

    def click_facebook_link(self):
        self.driver.find_element(*self.FACEBOOK_LINK).click()

    def switch_to_new_window(self):
        self.new_window_is_opened()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def switch_to_original_window(self):
        self.driver.switch_to.window(self.original_window)