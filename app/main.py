class Person:

    people = {}  # name: Person

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list: list[Person] = []
    for person in people:
        temp_person = Person(person["name"], person["age"])
        if person.get("wife"):
            temp_person.wife = None
        else:
            temp_person.husband = None
        result_list.append(temp_person)

    for person in people:
        me = Person.people.get(person.get("name"))
        wife = Person.people.get(person.get("wife"))
        husband = Person.people.get(person.get("husband"))
        wife_husband = wife or husband
        if person.get("wife"):
            me.wife = wife_husband
        else:
            me.husband = wife_husband

    return result_list
