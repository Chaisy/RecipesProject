from CTkMessagebox import CTkMessagebox
import Admin
import ChefFunctions
import roles
import UserFunctions
import registration
import customtkinter as CTk
from PIL import Image
import sqlite3

# формат почты, уникальность логина и logOut
# вопрос с админом, любой пользователь не модет же им быть
# почему 2 окна)))))))) при вызове классе из другого файла он отрисовывает дважды
# как сделать команду при создании кнопок в цикле

class Log_in(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x500")
        self.title("LogIn")
        self.resizable(False, False)

        self.logIn_frame = CTk.CTkFrame(master=self, fg_color="white", width=700, height=500)
        self.logIn_frame.grid(row=0, column=0)

        self.pic = CTk.CTkImage(dark_image=Image.open("./projectRecipes/IMG_20230408_000133.jpg"), size=(233, 500))
        self.pic_frame = CTk.CTkFrame(master=self.logIn_frame, height=500, width=233)
        self.pic_frame.grid(row=0, column=0, sticky="w")
        self.pic_label = CTk.CTkLabel(master=self.pic_frame, text="", image=self.pic)
        self.pic_label.grid(row=0, column=0, sticky="w")

        self.menu_frame = CTk.CTkFrame(master=self.logIn_frame, width=467, height=500, fg_color="white")
        self.menu_frame.grid(row=0, column=1, sticky="n")

        self.logo_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 20), text_color="black",
                                      text="Afflatus")
        self.logo_text.grid(row=0, column=0, pady=(10, 0), sticky="n")

        self.entry_nickname = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Nickname",
                                           font=("Courier", 18))
        self.entry_nickname.grid(row=0, column=0, sticky="n", pady=(150, 0))

        self.entry_password = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Password",
                                           font=("Courier", 18))
        self.entry_password.grid(row=0, column=0, sticky="n", pady=(200, 0))

        self.go_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                       fg_color="#6f8e3e", text="Go!", font=("Courier", 18),
                                       command=lambda: self.LogIn_Check())
        self.go_button.grid(row=0, column=0, sticky="n", pady=(280, 0))

        self.registration_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                                 fg_color="white",
                                                 text_color="black", text="Registration", font=("Courier", 18),
                                                 command=self.home_button_event
                                                 )
        self.registration_button.grid(row=0, column=0, sticky="n", pady=(350, 0))

        self.about_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                          fg_color="white", text_color="black", text="About", font=("Courier", 18),
                                          command=self.about)
        self.about_button.grid(row=0, column=0, sticky="sw", padx=(110, 0), pady=(400, 0))

        self.help_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                         fg_color="white", text_color="black", text="Help", font=("Courier", 18),
                                         command=self.help)
        self.help_button.grid(row=0, column=0, sticky="se", padx=(0, 110), pady=(400, 0))

    def home_button_event(self):
        self.destroy()
        registration.Registration()



    def about(self):
        self.destroy()
        About()

    def help(self):
        self.destroy()
        Help()

    def LogIn_Check(self):
        # try:
            con = sqlite3.connect('Userdata2.db')
            c = con.cursor()
            check = False
            for row in c.execute("Select * from record2"):
                username = row[0]
                pwd = row[5]
                role = row[1]

                if self.entry_nickname.get() == username:
                    check = True
                    if self.entry_password.get() == pwd:
                        if role:
                            if role == "C":
                                active_user = roles.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                                print(active_user)
                                ChefFunctions.save_active_info(active_user)
                                self.destroy()
                                ChefFunctions.ChefFunc()

                                # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You chef!")
                                break
                            if role == "U":
                                active_user = roles.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                                print(active_user)
                                UserFunctions.save_active_info(active_user)
                                self.destroy()
                                UserFunctions.UserInt()
                                # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You user!")
                                break
                            if role == "A":
                                active_user = roles.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                                print(active_user)
                                Admin.save_active_info(active_user)
                                self.destroy()
                                Admin.AdminInt()
                                # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You admin!")
                                break
                        else:
                            CTkMessagebox(master=self, title="Congratulations!!!!!", message="You nixto!")
                            break
                    else:
                        CTkMessagebox(title="Failed", message=f"Password is wrong. Please? try again")
                        break
            if not check:
                CTkMessagebox(title="Failed",
                              message=f"No user with nickname{self.entry_nickname.get()}, please registrate")



        # except Exception:
        #     CTkMessagebox(title="Failed", message=f"ne zashi v basy")

        # file_DataBase = open("dataDase_local.txt", 'rb')
        # #data_roles = roles.User
        #
        # data = pickle.load(file_DataBase)
        # print(data)
        # file_DataBase.close()
        # if self.entry_nickname.get() in (d for d in data):
        #     # data_list = data[self.entry_nickname.get()]
        #     if self.entry_password.get() == data[self.entry_nickname.get()]:
        #         if self.entry_password.get() in data:
        #             if data[self.entry_password.get()] == "C":
        #                 self.destroy()
        #                 Chef.ChefInt()
        #                 # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You chef!")
        #             if data[self.entry_password.get()] == "U":
        #                 self.destroy()
        #                 UserFunctions.Recommendation()
        #                 # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You user!")
        #             if data[self.entry_password.get()] == "A":
        #                 # self.destroy()
        #                 # UserFunctions.Recommendation()
        #                 CTkMessagebox(master=self, title="Congratulations!!!!!", message="You admin!")
        #         else:
        #                 CTkMessagebox(master=self, title="Congratulations!!!!!", message="You nixto!")
        #     else:
        #
        #         CTkMessagebox(title="Failed",message=f"Password is wrong. Please? try again")
        # else:
        #     CTkMessagebox(title="Failed",message=f"No user with nickname{self.entry_nickname.get()}, please registrate")

class About(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x500")
        self.title("LogIn")
        self.resizable(False, False)

        self.about_frame = CTk.CTkFrame(master=self, fg_color="white", width=700, height=500)
        self.about_frame.grid(row=0, column=0)

        self.text = CTk.CTkLabel(master=self.about_frame, height=500, width=700, font=("Courier", 20), text_color="black",
                                 text="Here is a list of the most popular recipes that\n people are loving!\n "
                                      "Try out some of these recipes to find out \nwhy everyone is "
                                      "raving about them.")
        self.text.grid(row=0, column=0, sticky="nswe")

        self.cancel_button = CTk.CTkButton(master=self.about_frame, width=300, height=40, hover_color="#bdd88b",
                                           fg_color="#6f8e3e", text="Cancel", font=("Courier", 18),
                                           command=self.home_button_event1)
        self.cancel_button.grid(row=0, column=0, pady=(0,10), sticky="s")

    def home_button_event1(self):
        self.destroy()
        Log_in()

class Help(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x500")
        self.title("LogIn")
        self.resizable(False, False)

        self.about_frame = CTk.CTkFrame(master=self, fg_color="white", width=700, height=500)
        self.about_frame.grid(row=0, column=0)

        self.text = CTk.CTkLabel(master=self.about_frame, height=500, width=700, font=("Courier", 20), text_color="black",
                                 text=" If you have problems with app, you can write us\n"
                                      "EMAIL: dashulianortom@gmail.com")
        self.text.grid(row=0, column=0)

        self.cancel_button = CTk.CTkButton(master=self.about_frame, width=300, height=40, hover_color="#bdd88b",
                                           fg_color="#6f8e3e", text="Cancel", font=("Courier", 18),
                                           command=self.home_button_event1)
        self.cancel_button.grid(row=0, column=0, pady=(0,10), sticky="s")

    def home_button_event1(self):
        self.destroy()
        Log_in()

