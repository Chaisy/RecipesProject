import string


class User:
    __slots__ = ['Nickname', 'Name', 'Surname', 'Email', 'Password']

    def __init__(self, Nickname: str, Name: str, Surname: str, Email: str, Password: str) -> None:
        self.Nickname = Nickname
        self.Name = Name
        self.Surname = Surname
        self.Email = Email
        self. Password = Password

    def __str__(self):
        return self.Nickname


class Chef:
    __slots__ = ['Nickname', 'Name', 'Surname', 'Email', 'Password', 'MyRecipes', 'Views', 'Likes']

    def __init__(self, Nickname: str, Name: str, Surname: str, Email: str, Password: str, Views: int, Likes: int, MyRecipes: list[string] = None) -> None:
        self.Nickname = Nickname
        self.Name = Name
        self.Surname = Surname
        self.Email = Email
        self. Password = Password
        self.Views = Views
        self.Likes = Likes
        self.MyRecipes = MyRecipes

    def __str__(self):
        return self.Nickname

class Admin:
    __slots__ = ['Nickname', 'Name', 'Surname', 'Email', 'Password', 'EmailsAll', 'BlockedAll', 'Complaints']

    def __init__(self, Nickname: str, Name: str, Surname: str, Email: str, Password: str, EmailsAll: list[string]=None, BlockedAll: list[string]= None, Complaints: list[string] = None) -> None:
        self.Nickname = Nickname
        self.Name = Name
        self.Surname = Surname
        self.Email = Email
        self. Password = Password
        self.EmailsAll = EmailsAll
        self.BlockedAll = BlockedAll
        self.Complaints = Complaints

    def __str__(self):
        return self.Nickname



