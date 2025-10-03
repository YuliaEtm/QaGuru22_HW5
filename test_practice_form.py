import time

from selene import browser, be, have
from selenium.webdriver.chrome.options import Options
import os


def test_submitting_the_form(browser_settings):

    browser.open("/automation-practice-form")
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivanov235@yandex.ru')

    browser.element('label[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('97891234567')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="5"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1995"]').click()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').type('Physics').press_enter()

    browser.element('label[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').set_value(os.path.abspath('sostavlennaa-kniga-i-doska.jpg'))

    browser.element('#currentAddress').type('Lenina str')

    browser.element('#state').click()
    browser.all('div[class*="option"]').element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.all('div[class*="option"]').element_by(have.text('Noida')).click()

    browser.element('#submit').click()

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))


    browser.element('.modal-content').should(be.visible)
    browser.all('td').should(have.texts([
        'Student Name', 'Ivan Ivanov',
        'Student Email', 'Ivanov235@yandex.ru',
        'Gender', 'Male',
        'Mobile', '9789123456',
        'Date of Birth', '15 June,1995',
        'Subjects', 'Physics',
        'Hobbies', 'Reading',
        'Picture', 'sostavlennaa-kniga-i-doska.jpg',
        'Address', 'Lenina str',
        'State and City', 'NCR Noida'
    ]))

