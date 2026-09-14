from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    TO_READ = "to-read"
    CURRENTLY_READING = "currently-reading"
    READ = "read"

@dataclass
class Book:
    title: str
    author: str
    status: Status = Status.TO_READ