import pickle
from CTkMessagebox import CTkMessagebox
import registration
import User
import Chef
import customtkinter as CTk
from PIL import Image
#вопрос с админом, любой пользователь не модет же им быть
#почему 2 окна)))))))) при вызове классе из другого файла он отрисовывает дважды

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
                                          fg_color="white", text_color="black", text="About", font=("Courier", 18))
        self.about_button.grid(row=0, column=0, sticky="sw", padx=(110, 0), pady=(400, 0))

        self.help_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                         fg_color="white", text_color="black", text="Help", font=("Courier", 18))
        self.help_button.grid(row=0, column=0, sticky="se", padx=(0, 110), pady=(400, 0))


    def home_button_event(self):
        self.destroy()
        registration.Registration()

    def LogIn_Check(self):
        file_DataBase = open("dataDase_local.txt", 'rb')
        data = pickle.load(file_DataBase)
        print(data)
        file_DataBase.close()
        if self.entry_nickname.get() in data:
            # data_list = data[self.entry_nickname.get()]
            if self.entry_password.get() == data[self.entry_nickname.get()]:
                if self.entry_password.get() in data:
                    if data[self.entry_password.get()] == "C":
                        self.destroy()
                        Chef.ChefInt()
                        # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You chef!")
                    if data[self.entry_password.get()] == "U":
                        self.destroy()
                        User.Recommendation()
                        # CTkMessagebox(master=self, title="Congratulations!!!!!", message="You user!")
                else:
                        CTkMessagebox(master=self, title="Congratulations!!!!!", message="You nixto!")
            else:

                CTkMessagebox(title="Failed",message=f"Password is wrong. Please? try again")
        else:
            CTkMessagebox(title="Failed",message=f"No user with nickname{self.entry_nickname.get()}, please registrate")

