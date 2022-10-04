from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Mobileheader(Page):

    HAMBURGER_MENU = (By.CSS_SELECTOR, 'a[href="#"]')
    LAPTOP = (By.CSS_SELECTOR, "div[id='main-menu'] a[href*= 'https://gettop.us/product-category/laptop']")
    LAPTOP_ITEMS = (By.CSS_SELECTOR, 'div.product-small.box')
    LAPTOP_ITEM_SLIDER = (By.CSS_SELECTOR,
                          "figure[class*='product-gallery-slider'] button.flickity-button.flickity-prev-next-button.next")
    THUMBNAIL_IMAGES_MOBILE = (By.CSS_SELECTOR, "img[class='attachment-woocommerce_thumbnail']")

    def click_hamburger_menu(self):
        self.find_element(*self.HAMBURGER_MENU).click()
        sleep(4)

    def click_laptop(self):
        self.find_element(*self.LAPTOP).click()

    def click_laptop_items(self):
        self.find_element(*self.LAPTOP_ITEMS).click()

    def laptop_items_slider(self):
        for i in range(3):
            self.find_element(*self.LAPTOP_ITEM_SLIDER).click()
            sleep(2)

    def user_can_see_thumbnail_image_from_mobile(self):
        images = self.find_elements(*self.THUMBNAIL_IMAGES_MOBILE)
        for i in range(len(images)):
            image_to_click = self.find_elements(*self.THUMBNAIL_IMAGES_MOBILE)[i]
            image_to_click.click()




