"""
Basic example showing how to read and validate data from a file using Pydantic
"""

import json
import pydantic
from typing import Optional, List


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing"""

    def __init__(self, title:str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBNFormatError(Exception):
    """Custom error that is raised when ISBN10 doesnt have the right format."""
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):

    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        """Make sure there is either an ISBN10 or ISBN13 in the json"""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(title=values["title"], message="Document should have "
                                                                  "either an ISBN10 or ISBN13")
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value):
        """Validator to check if 1SBN10 has a valid value"""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBNFormatError(value= value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        weighted_sum = sum((10-i)*char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBNFormatError(value= value, message="ISBN10 should be divisible by 11")
        return value

    class Config:
        """Pydantic config class"""

        allow_mutation = False
        anystr_lower = True


def main() -> None:
    """ Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        # books[0].title = "New name"
        # print(books[0].dict(include={"title"}))
        # print(books[0].dict())
        print(books[0].copy(deep=True))


if __name__ == "__main__":
    main()