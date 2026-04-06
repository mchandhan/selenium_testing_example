import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List of unique names for testing
names = [
    "Abhay", "Alok", "Amrita", "Anmol", "Archana",
    "Ashwin", "Avantika", "Balaji", "Bhavesh", "Chandni"
]



def fill_form():
    # Setup Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Uncomment if you don't want a window to open
    
    # Initialize the driver using WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        # Loop for multiple submissions
        for i in range(10):
            # REPLACE WITH YOUR ACTUAL FORM URL
            driver.get("https://forms.gle/RjtPWNhc82fWn4EVA")
            time.sleep(2)  # Wait for initial load
            
            try:
                # 1. Fill Name/Text Inputs
                # Google forms typically use a specific class for the text input field
                text_inputs = driver.find_elements(By.XPATH, '//input[@type="text"]')
                for text_box in text_inputs:
                    text_box.send_keys(names[i % len(names)])  # Use names in a loop to ensure uniqueness
                    time.sleep(0.3) # Short delay for stability

                # 2. Select Random Radio Buttons
                # Your HTML shows radio groups are contained in divs with role="radiogroup" 
                # Each individual option has role="radio" and a data-value 
                radio_groups = driver.find_elements(By.XPATH, '//div[@role="radiogroup"]')
                
                for group in radio_groups:
                    # Find all clickable radio options within this specific question group
                    options = group.find_elements(By.XPATH, './/div[@role="radio"]')
                    if options:
                        choice = random.choice(options)
                        # Scroll to element to ensure it is clickable
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", choice)
                        choice.click()
                        time.sleep(0.3) # Short delay for stability

                # 3. Submit
                # Google Forms submit buttons usually have a span with text "Submit" [cite: 47]
                submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Submit")]')))
                submit_button.click()
                
                print(f"Submission {i+1} completed.")
                
                # Wait for the "response recorded" page before starting next loop
                wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Your response has been recorded")]')))
                time.sleep(1)
                
            except Exception as e:
                print(f"Error on submission {i+1}: {e}")
                continue # Try next submission if one fails

    finally:
        driver.quit()

if __name__ == "__main__":
    fill_form()
