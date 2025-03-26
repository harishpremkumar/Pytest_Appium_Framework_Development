import pytest
from pytest_bdd import scenarios, given, when
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

scenarios("../features/tc01.feature")  # Make sure the path to your feature file is correct


@pytest.fixture
def setup():
    # Initialize Appium options and driver
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "Android Emulator",
        "appium:app": "C:\\Users\\HarishPremkumar\\Python_Appium_Framework_Developement\\Config\\Android-MyDemoAppRN.1.1.0.build-226.apk",
        "appium:automationName": "UiAutomator2",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()





@given('I am logged into the Saucelabs application on a mobile device')
def login_into_saucelabs_app(setup):
    driver = setup
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='open menu']"))
    )
    driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='open menu']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Log In']"))
    )
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Log In']").click()

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
    print("Credential Step is filling.")
    


@when("I am added Saucelabs Backpacks and update the quantity 1 as 5")
def add_product(setup):
    driver = setup
    
    try:
        # Wait for the "Sauce Labs Backpack" product to be clickable
        product_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@content-desc='store item text' and @text='Sauce Labs Backpack']"))
        )
        
        # Check if the product is displayed and clickable
        if product_element.is_displayed():
            print("Sauce Labs Backpack found and is clickable!")
            product_element.click()
            time.sleep(2)   # Wait for the product page to load
            
            # Find the "+" button to increase quantity
            plus_button = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='counter plus button']")  # Adjust the locator
            
            # Find the quantity element, which has text "1"
            quantity_element = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='1']")  # Quantity XPath
            
            current_quantity = int(quantity_element.text)
            print(f"Current quantity: {current_quantity}")
            
            # Loop to click the "+" button until the quantity reaches 5
            while current_quantity < 5:
                print(f"Current quantity is {current_quantity}. Clicking '+' to increase quantity.")
                plus_button.click()
                time.sleep(2)  # Wait for the UI to update
                
                # Re-check the quantity after clicking the "+" button
                quantity_element = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='" + str(current_quantity + 1) + "']")  # Update XPath with the new quantity
                current_quantity = int(quantity_element.text)
                
                # If quantity reaches 5, break the loop
                if current_quantity == 5:
                    print("Quantity has reached 5. Exiting the program.")
                    quantity_amount_text = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='product price']").text
                    price1 = float(quantity_amount_text.replace('$', ''))
                    driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Add To Cart button']").click()
                    print(price1)
                    driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='cart badge']").click()
                    Total_quantity_amount = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='total price']").text
                    price2 = float(Total_quantity_amount.replace('$', ''))
                    if price1 == price2:
                        time.sleep(3)
                        driver.close()
                        print("Product Step is running.")
                        
            # If after 5 clicks the quantity hasn't reached 5, exit the program
            if current_quantity != 5:
                print(f"Quantity did not reach 5, exiting the program.")
        else:
            print("The product 'Sauce Labs Backpack' is not visible or clickable.")
    
    except Exception as e:
        # Handle errors such as element not found or clickable
        print(f"An error occurred: {e}")
