from selene import browser, be, have
import os
image_path = os.path.abspath("textfile.txt")

def test_fill_form():
    #Заполнение графы Имя
    browser.element('[id="firstName"]').should(be.visible).type("Иван")
    #Заполнение графы Фамилия
    browser.element('[id="lastName"]').should(be.visible).type("Иванов")
    #Заполнение графы почты
    browser.element('[id="userEmail"]').should(be.visible).type("ivanov22@gmail.com")
    #Выбор радиокнопки
    browser.element('label[for="gender-radio-1"]').click()
    #Заполнение графы телефон
    browser.element('[id="userNumber"]').should(be.visible).type("89098887678")
    #Выбор даты рождения
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__day--021').should(be.visible).click()
    #Выбор Subjects
    browser.element('#subjectsInput').should(be.visible).type('Maths').press_enter()
    #Выбор хобби
    browser.element('label[for ="hobbies-checkbox-1"]').click()
    #Загрузка файла
    browser.element('[id = "uploadPicture"]').should(be.visible).send_keys(image_path)
    #Заполнение адреса
    browser.element('[id="currentAddress"]').should(be.visible).type("ул.Пушкина д.Колотушкина кв.3")
    #Выбор штата
    browser.element('[id="state"]').should(be.visible).click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    #Выбор города
    browser.element('[id="city"]').should(be.visible).click()
    browser.element('[id="react-select-4-input"]').type('Delhi').press_enter()
    #Отправка формы
    browser.element('#submit').click()
    #browser.element('[id="submit"]').should(be.visible).click()
    #Проверка отправки формы
    browser.element('[id="example-modal-sizes-title-lg"]').should(be.visible).should(have.text('Thanks for submitting the form'))



