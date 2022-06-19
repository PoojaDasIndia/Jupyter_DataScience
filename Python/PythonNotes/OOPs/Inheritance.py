# Inherit: To receive a quality, characteristic, etc., from your parents or family.
"""The base class is called the parent class, and the derived class is known as a child."""
print("\n************Without inheritance**************\n")
class Family:

    def __init__(self,family_name,number_of_member,country):
        self.family_name = family_name
        self.number_of_members = number_of_member
        self.country = country

    def member_says(self):
        print(f"Hey, I am from {self.family_name} family and there are {self.number_of_members} members in family")

class Family_detailed:
    def __init__(self, family_name, number_of_members, country):
        self.family_name = family_name
        self.number_of_members = number_of_members
        self.country=country

    def member_says(self):
        print(f"Hey, I am from {self.family_name} family and there are {self.number_of_members} members in family")

    def which_country(self):
        print(f"The {self.family_name} family has roots from {self.country}" )


a = Family("Rodrigues",5,"Peru")
b = Family_detailed("Bezos",15,"United States of America")

a.member_says()
b.member_says()
b.which_country()


print("\n************With inheritance**************\n")

class Family:
    def __init__(self, family_name, number_of_members, country):
        self.family_name = family_name
        self.number_of_members = number_of_members
        self.country=country

    def member_says(self):
        print(f"Hey, I am from {self.family_name} family and there are {self.number_of_members} members in family")


class Family_detailed(Family):

    def which_country(self):
        print(f"The {self.family_name} family has roots from {self.country}" )


a = Family("Rodrigues",5,"Peru")
b = Family_detailed("Bezos",15,"United States of America")

a.member_says()
b.member_says()
b.which_country()