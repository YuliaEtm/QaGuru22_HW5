import time

from selene import browser, have

from demoqa_tests import resource
from demoqa_tests.pages.registration_page import RegistrationPage


def test_submitting_the_form(browser_settings):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register()
    registration_page.should_registered_user_data()

