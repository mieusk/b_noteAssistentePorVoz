import pyttsx3, speech_recognition as sr, datetime, os, shutil

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', 'brazil')

diretorioAtual = os.getcwd()
options = Options()
options.binary_location = "{}\\chrome.exe".format(diretorioAtual)
options.add_extension('{}\\cmedhionkhpnakcndndgjdbohmhepckk.zip'.format(diretorioAtual))
driver = webdriver.Chrome(options=options, executable_path="{}\\chromedriver.exe".format(diretorioAtual))
driver.set_window_position(-10000, -10000)
driver.get('https://www.youtube.com')
youtube = driver.current_window_handle

def fale(audio):
	engine.say(audio)
	engine.runAndWait()

def inicio():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		fale('Bom dia, minhe linde!')

	elif hour>= 12 and hour<18:
		fale('Boa tarde, minhe linde!')  

	else:
		fale('Boa noite, minhe linde!')

	columns = shutil.get_terminal_size().columns
	print('#####################'.center(columns))
	print('Bem-vinde, minhe linde.'.center(columns))
	print('#####################'.center(columns))
	fale('Diga seu comando')
 
def ouvir():
	 
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
		print("Não reconheci.") 
		return "None"
	 
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()
	inicio()
	if EC.number_of_windows_to_be(2):
		driver.switch_to.window(youtube)

	while True:
		query = ouvir().lower()
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
				fale("Tocando.")
				element.click()
 
			elif 'hora' in query2:
				strTime = datetime.datetime.now().strftime("%H:%M")   
				fale(f"São {strTime} horas.")

			elif 'para' in query2 or 'parar' in query2 or 'silêncio' in query2:
				element = driver.find_element(By.XPATH, "//*[@class='style-scope ytd-logo']")
				element.click()
			
			else:
				fale('Não posso ajudar.')
