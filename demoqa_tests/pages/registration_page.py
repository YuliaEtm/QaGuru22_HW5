from selene import browser, have, be, command

from demoqa_tests import resource
from datetime import date

from demoqa_tests.data.student import student


class RegistrationPage:
    def __init__(self):
    #self.panel = SubmittingFormPage()

        self._first_name = browser.element('#firstName')
        self._last_name = browser.element('#lastName')
        self._email = browser.element('#userEmail')
        self._number = browser.element('#userNumber')
        self._upload = browser.element('#uploadPicture')
        self._address = browser.element('#currentAddress')
        self._subjects = browser.element('#subjectsInput')

        # self._gender_male = browser.element('label[for="gender-radio-1"]')
        # self._gender_female = browser.element('label[for="gender-radio-2"]')
        # self._gender_other = browser.element('label[for="gender-radio-3"]')
        #
        self._birth_input = browser.element('#dateOfBirthInput')
        self._birth_year_select = browser.element('.react-datepicker__year-select')
        self._birth_month_select = browser.element('.react-datepicker__month-select')



    # self._subjects_box = browser.element('#subjectsContainer')
    # self._subjects_input = browser.element('#subjectsInput')
    #
    # self._hobby_sports = browser.element('label[for="hobbies-checkbox-1"]')
    # self._hobby_reading = browser.element('label[for="hobbies-checkbox-2"]')
    # self._hobby_music = browser.element('label[for="hobbies-checkbox-3"]')
    #
    #
    #
        self._state = browser.element('#state')
        self._all = browser.all('div[class*="option"]')

        self._city = browser.element('#city')

    #
        self._submit = browser.element('#submit')
    #
    # self._genders = {
    #     'Male': self._gender_male,
    #     'Female': self._gender_female,
    #     'Other': self._gender_other,
    # }
        self._hobbies = {
            'Sports': browser.element('label[for="hobbies-checkbox-1"]'),
            'Reading': browser.element('label[for="hobbies-checkbox-2"]'),
            'Music': browser.element('label[for="hobbies-checkbox-3"]')
            }

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def fill_first_name(self, value):
        self._first_name.type(value)
        return self

    def fill_last_name(self, value):
        self._last_name.type(value)
        return self

    def fill_email(self, value):
        self._email.type(value)
        return self

    def fill_user_number(self, value):
        self._number.type(value)
        return self

    def upload_file(self, value):
        self._upload.set_value(resource.pash(value))
        return self

    def fill_gender(self, value):
        browser.element(
            {'Male': 'label[for="gender-radio-1"]',
             'Female': 'label[for="gender-radio-2"]',
             'Other': 'label[for="gender-radio-3"]'}[value]
            ).click()
        return self

    def birthday(self, data):
        self._birth_input.click()
        self._birth_month_select.type(data.month)

        self._birth_year_select.type(data.year)

        browser.element(f'.react-datepicker__day--0{data.day}').click()
        return self

    def subjects(self, value):
        self._subjects.type(value).press_enter()
        return self

    def hobbies(self, value):
        self._hobbies[value].click()
        return self

    def fill_address(self, value):
        self._address.type(value)
        return self

    def fill_state(self, value):
        self._state.perform(command.js.scroll_into_view)
        self._state.click()
        self._all.element_by(have.text(value)).click()
        return self

    def fill_city(self, value):
        self._city.click()
        self._all.element_by(have.text(value)).click()
        return self

    def click_submit(self):
        self._submit.click()
        return self

    def register(self):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.fill_gender(student.gender)
        self.fill_user_number(student.phone)
        self.birthday(student.birth_date)
        self.subjects(student.subjects)
        self.hobbies(student.hobbies)
        self.upload_file(student.picture)
        self.fill_address(student.address)
        self.fill_state(student.state)
        self.fill_city(student.city)
        self.click_submit()
        return self

    def should_registered_user_data(self):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-content').should(be.visible)

        browser.element('.table').all('td').even.should(have.exact_texts(
                 f'{student.first_name} {student.last_name}',
                 student.email,
                 student.gender.value,
                 '9789123456',
                 '15 October,1995',
                 student.subjects,
                 student.hobbies.value,
                 student.picture,
                 student.address,
                 f'{student.state} {student.city}'
            ))

        return self






