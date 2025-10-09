
from demoqa_tests.pages.registration_page import RegistrationPage


def test_submitting_the_form(browser_settings):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.remove_banners()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('Ivanov235@yandex.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_user_number('9789123456')
    registration_page.birthday('1995', 'June', '15')
    registration_page.subjects('Physics')
    registration_page.hobbies('Reading')
    registration_page.upload_file('sostavlennaa-kniga-i-doska.jpg')
    registration_page.fill_address('Lenina str')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Noida')
    registration_page.click_submit()
    registration_page.should_registered_user_data()
