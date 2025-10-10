from datetime import date
from demoqa_tests.models.user import User, Gender, Hobby

# Пользователь для тестов
student = User(
    first_name='Ivan',
    last_name='Ivanov',
    email='Ivanov235@yandex.ru',
    gender=Gender.male,
    phone='9789123456',
    birth_date=date(1995, 8, 15),
    subjects='Physics',
    hobbies=Hobby.reading,
    picture='sostavlennaa-kniga-i-doska.jpg',
    address='Lenina str',
    state='NCR',
    city='Noida')
