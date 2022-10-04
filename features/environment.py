from selenium import webdriver
from app.application import Application
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver import Chrome
#from selenium.webdriver.chrome.service import Service


def browser_init(context, test_name):

    """
    :param context: Behave context
    """

    # ALL BROWSER WITH EXECUTABLE PATH AS BELOW:
    #context.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # context.browser = webdriver.Safari()
    #context.driver = webdriver.Firefox(executable_path='./geckodriver.exe')
    #context.driver = webdriver.Firefox(executable_path='C:\\Users\\shaha\\OneDrive\\Desktop\\Gititop Project\\geckodriver.exe')

    #context.driver.maximize_window()
    #context.driver.implicitly_wait(4)
    #context.app = Application(context.driver)

    #ABOVE CODE ENDS HERE

    #Mobile emulation using chrome devtool protocol + selenium

    # context.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # context.driver.maximize_window()
    # set_device_metrics_override = dict({
    #     "width": 375,
    #     "height": 812,
    #     "deviceScaleFactor": 50,
    #     "mobile": True
    # })
    #
    # context.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', set_device_metrics_override)
    # context.driver.get("https://gettop.us/")
    # context.app = Application(context.driver)

    #ABOVE CODE FOR MOBILE EMULATION + CDP IS OVER HERE.

    #OTHER WAY TO RUN TEST CASES FOR MOBILE EMULATION USING CHROME BROWSER IS AS BELOW:
    #IMPORT SERVICE TO EXECUTE THIS CODE

    # options = webdriver.ChromeOptions()
    # service = Service('./chromedriver.exe')
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(chrome_options=options, service=service)
    # context.app = Application(context.driver)

    #ABOVE CODE ENDS HERE

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver.exe')
    # context.app = Application(context.driver)

    #ABOVE CODE FOR HEADLESS MODE IS OVER HERE

     #BROWSERSTACK CODE for cross browser testing
    # bs_user = 'amishah_TSPaqC'
    # bs_key = 'S4apnHKzZMFz9wd9kJwY'
    #
    # desired_cap = {
    #     "browserName": "Firefox",
    #     "browserVersion": "102.0",
    #     "os": "Windows",
    #     "osVersion": "10",
    #     'name': test_name''
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(5)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)

    #ABOVE CODE FOR BROWSER STACK FOR CROSS BROWSER TESTING IS OVER HERE

    # BROWSERSTACK CODE for mobile emulation
    # desired_cap = {
    #     "os_version": "16",
    #     "device": "iPhone 14"
    # }

    bs_user = 'amishah_TSPaqC'
    bs_key = 'S4apnHKzZMFz9wd9kJwY'

    desired_cap = {
        'bstack:options': {
            "osVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "realMobile": "true",
            "local": "false",
        },
    }
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

   #ABOVE CODE FOR MOBILE EMULATION+BROWSER STACK IS OVER HERE


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
