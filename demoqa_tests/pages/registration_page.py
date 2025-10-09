from selene import browser, have, be
import calendar
from demoqa_tests import resource
from demoqa_tests.data.student import student


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
        return self

    def remove_banners(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self, value):
        browser.element(
            {'Male': 'label[for="gender-radio-1"]',
             'Female': 'label[for="gender-radio-2"]',
             'Other': 'label[for="gender-radio-3"]'}[value]
        ).click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def hobbies(self, value):
        browser.element(
            {'Sports': 'label[for="hobbies-checkbox-1"]',
             'Reading': 'label[for="hobbies-checkbox-2"]',
             'Music': 'label[for="hobbies-checkbox-3"]'}[value]
        ).click()
        return self

    def upload_file(self, value):
        browser.element('#uploadPicture').set_value(resource.pash(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('div[class*="option"]').element_by(have.text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('div[class*="option"]').element_by(have.text(value)).click()
        return self

    def click_submit(self):
        browser.element("#submit").click()
        return self

    def should_registered_user_data(self):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-content').should(be.visible)

        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{student.first_name} {student.last_name}',
            student.email,
            student.gender.value,
            student.phone,
            f'{student.birth_date.day} {calendar.month_name[student.birth_date.month]},{student.birth_date.year}',
            student.subjects,
            student.hobbies.value,
            student.picture,
            student.address,
            f'{student.state} {student.city}'
        ))

        return self
