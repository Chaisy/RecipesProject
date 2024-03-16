import string
save_data = {}


class User:
    __slots__ = ['Nickname','Role', 'Name', 'Surname', 'Email', 'Password', 'About']

    def __init__(self, Nickname: str, Role:str, Name: str, Surname: str, Email: str, Password: str, About: str) -> None:
        self.Nickname = Nickname
        self.Role = Role
        self.Name = Name
        self.Surname = Surname
        self.Email = Email
        self. Password = Password
        self.About = About
    #
    # def __str__(self):
    #     return self.Nickname, self.Role, self.Name, self.Surname, self.Email, self.Password, self.About

    def registration_dict(self):
        global save_data
        save_data = {'Admin': '1111', '1111': 'A'}
        save_list_data = [self.Nickname, self.Role, self.Surname, self.Email, self.Password]
        save_data[self.Nickname] = save_list_data[4]  # -1
        save_data[self.Password] = save_list_data[1]
        return save_data


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

class SuperAdmin:
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



