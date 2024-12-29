import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# каждый тест должен начинаться с test_
def test_positive_login():
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    chrome_options.add_argument("--disable-search-engine-choice-screen") # отключаем выбор движка для поиска
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://pokemonbattle-stage.ru/"
    driver.get(url=url)
		
		# ищем по селектору инпут "Email", кликаем по нему и вводим значение email
    email = WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class*="f_email"]')))
    email.click()
    email.send_keys('email') # тут email своего тестового аккаунта на stage окружении
		
		# ищем по селектору инпут "Password", кликаем по нему и вводим значение пароля
    password = driver.find_element(by=By.CSS_SELECTOR, value='[class*="f_pass"]')
    password.click()
    password.send_keys('password') # тут пароль своего тестового аккаунта на stage окружении
		
		# ищем по селектору кнопку "Войти" и кликаем по ней
    enter = driver.find_element(by=By.CSS_SELECTOR, value='[class*="send_auth"]')
    enter.click()
    
    # ждем успешного входа и обновления страницы
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.url_to_be('https://pokemonbattle-stage.ru/'))
		
		# ищем элемент на странице, который содержит ID тренера
    trainer_id = driver.find_element(by=By.CLASS_NAME, value='header__id-texts')
		
		# сравниваем полученный ID из кода теста с ID вашего тестового тренера
    assert trainer_id.text.replace('\n', ': ') == 'ID: 1363', 'Unexpected ID trainer' # введи тут ID своего тренера
    
