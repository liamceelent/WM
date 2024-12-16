from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


# Path to ChromeDriver (use the correct path for your setup)
chrome_driver_path = r'C:\Program Files (x86)\chrome.exe'  # Correct path

def loginSalesforce(driver):
    # Initialize the ChromeDriver
    # Launch the website
    driver.get("https://intergraph-ppm.lightning.force.com/lightning/o/Case/list?filterName=Copy_of_SC_EAM_Support_ALL")

    time.sleep(3)

    login_button = driver.find_element(By.XPATH, "//button[contains(@onclick, 'IdpOptions.useIdp')]")

    # Click the button
    login_button.click()
    time.sleep(3)

    email_input = driver.find_element(By.ID, "i0116")

    email_input.send_keys("liam.ceelen-thomas@hexagon.com")  # Replace with the desired text

    next_button = driver.find_element(By.ID, "idSIButton9")

    # Click the "Next" button
    next_button.click()

    time.sleep(3)

    # Enter password
    password_input = driver.find_element(By.ID, "i0118")
    password_input.send_keys("Bandit02Bandit02!!")

    sign_in_button = driver.find_element(By.ID, "idSIButton9")
    sign_in_button.click()
    print("Sign In button clicked!")

    time.sleep(3)

    element = driver.find_element(By.XPATH, "//div[contains(text(), 'Text +XX XXXXXXXX91')]")
    element.click()

    time.sleep(3)

    code_input = driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC")  # Locate the code input field by ID
    code = input("Please supply code: ")  # Prompt user to enter the code
    code_input.send_keys(code)  # Send the code to the input field


    verify_button = driver.find_element(By.ID, "idSubmit_SAOTCC_Continue")
    verify_button.click()
    print("Verify button clicked!")

    time.sleep(3)

    yes_button = driver.find_element(By.ID, "idSIButton9")
    yes_button.click()

    time.sleep(3)


def navigateMenu(driver):
    cases_button = driver.find_element(By.XPATH, "//button[@title='Select a List View: Cases']")
    cases_button.click()
    time.sleep(3)


def navigateEAMSupport(driver):
    link_element = driver.find_element(By.XPATH, "//a[contains(@href, 'javascript:void(0);') and @role='option']//span[text()='SC: EAM Support']")
    link_element.click()
    time.sleep(3)

def navigateApacAll(driver):
    link_element = driver.find_element(By.XPATH, "//span[text()='apac - all']")
    # Click the button
    link_element.click()
    time.sleep(3)


def getAllOpenCases(driver):
    table_element = driver.find_element(By.XPATH, "//table[@role='grid' and contains(@class, 'slds-table')]")

    rows = table_element.find_elements(By.XPATH, ".//tr")

    # Iterate through rows and extract cell data
    for row_index, row in enumerate(rows):
        # Get all cells in the current row (both <td> and <th>)
        cells = row.find_elements(By.XPATH, ".//td | .//th")
        
        print(f"Row {row_index + 1}:")
        for cell_index, cell in enumerate(cells):
            print(f"    Cell {cell_index + 1}: {cell.text}")
    time.sleep(3)

def __main__():
    driver = webdriver.Chrome()
    loginSalesforce(driver)
    navigateMenu(driver)
    navigateEAMSupport(driver)
    getAllOpenCases(driver)
    navigateMenu(driver)
    navigateApacAll(driver)
    getAllOpenCases(driver)
    time.sleep(1000)
    driver.quit()

if __name__ == "__main__":
    __main__()