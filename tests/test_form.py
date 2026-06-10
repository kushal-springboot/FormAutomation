from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():

    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/text-box")

    driver.find_element(By.ID, "userName").send_keys("Kushal")

    driver.find_element(By.ID, "userEmail").send_keys("kushal@gmail.com")

    submit_btn = driver.find_element(By.ID, "submit")

    driver.execute_script(
        "arguments[0].scrollIntoView();",
        submit_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        submit_btn
    )

    driver.quit()