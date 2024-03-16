import re

from CTkMessagebox import CTkMessagebox

import log_in
import customtkinter as CTk
from PIL import Image
import pickle
import roles
import sqlite3
picture_filename = "./UsersPic/user_cat.jpg"
resultChooseRole = "U"
f = ('Times', 14)

con = sqlite3.connect('Userdata2.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record2(
                    nickname text,
                    role text,
                    name text,
                    surname text, 
                    email text,  
                    password text,
                    about text
                )
            ''')
con.commit()

class Registration(CTk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("700x500")
        self.title("Registration")
        self.resizable(False, False)

        self.registration_frame = CTk.CTkFrame(master=self, fg_color="white", width=700, height=500)
        self.registration_frame.grid(row=0, column=0)

        self.pic = CTk.CTkImage(dark_image=Image.open("./projectRecipes/chicken.jpg"), size=(233, 500))
        self.pic_frame = CTk.CTkFrame(master=self.registration_frame, height=500, width=233)
        self.pic_frame.grid(row=0, column=0, sticky="w")
        self.pic_label = CTk.CTkLabel(master=self.pic_frame, text="", image=self.pic)
        self.pic_label.grid(row=0, column=0, sticky="w")

        self.menu_frame = CTk.CTkFrame(master=self.registration_frame, width=467, height=500, fg_color="white")
        self.menu_frame.grid(row=0, column=1, sticky="n")

        self.logo_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 20), text_color="black",
                                      text="Afflatus")
        self.logo_text.grid(row=0, column=0, pady=(10, 0), sticky="n")
        role_var = CTk.BooleanVar()
        role_var.set(False)

        self.chooseUser_radio = CTk.CTkRadioButton(master=self.menu_frame, text="User",
                                                   variable=role_var, value=0,
                                                   fg_color="#6f8e3e", border_color="#bdd88b",
                                                   hover_color="#bdd88b", font=("Courier", 16),
                                                   command=self.userChoose)

        self.chooseUser_radio.grid(row=0, column=0, sticky="nw", pady=(50, 0), padx=(110, 0))

        self.chooseChef_radio = CTk.CTkRadioButton(master=self.menu_frame, text="Chef",
                                                   variable=role_var, value=1, border_color="#bdd88b",
                                                   fg_color="#6f8e3e", hover_color="#bdd88b", font=("Courier", 16),
                                                   command=self.chefChoose)

        self.chooseChef_radio.grid(row=0, column=0, sticky="ne", pady=(50, 0), padx=(0, 110))

        self.entry_nickname = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Nickname",
                                           font=("Courier", 18))
        self.entry_nickname.grid(row=0, column=0, sticky="n", pady=(100, 0))

        self.entry_name = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Name",
                                       font=("Courier", 18))
        self.entry_name.grid(row=0, column=0, sticky="n", pady=(150, 0))

        self.entry_surname = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Surname",
                                          font=("Courier", 18))
        self.entry_surname.grid(row=0, column=0, sticky="n", pady=(200, 0))

        self.entry_email = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Email",
                                        font=("Courier", 18))
        self.entry_email.grid(row=0, column=0, sticky="n", pady=(250, 0))

        self.entry_password = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Password",
                                           font=("Courier", 18))
        self.entry_password.grid(row=0, column=0, sticky="n", pady=(300, 0))

        self.go_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                       fg_color="#6f8e3e", text="Go!", font=("Courier", 18),
                                       command=lambda: self.registrate_Login_password()
                                       )
        self.go_button.grid(row=0, column=0, sticky="n", pady=(350, 0))

        self.logIn_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                          fg_color="white",
                                          text_color="black", text="LogIn", font=("Courier", 18),
                                          command=self.LogIn_button_event
                                          )
        self.logIn_button.grid(row=0, column=0, sticky="n", pady=(400, 0))

        self.about_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                          fg_color="white", text_color="black", text="About", font=("Courier", 18),
                                          command=self.about_button_event)
        self.about_button.grid(row=0, column=0, sticky="sw", padx=(110, 0), pady=(450, 0))

        self.help_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                         fg_color="white", text_color="black", text="Help", font=("Courier", 18),
                                         command=self.help_button_event)
        self.help_button.grid(row=0, column=0, sticky="se", padx=(0, 110), pady=(450, 0))

    def userChoose(self):
        global resultChooseRole
        resultChooseRole = "U"
        return resultChooseRole

    def chefChoose(self):
        global resultChooseRole
        resultChooseRole = "C"
        return resultChooseRole

    def adminChoose(self):
        global resultChooseRole
        resultChooseRole = "A"
        return resultChooseRole

    def LogIn_button_event(self):
        self.destroy()
        log_in.Log_in()

    def about_button_event(self):
        self.destroy()
        log_in.About()

    def help_button_event(self):
        self.destroy()
        log_in.Help()

    def registrate_Login_password(self):
        povtop=0
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from record2"):
            nickname = row[0]
            password = row[5]
            if (self.entry_nickname.get() == nickname or self.entry_password.get() == password): povtop+=1

        if not povtop:

            if re.fullmatch(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+',self.entry_email.get()):
                cur.execute(
                    "INSERT INTO record2 VALUES (:nickname, :role, :name, :surname, :email, :password, :about, :photo)",
                    {
                        'nickname': self.entry_nickname.get(),
                        'role': resultChooseRole,
                        'name': self.entry_name.get(),
                        'surname': self.entry_surname.get(),
                        'email': self.entry_email.get(),
                        'password': self.entry_password.get(),
                        'about': "",
                        'photo': picture_filename

                    })
                dataBase.commit()
                self.destroy()
                log_in.Log_in()
            else:
                CTkMessagebox(master=self, title="Error", message="You have problem with email!")

        else:
            CTkMessagebox(master=self, title="Error", message="You cant use this nick or password!")
        global save_data
        save_user = roles.User(self.entry_nickname.get(), resultChooseRole, self.entry_name.get(),
                               self.entry_surname.get(), self.entry_email.get(), self.entry_password.get(), "")
        save_data = roles.User.registration_dict(save_user)
        print(save_data)
        # save_list_data=[self.entry_name, resultChooseRole, self.entry_surname, self.entry_email, self.entry_password]#пока что не сохраняет ник
        # save_data[self.entry_nickname.get()] = save_list_data[4].get()#-1
        # save_data[self.entry_password.get()] = save_list_data[1]
        file_DataBase = open("dataDase_local.txt", 'wb')

        pickle.dump(save_data, file_DataBase)
        file_DataBase.close()
        print(f"ПРОВЕРКА. ВЫВОД СЛОВАРЯ С ПАРОЛЯМИ И РОЛЯМИ\n{save_data}")

