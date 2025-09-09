class Person:

    people = {}  # name: Person

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    ul = []
    for person in people:
        pers = Person(person["name"], person["age"])
        ul.append(pers)

    for person in people:
        me = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            me.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            me.husband = Person.people[person["husband"]]
    return ul
