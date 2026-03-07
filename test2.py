from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains 

options = Options()
options.add_experimental_option("detach", True)  # Keeps browser open

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://mchandhan.github.io/portfolio/portfolio.html")
actions = ActionChains(driver)
element = driver.find_element(By.XPATH, "/html/body/section[1]/div/div[1]/a[2]")

actions.context_click(element).perform()  # Right-click on the element


input("Press Enter to close the browser...")

driver.quit()