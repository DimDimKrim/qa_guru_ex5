
from selene import browser, have, be, by
import resource

class RegistrationPage:
    # функция открывает страницу
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.execute_script('window.scrollBy(0, 500)')
        return self

    # функция заполняет имя
    def fill_first_name(self, value):
        browser.element('[id="firstName"]').should(be.visible).type(value)
        return self

    # Заполнение графы Фамилия
    def fill_second_name(self, value):
        browser.element('[id="lastName"]').should(be.visible).type(value)
        return self

    # Заполнение графы почты
    def fill_email(self, value):
        browser.element('[id="userEmail"]').should(be.visible).type(value)
        return self

    # Выбор радиокнопки пола
    def gender_button(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()
        return self

    # Заполнение графы телефон
    def phone_number(self, value):
        browser.element('[id="userNumber"]').should(be.visible).type(value)
        return self

    # Выбор даты рождения
    def day_of_birth(self, month, year, day):
        browser.element('[id = "dateOfBirthInput"]').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.all('.react-datepicker__year-select option').element_by(have.exact_text(year)).click()
        browser.all(f'.react-datepicker__day:not(.react-datepicker__day--outside-month)').element_by(
            have.exact_text(str(int(day)))).click()
        return self

    #Выбор Subjects
    def subject_fill(self, value):
        browser.element('#subjectsInput').should(be.visible).type(value).press_enter()
        return self

    # Выбор хобби
    def hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    # Загрузка файла
    def download_file(self, value):
        browser.element('[id = "uploadPicture"]').should(be.visible).send_keys(resource.image_path(value))
        return self

    # Заполнение адреса
    def fill_adress(self, value):
        browser.element('[id="currentAddress"]').should(be.visible).type(value)
        return self

    # Выбор локации
    def choose_location(self, state, city):
        browser.element('#state input').type(state).press_enter()
        browser.element('#city input').type(city).press_enter()
        return self

    # Выбор города
    def choose_city(self, city):
        browser.element('[id="city"]').should(be.visible).click()
        browser.element('[id="react-select-4-input"]').type(city).press_enter()
        return self

    # Отправка формы
    def submit_form(self):
        browser.element('[id="submit"]').click()
        return self

    # Проверка формы
    def should_have_registered_user_with(self,
                                         full_name,
                                         email,
                                         gender,
                                         phone_number,
                                         birthday,
                                         subjects,
                                         hobby,
                                         file_name,
                                         address,
                                         state_city):
        (browser.all('tbody tr td:nth-child(2)')
        .should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            birthday,
            subjects,
            hobby,
            file_name,
            address,
            state_city
        )))
        return self