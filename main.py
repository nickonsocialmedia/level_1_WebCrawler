from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome options instance
options = webdriver.ChromeOptions()
# Setting the driver path and requesting a page
driver = webdriver.Chrome(options=options)

driver.get('http://luc.zietoshi.com')

# Wait for the page to load completely (adjust the timeout as needed)
wait = WebDriverWait(driver, 8)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Get the page source after it has fully loaded
page_source = driver.page_source

# Print the page source or do further processing
print(page_source)

# Close the browser when done
driver.quit()
