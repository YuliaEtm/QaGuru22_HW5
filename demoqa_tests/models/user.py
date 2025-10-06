from dataclasses import dataclass
from datetime import date
from enum import Enum


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
