from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback
from flask import Flask
import threading 
app = Flask(__name__)
"""
export default {
      async fetch(request, env) {
        try {
          const { prompt } = await request.json();
          if (!prompt) {
            return new Response('Error: No prompt provided', { status: 400 });
          }    
          const inputs = {
            prompt: prompt,
          };    
          const response = await env.AI.run('@cf/stabilityai/stable-diffusion-xl-base-1.0', inputs);   
          if (response) {
            return new Response(response, {
              headers: {
                'Content-Type': 'image/png',
              },
            });
          }
          else {
            return new Response('Error: Image generation failed', { status: 500 });
          }
        } 
        catch (error) {
        return new Response('Error: ' + error.message, { status: 500 });}
  },
};
"""
@app.route('/')
def home():
    return "Bot is running!"
    
def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# Start the Flask server in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

print("Started Selenium Part -----")

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver,5)  # Increased timeout
    print("started the reloader -------")
    while True:
            print("entered loop......")
            driver.get('https://ace-nudity-detector.onrender.com/')
            form = WebDriverWait(driver, 5).until( EC.presence_of_element_located((By.XPATH, '//form[@id="dataForm"]')))
            id_input = form.find_element(By.XPATH, '//input[@id="id"]')            
            id_input.send_keys("id")
            name_input = form.find_element(By.XPATH, '//input[@id="name"]')            
            name_input.send_keys("Some_Random_Name")
            title_input = form.find_element(By.XPATH, '//input[@id="title"]')            
            title_input.send_keys("Some_Random_Title")
            submit = form.find_element(By.XPATH, '//button[@type="submit"]')
            submit.click()
            import time 
            time.sleep(300) #for every 5 minutes this cycle continues 
                                                                          
except Exception as e:
    print("e :",e) 
    