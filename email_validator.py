import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"(?P<name>[a-z]*)\@(?P<server>[a-z]*)(?P<domain>[\.a-z]*)"

domain_list = [".com", ".bg", ".org", ".net"]

command = input()

while not command == "End":

    current_email = command

    regex_result = re.findall(pattern, current_email)

    if "@" not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    name = regex_result[0][0]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = regex_result[0][2]

    if domain not in domain_list:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    command = input()
