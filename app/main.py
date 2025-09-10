class Person:
    people = {}  # name: Person
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result_list = []
    for person in people:
        temp_person = Person(person["name"], person["age"])
        result_list.append(temp_person)
    for person in people:
        me = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            spouse = Person.people[person["wife"]]
            me.wife = spouse
            if not hasattr(spouse, "husband"):
                spouse.husband = me
        if "husband" in person and person["husband"] is not None:
            spouse = Person.people[person["husband"]]
            me.husband = spouse
            if not hasattr(spouse, "wife"):
                spouse.wife = me
    return result_list
