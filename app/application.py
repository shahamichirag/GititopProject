from Pages.header import Header
from Pages.search_result_page import Searchresult


class Application:
    def __init__(self,driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.search_result_page = Searchresult(self.driver)