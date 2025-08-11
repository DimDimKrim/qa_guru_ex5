import os
import sys
import pytest
from selene import browser, be, have
from pages.registration_page import RegistrationPage



def test_fill_form():
    registration_page = RegistrationPage()

    registration_page.open()
    (
    registration_page
    .fill_first_name('Иванов')
    .fill_second_name('Иван')
    .fill_email('ivanov12@gmail.pom')
    .gender_button("Male")
    .phone_number('7788995511')
    .day_of_birth('August', '1995', '1')
    .subject_fill('Maths')
    .hobby("Reading")
    .download_file('textfile.txt')
    .fill_adress('ул.Пушкина д.Колотушкина 19147')
    .choose_location('Haryana', 'Panipat')
    .submit_form()
    )

    registration_page.should_have_registered_user_with(
    'Иванов Иван',
    'ivanov12@gmail.pom',
    'Male',
    '7788995511',
    '01 August,1995',
    'Maths',
    'Reading',
    'textfile.txt',
    'ул.Пушкина д.Колотушкина 19147',
    'Haryana Panipat'
    )
    print('test successful')
    # breakpoint()
