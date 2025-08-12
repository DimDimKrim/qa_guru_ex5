import os
import sys
import pytest
from selene import browser, be, have
from pages.registration_page import RegistrationPage
from users import User


def test_form_submission():
    registration_page = RegistrationPage()
    ivan = User(first_name='Иван',
                 last_name='Иванов',
                 email='ivanov12@gmail.pom',
                 gender="Male",
                 phone_number='7788995511',
                 birthday=('August', '1995', '5'),
                 first_subject='Maths',
                 second_subject=('p', 'Physics'),
                 hobby="Reading",
                 file_name='textfile.txt',
                 address='ул. Пушкина д.Колотушкина',
                 user_location=('Haryana', 'Panipat')
                 )

    registration_page.open()
    registration_page.register(ivan)
    registration_page.should_have_registered(ivan)
    print('test finished')
