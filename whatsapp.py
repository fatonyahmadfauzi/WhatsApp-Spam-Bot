import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Buka WhatsApp Web
driver.get('https://web.whatsapp.com/')
print("\n\nScan QR code lalu tekan ENTER setelah berhasil login...")
input('Press ENTER after scanning QR code...')

# Ambil input dari user
name = input('Enter the name of user or group: ')
msg_source = input('Use clipboard for message? (Y/N): ').strip().upper()
count = int(input('Enter how many times to send the message: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').strip().upper()

# Cari dan klik chat
try:
    user = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, f'//span[@title="{name}"]'))
    )
    user.click()
except Exception as e:
    print(f"[!] Error: {e}")
    driver.quit()
    exit()

time.sleep(2)

# Fungsi kirim pesan
def send_message(content):
    try:
        msg_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "_ak1r")]//div[@role="textbox"]'))
        )
        
        # Paste atau ketik manual
        if msg_source == 'Y':
            pyperclip.copy(content)
            msg_box.click()
            msg_box.send_keys(Keys.CONTROL, 'v')
        else:
            msg_box.send_keys(content)
        
        time.sleep(0.5)
        
        # Kirim pesan
        send_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[.//span[@data-icon="send"]]'))
        )
        send_button.click()
        
    except Exception as e:
        print(f"[!] Send error: {e}")

# Loop pengiriman pesan
for i in range(count):
    try:
        # Format pesan
        timestamp = datetime.now().strftime("%I:%M %p").lstrip("0")
        base_content = pyperclip.paste() if msg_source == 'Y' else msg
        final_content = f"<Status: {i+1}/{count}> {base_content}\n{timestamp}" if bot_prompt == 'Y' else base_content
        
        send_message(final_content)
        print(f"Sent message {i+1}/{count}")
        time.sleep(gap)
        
    except Exception as e:
        print(f"[!] Loop error: {e}")

print("All messages sent! Closing in 10 seconds...")
time.sleep(10)
driver.quit()