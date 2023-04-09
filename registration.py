import app_recipe as ap
import log_in
import customtkinter as CTk
from PIL import Image


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

        self.entry_nickname = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Nickname",
                                           font=("Courier", 18))
        self.entry_nickname.grid(row=0, column=0, sticky="n", pady=(100, 0))

        self.entry_name = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Nickname",
                                       font=("Courier", 18))
        self.entry_name.grid(row=0, column=0, sticky="n", pady=(150, 0))

        self.entry_surname = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Nickname",
                                          font=("Courier", 18))
        self.entry_surname.grid(row=0, column=0, sticky="n", pady=(200, 0))

        self.entry_email = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Password",
                                        font=("Courier", 18))
        self.entry_email.grid(row=0, column=0, sticky="n", pady=(250, 0))

        self.entry_password = CTk.CTkEntry(master=self.menu_frame, width=300, placeholder_text="Password",
                                           font=("Courier", 18))
        self.entry_password.grid(row=0, column=0, sticky="n", pady=(300, 0))

        self.go_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                       fg_color="#6f8e3e", text="Go!", font=("Courier", 18))
        self.go_button.grid(row=0, column=0, sticky="n", pady=(350, 0))

        self.logIn_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                          fg_color="white",
                                          text_color="black", text="Registration", font=("Courier", 18),
                                          command=self.LogIn_button_event
                                          )
        self.logIn_button.grid(row=0, column=0, sticky="n", pady=(400, 0))

        self.about_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                          fg_color="white", text_color="black", text="About", font=("Courier", 18))
        self.about_button.grid(row=0, column=0, sticky="sw", padx=(110, 0), pady=(450, 0))

        self.help_button = CTk.CTkButton(master=self.menu_frame, width=100, height=40, hover_color="#bdd88b",
                                         fg_color="white", text_color="black", text="Help", font=("Courier", 18))
        self.help_button.grid(row=0, column=0, sticky="se", padx=(0, 110), pady=(450, 0))

    def LogIn_button_event(self):
        self.destroy()
        log_in.Log_in()


