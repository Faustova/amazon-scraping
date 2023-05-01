from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
# Replace these values with your own
#url = 'https://www.amazon.com/Tress-Wellness-Digital-Display-Sensitive/dp/B07CRZQ9MY?ref_=ast_sto_dp&th=1'
#url = "https://www.amazon.com/Multiple-Formulas-Different-Brazilian-KoluaWax/dp/B07BC83ZCT/ref=sr_1_1?crid=K4M16BIFVVRU&keywords=B07BC83ZCT+kotamu&qid=1682601602&sprefix=b07bc83zct+kotamu%2Caps%2C152&sr=8-1"
#url = 'https://www.amazon.com/dp/B09D7GNWSS/ref=syn_sd_onsite_desktop_0?ie=UTF8&pd_rd_plhdr=t&th=1&psc=1'
#url = 'https://www.amazon.com/Fochst-Crystal-Hair-Eraser-Exfoliation/dp/B0BFHPFJM1/'
#url = 'https://www.amazon.com/Stanley-Quencher-FlowState-Stainless-Insulated/dp/B0BQZ9K23L?th=1'
#url = 'https://www.amazon.com/EveryDrop-Whirlpool-Refrigerator-Water-Filter/dp/B00UXG4WR8'
url = 'https://www.amazon.com/Tress-Wellness-Digital-Display-Sensitive/dp/B07CRZQ9MY'
zip_code = '12345'

# Set up the Selenium WebDriver (e.g., for Google Chrome)
driver = webdriver.Chrome()

# Navigate to the Amazon product page
driver.get(url)

# Find and click the "Select your address" link
select_your_address_link = driver.find_element(By.CSS_SELECTOR, 'a[id="nav-global-location-popover-link"]')
select_your_address_link.click()

# Wait for the zip code input field to appear
time.sleep(1)

# Find the zip code input field, enter the zip code
zip_code_input = driver.find_element(By.ID, 'GLUXZipUpdateInput')
zip_code_input.send_keys(zip_code)

# Find and click the "apply" button
apply_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][aria-labelledby="GLUXZipUpdate-announce"]')
apply_button.click()

# Wait for the "continue" button to appear
time.sleep(1)

# Find the "continue" button using JavaScript and click it
continue_button = driver.find_element(By.XPATH, '//span[@id="GLUXConfirmClose-announce"]')
driver.execute_script("arguments[0].click();", continue_button)

# Wait for the page to update
time.sleep(1)

# ... Previous Selenium code ...

# Get the page HTML source
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the price span element using a more general approach
price_span = soup.find('span', {'data-a-size': 'xl', 'data-a-color': 'base'})

if price_span is not None:
    # Extract the price value as a string
    price_value = price_span.find('span', class_='a-offscreen').text

    # Remove the dollar sign and convert the price to a float
    price = float(price_value.replace('$', ''))

    print(price)
else:
    print("Price not found")

# Find the coupon label element
coupon_label = soup.find('label', {'id': lambda id: id and id.startswith('couponText')})

if coupon_label is not None:
    # Extract the coupon value as a string
    coupon_value_str = coupon_label.text.strip()
    
    # Extract the dollar value from the string
    match = re.search(r'\$\d+', coupon_value_str)
    
    if match:
        coupon_value = float(match.group(0).replace('$', ''))
        print(f"Coupon value: ${coupon_value:.2f}")
    else:
        print("Coupon value not found")
else:
    print("Coupon not found")


# Find the best seller badge element
best_seller_badge = soup.find('i', {'class': 'p13n-best-seller-badge'})

if best_seller_badge is not None:
    print("Best Seller badge found:", best_seller_badge.text.strip())
else:
    print("Best Seller badge not found")


# Find the "Amazon's Choice" badge
amazon_choice_badge = soup.find('span', {'class': 'ac-badge-rectangle'})

if amazon_choice_badge:
    print("Amazon's Choice badge found.")
else:
    print("Amazon's Choice badge not found.")


# Find the "Deal" badge
deal_badge = soup.find('span', {'class': 'dealBadgeSupportingText'})

if deal_badge:
    print("Deal badge found.")
else:
    print("Deal badge not found.")

# Find the deal value
deal_value = soup.find('span', {'class': 'savingPriceOverride'})

if deal_value:
    print(f"Deal value found: {deal_value.text.strip()}")
else:
    print("Deal value not found.")


# Continue with other actions or close the WebDriver
driver.quit()


# coupon
# title
# rating
# review_count

## OK
# best seller

