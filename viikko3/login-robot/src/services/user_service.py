from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password))

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        # muut ehdot nimelle ja salasanalle:
        # Käyttäjätunnuksen on oltava merkeistä a-z koostuva vähintään 3 merkin pituinen merkkijono,
        # joka ei ole vielä käytössä.
        # Vinkki: säännölliset lausekkeet ja ^[a-z]+$.
        # Salasanan on oltava vähintään 8 merkkiä pitkä.
        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")
        if not username.isalpha():
            # the isalpha() method returns True if all the characters are alphabet letters (a-z)
            # https://www.w3schools.com/python/ref_string_isalpha.asp
            raise UserInputError("Username must only contain letters")
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")
        #salasanassa ei saa olla pelkkiä kirjaimia
        if password.isalpha():
            raise UserInputError("Password cannot only contain letters")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
