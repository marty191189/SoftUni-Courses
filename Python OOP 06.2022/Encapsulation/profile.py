class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_name):

        if len(new_name) < 5 or 15 < len(new_name):
            raise ValueError ("The username must be between 5 and 15 characters.")

        self.__username = new_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):

        is_length_valid = 8 <= len(new_password)

        is_uppercase_presented = any([True for char in new_password if char.isupper()])

        is_digit_presented = any([True for char in new_password if char.isdigit()])

        if not is_length_valid or not is_uppercase_presented or not is_digit_presented:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = new_password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')

profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
