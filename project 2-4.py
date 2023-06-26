from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# Инициализация драйвера браузера
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    # Открыть страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидание, пока цена не станет равной $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решить математическую задачу
    input_value = browser.find_element(By.ID, "input_value").text
    result = str(math.log(abs(12*math.sin(int(input_value)))))

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получить результат
    alert = browser.switch_to.alert
    result_text = alert.text.split()[-1]
    print(f"Результат: {result_text}")

finally:
    # Закрыть браузер
    browser.quit()
