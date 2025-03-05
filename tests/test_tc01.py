import pytest
from pytest_bdd import given, scenarios, when
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

scenarios("../features/tc01.feature")


@pytest.fixture
def setup():

    options = AppiumOptions()
    options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "Android Emulator",
    "appium:app": "C:\\Users\\HarishPremkumar\\Python_Appium_Framework_Developement\\tests\\Android-MyDemoAppRN.1.1.0.build-226.apk",
    "appium:automationName": "UiAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
    driver = webdriver.Remte("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()


@given('I am logged into the Saucelabs application on a mobile device')
def test_login_into_saucelabs_app(setup):
    driver = setup
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='open menu']"))
    )
    driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='open menu']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Log In']"))
    )
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Log In']").click()
    # driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Username input field']"))
    )
    username = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Username input field']")
    password = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password input field']")
    login_button = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Login button']")  
    username.send_keys("bob@example.com")
    password.send_keys("10203040")
    login_button.click()
    time.sleep(3)
    screenshot_path = "screenshot_after_click.png"
    driver.save_screenshot(screenshot_path)








