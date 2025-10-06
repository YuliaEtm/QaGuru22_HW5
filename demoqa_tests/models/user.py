from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List


class Gender(str, Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(str, Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone: str
    birth_date: date
    subjects: str
    hobbies: Hobby
    picture: str = ''
    address: str = ''
    state: str = ''
    city: str = ''



    @property
    def birthday_result(self) -> str:
        months = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
        return f'{self.birth_date.day} {months[self.birth_date.month - 4]},{self.birth_date.year}'
