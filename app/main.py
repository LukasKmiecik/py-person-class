class Person:

    people = {}  # name: Person

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


# def create_person_list(person_dict : list) -> list:
#     Person.people.clear()
#     result_list: list[Person] = []
#     for person in person_dict :
#         temp_person = Person(person["name"], person["age"])
#         if person.get("wife"):
#             temp_person.wife = None
#         else:
#             temp_person.husband = None
#         result_list.append(temp_person)
#
#     for person in person_dict :
#         me = Person.people.get(person.get("name"))
#         wife = Person.people.get(person.get("wife"))
#         husband = Person.people.get(person.get("husband"))
#         spouse_name = wife or husband
#         if person.get("wife"):
#             me.wife = spouse_name
#         else:
#             me.husband = spouse_name
def create_person_list(person_dict: list) -> list:
    Person.people.clear()
    result_list = []
    for person in person_dict:
        temp_person = Person(person["name"], person["age"])
        result_list.append(temp_person)
    for person in person_dict:
        me = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            me.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            me.husband = Person.people[person["husband"]]
    return result_list
