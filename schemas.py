from pydantic import BaseModel
from typing import Annotated,Optional
from pydantic.functional_validators import AfterValidator
from datetime import datetime



def validate_year(year:int):
    assert year <=datetime.now().year and year > 1700, f'Invalid year'
    return year

ValidDate=Annotated[int,AfterValidator(validate_year)]

class BookSchema(BaseModel):
    id:int
    title:str
    author:str
    published_year:ValidDate

class CreateBookSchema(BaseModel):
    title:str
    author:str
    published_year:ValidDate


class UpdateBookSchema(BaseModel):
    title:Optional[str]
    author:Optional[str]
    published_year:Optional[ValidDate]