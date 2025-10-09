from demoqa_tests.data.student import student
from demoqa_tests.pages.registration_page import RegistrationPage
import calendar


def test_submitting_the_form(browser_settings):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.remove_banners()
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.fill_email(student.email)
    registration_page.fill_gender(student.gender)
    registration_page.fill_user_number(student.phone)
    registration_page.birthday(student.birth_date.year, calendar.month_name[student.birth_date.month],
                               student.birth_date.day)
    registration_page.subjects(student.subjects)
    registration_page.hobbies(student.hobbies)
    registration_page.upload_file(student.picture)
    registration_page.fill_address(student.address)
    registration_page.fill_state(student.state)
    registration_page.fill_city(student.city)
    registration_page.click_submit()
    registration_page.should_registered_user_data()
