import pyttsx3, speech_recognition as sr, datetime, os, shutil

from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', 'brazil')

options = Options()
options.binary_location = "C:/b/chrome.exe"

options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options, executable_path="C:/b/chromedriver.exe", )
driver.get('https://www.youtube.com')

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Bom dia, minhe linde!")

	elif hour>= 12 and hour<18:
		speak("Boa tarde, minhe linde!")  

	else:
		speak("Boa noite, minhe linde!")

 
def username():
	columns = shutil.get_terminal_size().columns
	print("#####################".center(columns))
	print("Bem-vinde, minhe linde.".center(columns))
	print("#####################".center(columns))
	 
	speak("Diga seu comando")
 
def takeCommand():
	 
	r = sr.Recognizer()
	 
	with sr.Microphone() as source:
		 
		print("Ouvindo...")
		r.pause_threshold = 1
		audio = r.listen(source)
  
	try:
		print("Reconhecendo...")   
		query = r.recognize_google(audio, language ='pt-br')
		print(f"Você disse: {query}\n")
  
	except Exception as e:
		print(e)   
		print("Não reconhecemos.") 
		return "None"
	 
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()
	wishMe()
	username()
	 
	while True:
		query = takeCommand().lower()
		if query.startswith('note'):
			query2 = query.replace('note', '')

			if 'tocar' in query2 or 'toca' in query2 or 'toque' in query2:
				element = driver.find_element_by_name('search_query')
				query22 = query2.replace('tocar', '').replace('note', '').replace('toca', '').replace('toque', '')
				element = element.send_keys(query22)
				element = driver.find_element(By.XPATH, "//*[@class='style-scope ytd-searchbox']")
				element.submit()
				element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='yt-simple-endpoint style-scope ytd-video-renderer']")))
				element = driver.find_element(By.XPATH, "//*[@class='yt-simple-endpoint style-scope ytd-video-renderer']")
				element.get_attribute('href')
				speak("Tocando.")
				element.click()
 
			elif 'hora' in query2:
				strTime = datetime.datetime.now().strftime("%H:%M")   
				speak(f"São {strTime} horas.")

			elif 'para' in query2 or 'parar' in query2 or 'silêncio' in query2:
				element = driver.find_element(By.XPATH, "//*[@class='style-scope ytd-logo']")
				element.click()
			
			else:
				speak('Não posso ajudar.')
