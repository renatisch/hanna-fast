from fastapi import FastAPI
from models import Person, PersonPatch
import json, random
from utils import update_profile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is your maing route"}


# lists people: all or sorted by name/city
@app.get("/people/")
def list_people(name: str | None = None, city: str | None = None):
    people = []
    with open("people.json", "r") as data:
        profiles = json.loads(data.read())
        if name or city:
            for each in profiles:
                profile = Person(**each)
                if profile.city == city or profile.name == name:
                    people.append(profile)
            return people
    return profiles


@app.get("/people/{id}")
def get_person(id: int):
    people = []
    with open("people.json", "r") as data:
        profiles = json.loads(data.read())
        for each in profiles:
            profile = Person(**each)
            if profile.id == id:
                return profile
    return {"message": "The profile with given id is not found"}


@app.delete("/people/{id}")
def delete_person(id: int):
    updated_profiles = []
    with open("people.json", "r") as data:
        profiles = json.loads(data.read())
        for each in profiles:
            profile = Person(**each)
            if profile.id == id:
                continue
            updated_profiles.append(profile.model_dump())
    with open("people.json", "w") as data:
        data.write(json.dumps(updated_profiles))
    return {"status": "deleted"}


# Create person
@app.post("/people/")
def create_person(person: Person):
    person.id = random.randint(50, 200)
    with open("people.json", "r") as data:
        profiles = json.loads(data.read())
    profiles.append(person.model_dump())
    with open("people.json", "w") as data:
        data.write(json.dumps(profiles))
    return person


@app.put("/people/{id}")
def update_person(id: int, person: Person):
    updated_profiles = []
    updated_profile = {}
    with open("people.json", "r") as data:
        profiles = json.loads(data.read())
        for each in profiles:
            if each["id"] == id:
                profile = update_profile(each, person=person)
                updated_profile = profile
                updated_profiles.append(profile)
                continue
            updated_profiles.append(each)
    with open("people.json", "w") as data:
        data.write(json.dumps(updated_profiles))
    return updated_profile


@app.patch("/people/{id}")
def update_person(id: int, person: PersonPatch):
    updated_profiles = []
    updated_profile = {}
    with open("people.json", "r") as data:
        profiles = json.loads(data.read())
        for each in profiles:
            if each["id"] == id:
                each.update(person.model_dump(exclude_unset=True))
                updated_profile = each
            updated_profiles.append(each)
    with open("people.json", "w") as data:
        data.write(json.dumps(updated_profiles))
    return updated_profile
