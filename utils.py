from main import Person


def update_profile(profile: dict, person: Person):
    profile["name"] = person.name
    profile["surname"] = person.surname
    profile["position"] = person.position
    profile["company"] = person.company
    profile["city"] = person.city
    profile["country"] = person.country
    profile["is_active"] = person.is_active
    return profile
