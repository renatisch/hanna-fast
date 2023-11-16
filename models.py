from pydantic import BaseModel


class Person(BaseModel):
    id: int | None = None
    name: str
    surname: str
    position: str
    company: str
    city: str
    country: str
    is_active: bool


class PersonPatch(BaseModel):
    id: int | None = None
    name: str | None = None
    surname: str | None = None
    position: str | None = None
    company: str | None = None
    city: str | None = None
    country: str | None = None
    is_active: bool | None = None
