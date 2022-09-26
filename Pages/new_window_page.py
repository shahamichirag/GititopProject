from Pages.base_page import Page


class Window(Page):

    def facebook_page_opened(self):
        self.verify_url_contains_query('facebook')
        assert 'facebook' in self.driver.current_url, f'not in {self.driver.current_url}'

    def close_window(self):
        self.driver.close()
