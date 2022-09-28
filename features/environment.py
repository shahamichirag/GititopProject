from selenium import webdriver
from app.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver import Chrome
#from selenium.webdriver.chrome.service import Service



def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # context.browser = webdriver.Safari()
    #context.driver = webdriver.Firefox(executable_path='./geckodriver.exe')
    #context.driver = webdriver.Firefox(executable_path='C:\\Users\\shaha\\OneDrive\\Desktop\\Gititop Project\\geckodriver.exe')


    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    ## HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver.exe')
    context.app = Application(context.driver)


     #BROWSERSTACK CODE
    # bs_user = 'amishah_TSPaqC'
    # bs_key = 'S4apnHKzZMFz9wd9kJwY'
    #
    # desired_cap = {
    #     "browserName": "Firefox",
    #     "browserVersion": "102.0",
    #     "os": "Windows",
    #     "osVersion": "10",
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(5)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
