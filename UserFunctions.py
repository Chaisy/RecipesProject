import json
import sqlite3
import tkinter
import customtkinter as CTk
from PIL import Image
import log_in
import recipe
import roles
picture_filename = "./UsersPic/user_cat.jpg"
filename = "./projectRecipes/Kitty.jpg"
list_ingr=[]
likes=[]
recipe_add = recipe.Recipe("None", "<5", "", "<100" ,"" ,"" ,"" ,[], [], [])
info =roles.User("", "", "", "", "", "", "")
# class ScrollableCheckBoxFrame(CTk.CTkScrollableFrame):
#     def __init__(self, master, item_list, command=None, **kwargs):
#         super().__init__(master, **kwargs)
#
#         self.command = command
#         self.checkbox_list = []
#         for i, item in enumerate(item_list):
#             for j, item in enumerate(item_list):
#                 button_recipe = CTk.CTkButton(self, text=item, width=324, height=400, fg_color="#dbdbdb", hover_color="#bdd88b")
#                 if self.command is not None:
#                     button_recipe.configure(command=self.command)
#                 button_recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))
#                 self.checkbox_list.append(button_recipe)
#
#
#     def remove_item(self, item):
#         for button_recipe in self.checkbox_list:
#             if item == button_recipe.cget("text"):
#                 button_recipe.destroy()
#                 self.checkbox_list.remove(button_recipe)
#                 return






class UserInt(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1400x1000")
        self.title("UserInt")
        self.resizable(False, False)

        self.userInt_frame = CTk.CTkFrame(master=self, fg_color="white", width=1400, height=1000)
        self.userInt_frame.grid(row=0, column=0)

        self.logo_text = CTk.CTkLabel(master=self.userInt_frame, width=1400, height=80, font=("Courier", 20),
                                      text_color="black",
                                      text="Afflatus")
        self.logo_text.grid(row=0, column=0, sticky="n")

        self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
        self.info_frame.grid(row=1, column=0)
        self.info_label = CTk.CTkLabel(master=self.info_frame, width=1400, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="Recommendations")
        self.info_label.grid(row=0, column=0)

        self.recepies_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=870)
        self.recepies_frame.grid(row=2, column=0)
        self.recepies_frame.grid_propagate(False)

        # self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.recepies_frame, width=1356, height=820,
        #                                                          command=self.checkbox_frame_event, fg_color="transparent",
        #                                                          item_list=[f"item {i}" for i in range(4)])#количество окошек
        # self.scrollable_checkbox_frame.grid(row=1, column=0, sticky="ns")
        # self.scrollable_checkbox_frame.add_item("new item")

        # self.recoment_frame = CTk.CTkFrame(master=self.recepies_frame, fg_color="white", width=1400, height=820)
        # self.recoment_frame.grid(row=1, column=0, sticky="n")
        # self.recoment_frame.grid_propagate(False)#возможно нужно комментить
        self.menu_frame = CTk.CTkFrame(master=self.userInt_frame, width=1400, height=100)
        self.menu_frame.grid(row=3, column=0, sticky="s")
        menu_list = ['Recommendation', 'Search', 'Liked', 'Watched', 'Profile']
        self.recommendation_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
                                                   hover_color="#6f8e3e", text="Recommendation",
                                                   text_color="black", font=("Courier", 18),
                                                   command=lambda: self.Recomendations()
                                                   )
        self.recommendation_button.grid(row=0, column=0)
        self.search_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
                                           hover_color="#6f8e3e", text="Search",
                                           text_color="black", font=("Courier", 18),
                                           command=lambda: self.Search()
                                           )
        self.search_button.grid(row=0, column=1)

        # self.my_recipies_button = CTk.CTkButton(master=self.menu_frame, width=233, height=100, fg_color="white",
        #                                         hover_color="#6f8e3e", text="My Recipes",
        #                                         text_color="black", font=("Courier", 18),
        #                                         command=lambda: self.My_Recipes()
        #                                         )
        # self.my_recipies_button.grid(row=0, column=2)

        self.liked_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
                                          hover_color="#6f8e3e", text="Liked",
                                          text_color="black", font=("Courier", 18),
                                          command=lambda: self.Liked(info.Nickname)
                                          )
        self.liked_button.grid(row=0, column=3)
        # self.watched_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
        #                                             hover_color="#6f8e3e", text = "Watched",
        #                                             text_color="black", font=("Courier", 18),
        #                                             command= lambda : self.Watched()
        #                                             )
        # self.watched_button.grid(row=0, column=4)
        # # a = UserFunctions.Recommendation()
        # self.rewiews_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
        #                                     hover_color="#6f8e3e", text="Rewiew",
        #                                     text_color="black", font=("Courier", 18),
        #                                     command=lambda: self.Profile()
        #                                     )
        # self.rewiews_button.grid(row=0, column=5)

        self.profile_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
                                            hover_color="#6f8e3e", text="Profile",
                                            text_color="black", font=("Courier", 18),
                                            command=lambda: self.Profile()
                                            )
        self.profile_button.grid(row=0, column=4)

        self.unLogIn_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="#6f8e3e",
                                            hover_color="#bdd88b", text="LogOut",
                                            text_color="black", font=("Courier", 18),
                                            command=lambda: self.LogOut()
                                            )
        self.unLogIn_button.grid(row=0, column=5)

        self.load_all_BD(info.Nickname)
        # self.geometry("1400x1000")
        # self.title("UserInt")
        # self.resizable(False, False)
        #
        # self.userInt_frame = CTk.CTkFrame(master=self, fg_color="white", width=1400, height=1000)
        # self.userInt_frame.grid(row=0, column=0)
        #
        # self.logo_text = CTk.CTkLabel(master=self.userInt_frame, width=1400, height=80, font=("Courier", 20), text_color="black",
        #                              text="Afflatus")
        # self.logo_text.grid(row=0, column=0, sticky="n")
        #
        # self.recepies_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
        # self.recepies_frame.grid(row=1, column=0)
        #
        # # self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.recepies_frame, width=1356, height=820,
        # #                                                          command=self.checkbox_frame_event, fg_color="transparent",
        # #                                                          item_list=[f"item {i}" for i in range(4)])#количество окошек
        # # self.scrollable_checkbox_frame.grid(row=1, column=0, sticky="ns")
        # # self.scrollable_checkbox_frame.add_item("new item")
        #
        # self.menu_frame = CTk.CTkFrame(master=self.userInt_frame, width=1400, height=100)
        # self.menu_frame.grid(row=2, column=0)
        # menu_list = ['Recommendation', 'Search', 'Liked', 'Watched', 'Profile']
        # self.recommendation_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
        #                                             hover_color="#6f8e3e", text = "Recommendation",
        #                                             text_color="black", font=("Courier", 18),
        #                                             command= lambda : self.Liked()
        #                                             )
        # self.recommendation_button.grid(row=0, column=0)
        # self.search_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
        #                                             hover_color="#6f8e3e", text = "Search",
        #                                             text_color="black", font=("Courier", 18),
        #                                             command= lambda : self.Search()
        #                                             )
        # self.search_button.grid(row=0, column=1)
        #
        # self.liked_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
        #                                             hover_color="#6f8e3e", text = "Liked",
        #                                             text_color="black", font=("Courier", 18),
        #                                             command= lambda : self.Liked()
        #                                             )
        # self.liked_button.grid(row=0, column=2)
        # self.watched_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
        #                                             hover_color="#6f8e3e", text = "Watched",
        #                                             text_color="black", font=("Courier", 18),
        #                                             command= lambda : self.Watched()
        #                                             )
        # self.watched_button.grid(row=0, column=3)
        # self.profile_button = CTk.CTkButton(master=self.menu_frame, width=280, height=100, fg_color="white",
        #                                             hover_color="#6f8e3e", text = "Profile",
        #                                             text_color="black", font=("Courier", 18),
        #                                             command= lambda : self.Profile()
        #                                             )
        # self.profile_button.grid(row=0, column=4)




    def LogOut(self):
        self.destroy()
        log_in.Log_in()

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

    def Recomendations(self):
        self.info_frame.destroy()
        self.recepies_frame.destroy()

        self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
        self.info_frame.grid(row=1, column=0, sticky="n")

        self.info_label = CTk.CTkLabel(master=self.info_frame, width=1400, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="Recommendations")
        self.info_label.grid(row=0, column=0)
        self.my_recipe_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=720)
        self.my_recipe_frame.grid(row=2, column=0, sticky="n")

        self.load_all_BD(info.Nickname)

    def Liked(self, nickname):
        global info, likes
        print(f" лайки -- {info.Nickname}")
        self.info_frame.destroy()
        self.recepies_frame.destroy()

        self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
        self.info_frame.grid(row=1, column=0, sticky="n")

        self.info_label = CTk.CTkLabel(master=self.info_frame, width=467, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="Liked")
        self.info_label.grid(row=0, column=0)

        # self.profile_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="pink", width=1400, height=770)
        # self.profile_frame.grid(row=2, column=0, sticky="n")
        # self.profile_frame.grid_propagate(False)
        i = -1
        j = -1
        self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
                                            height=770)  # height=720)
        self.my_recipe_frame.grid(row=2, column=0, sticky="n")
        self.my_recipe_frame.grid_propagate(False)
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from recordRecipe"):
            j += 1
            if j % 4 == 0:
                i += 1
                j = 0
            print(i)
            name = row[0]
            # likes = json.loads(row[6])
            # print(f"список лайков{likes}")
            if nickname in json.loads(row[6]):

                kkal = row[3]
                time = row[1]
                photo = row[9]
                with open(f"./projectRecipes/{name}.jpg", 'wb') as file:
                    file.write(photo)
                recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
                                      fg_color="#dbdbdb")
                self.call_recipe(name, time, kkal, f"./projectRecipes/{name}.jpg", i, j)
                recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))

    # def Watched(self):
    #
    #     self.recepies_frame.destroy()
    #
    #     self.liked_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
    #     self.liked_frame.grid(row=1, column=0)
    #
    #     self.infoLiked_label = CTk.CTkLabel(master=self.liked_frame, width=1400, height=820, font=("Courier", 10), text_color="black",#50
    #                                  text="Here You Can See Recipes, That You Watched")
    #     self.infoLiked_label.grid(row=0, column=0)
    #     self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
    #     self.recepies_frame.grid(row=1, column=0)

    def Profile(self):
        global info, picture_filename
        # active_info_profile = info
        self.info_frame.destroy()
        self.recepies_frame.destroy()
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from record2"):
            nick = row[0]
            if info.Nickname == nick:
                role = row[1]
                name = row[2]
                surname = row[3]
                email = row[4]
                about = row[6]
                photo = row[7]
                # with open(f"./UsersPic/{nick}.jpg", 'wb') as file:
                    # file.write(photo)
                self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
                self.info_frame.grid(row=1, column=0, sticky="n")

                self.info_label = CTk.CTkLabel(master=self.info_frame, width=467, height=50, font=("Courier", 15),
                                               text_color="black",  # 50
                                               text="Profile")
                self.info_label.grid(row=0, column=0)

                self.profile_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=770)
                self.profile_frame.grid(row=2, column=0, sticky="n")
                self.profile_frame.grid_propagate(False)

                self.picProf = CTk.CTkImage(dark_image=Image.open(picture_filename#f"./UsersPic/{nick}.jpg"
                                                                  ), size=(340, 750))

                self.pic_labelProf = CTk.CTkLabel(master=self.profile_frame, text="", image=self.picProf)
                self.pic_labelProf.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=(10, 10))

                self.menu_frame = CTk.CTkFrame(master=self.profile_frame, width=467, height=770, fg_color="white")
                self.menu_frame.grid(row=0, column=1, padx=(50, 0))

                ############################
                self.nickname_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                                  text_color="black",
                                                  text="Nickname: ")
                self.nickname_text.grid(row=0, column=0, pady=(10, 0), sticky="n")
                self.nickname = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                             text_color="black",
                                             text=info.Nickname)
                self.nickname.grid(row=0, column=1, pady=(10, 0), sticky="n")
                ############################
                self.name_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                              text_color="black",
                                              text="Name: ")
                self.name_text.grid(row=1, column=0, pady=(10, 0), sticky="n")
                self.name = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
                                         text=name)
                self.name.grid(row=1, column=1, pady=(10, 0), sticky="n")
                ############################
                self.surname_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                                 text_color="black",
                                                 text="Surname: ")
                self.surname_text.grid(row=2, column=0, pady=(10, 0), sticky="n")
                self.surname = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
                                            text=surname)
                self.surname.grid(row=2, column=1, pady=(10, 0), sticky="n")
                ############################
                ############################
                self.email_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                               text_color="black",
                                               text="Email: ")
                self.email_text.grid(row=3, column=0, pady=(10, 0), sticky="n")
                self.email = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
                                          text=email)
                self.email.grid(row=3, column=1, pady=(10, 0), sticky="n")
                ############################
                self.role_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                              text_color="black",
                                              text="Role: ")
                self.role_text.grid(row=4, column=0, pady=(10, 0), sticky="n")
                self.role = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
                                         text=role)
                self.role.grid(row=4, column=1, pady=(10, 0), sticky="n")
                ###########################
                self.info_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14),
                                              text_color="black",
                                              text="About: ")
                self.info_text.grid(row=5, column=0, pady=(10, 0), sticky="n")
                self.info = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
                                         text=about)
                self.info.grid(row=5, column=1, pady=(10, 0), sticky="n")

                self.entry_info = CTk.CTkEntry(master=self.menu_frame, width=300, height=150,
                                               placeholder_text="About me",
                                               font=("Courier", 18))
                self.entry_info.grid(row=6, column=0, sticky="n", padx=(50, 0), pady=(10, 0))

                self.add_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
                                                fg_color="#6f8e3e", text="Add", font=("Courier", 18),
                                                command=lambda: self.add_aboutMe()
                                                )
                self.add_button.grid(row=6, column=1)

                self.add_pic_button = CTk.CTkButton(master=self.menu_frame, width=467, height=50, hover_color="#bdd88b",
                                                    fg_color="white", text="Change Profile Photo", font=("Courier", 18),
                                                    text_color="black",
                                                    command=lambda: self.add_profile_picture()
                                                    )
                self.add_pic_button.grid(row=7, column=0)
                # self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
                # self.likedResipes_frame.grid(row=1, column=0)



    def add_aboutMe(self):
        global info
        adding = self.entry_info.get()
        info.About = adding
        print(adding)
        self.info.configure(text=info.About)
        # self.info['text'] = adding
        print(self.info.cget('text'))

        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        about_update = """Update record2 set about = ? where nickname = ? """
        data = (adding, info.Nickname)
        cur.execute(about_update, data)
        dataBase.commit()

    def add_profile_picture(self):
        filetypes = (("Изображение", "*.jpg *.gif *.png"))
        global picture_filename
        picture_filename = tkinter.filedialog.askopenfilename(title="Открыть файл",
                                                              initialdir="/home/dari/PycharmProjects/pythonProject1/UsersPic",
                                                              typevariable=filetypes)
        if picture_filename:
            print(picture_filename)

        self.pic_labelProf.configure(image=CTk.CTkImage(dark_image=Image.open(picture_filename), size=(340, 750)))
        with open(picture_filename, 'rb') as file:
            blob_data = file.read()
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        about_update = """Update record2 set photo = ? where nickname = ? """
        data = (blob_data, info.Nickname)
        cur.execute(about_update, data)
        dataBase.commit()
        print("done")

    def Search(self):
        self.info_frame.destroy()
        self.recepies_frame.destroy()

        self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
        self.info_frame.grid(row=1, column=0, sticky="n")

        self.info_label = CTk.CTkLabel(master=self.info_frame, width=467, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="Search")
        self.info_label.grid(row=0, column=0)

        self.menu_search = CTk.CTkFrame(master=self.info_frame, fg_color="white", width=1050, height=50)
        self.menu_search.grid(row=0, column=1, sticky="n")

        self.entry_search = CTk.CTkEntry(master=self.menu_search, width=466, height=50,
                                         font=("Courier", 18))
        self.entry_search.grid(row=0, column=0)  # название и ввод
        self.search_button = CTk.CTkButton(master=self.menu_search, width=466, height=50, fg_color="white",
                                           text="Search",
                                           hover_color="#bdd88b", font=("Courier", 18), text_color="black",
                                           command=self.search_recipe)
        self.search_button.grid(row=0, column=1)

        self.my_recipe_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=770)
        self.my_recipe_frame.grid(row=2, column=0, sticky="n")

    def search_recipe(self):
        self.recepies_frame.destroy()
        i = -1
        j = -1
        self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
                                            height=770)  # height=720)
        self.my_recipe_frame.grid(row=2, column=0, sticky="n")
        self.my_recipe_frame.grid_propagate(False)
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from recordRecipe"):
            j += 1
            if j % 4 == 0:
                i += 1
                j = 0
            print(i)
            name = row[0]
            if self.entry_search.get() == name:
                kkal = row[3]
                time = row[1]
                photo = row[9]
                with open(f"./projectRecipes/{name}.jpg", 'wb') as file:
                    file.write(photo)
                recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
                                      fg_color="#dbdbdb")
                self.call_recipe(name, time, kkal, f"./projectRecipes/{name}.jpg", i, j)
                recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))

    def load_all_BD(self, nickname):
        self.recepies_frame.destroy()
        info.Nickname = nickname
        i = -1
        j = -1
        self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
                                            height=770)  # height=720)
        self.my_recipe_frame.grid(row=2, column=0, sticky="n")
        self.my_recipe_frame.grid_propagate(False)

        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()

        for row in cur.execute("Select * from recordRecipe"):
            j += 1
            if j % 4 == 0:
                i += 1
                j = 0
            print(i)
            name = row[0]
            kkal = row[3]
            time = row[1]
            photo_ind = j
            photo = row[9]  # нужно хранить в стринге и просто название файла для filename
            with open(f"./projectRecipes/{name}.jpg", 'wb') as file:
                file.write(photo)
            recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
                                  fg_color="#dbdbdb")
            self.call_recipe(name, time, kkal, f"./projectRecipes/{name}.jpg", i, j)
            recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))

    def show_full_recipe(self, name):
        global recipe_add
        recipe_add.name = name
        print(f"recipe name -- {name}")
        window = Show_Full_Recipe(self)
        user = window.open()
        # self.load_all_BD(info.Nickname)


    def call_recipe(self, name, time, kcalAll, filenami,i,j):#окошко с мини рецептом
        # print(j)
        self.recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
                                         fg_color="#dbdbdb")
        self.recipe.grid(row=i, column=j,padx=(0, 15), pady=(0, 15))
        # self.recipe.grid_propagate(False)
        self.pic = CTk.CTkImage(dark_image=Image.open(filenami), size=(314,350))
        self.add_button = CTk.CTkButton(master=self.recipe, width=314, height=350, fg_color="#dbdbdb", text="",
                                        hover_color="#dbdbdb", font=("Courier", 18), text_color="black",
                                        image=self.pic)
        self.add_button.grid(row=0, column=0, sticky="n", pady=(5,0), padx =(5,5))
        self.recipe_name = CTk.CTkLabel(master=self.recipe, text=name,font=("Courier", 18))
        self.recipe_name.grid(row=1, column=0, sticky="n", pady=(5, 0))
        self.annotation_label = CTk.CTkLabel(master=self.recipe, text= "min: \nkkal: ",font=("Courier", 18))
        self.annotation_label.grid(row=2, column =0, sticky="w", padx = (60,0), pady = (5,0))

        self.t_k_label = CTk.CTkLabel(master=self.recipe, text=f"{time}\n{kcalAll}",
                                      font=("Courier", 18))
        self.t_k_label.grid(row=2, column =0,sticky="e", padx=(0,60),pady = (5,0))

        self.more_button = CTk.CTkButton(master=self.recipe, width=314, height=50, fg_color="#dbdbdb", text="More",
                                        hover_color="#bdd88b", font=("Courier", 18), text_color="black",
                                        command= lambda : self.show_full_recipe(name))
        self.more_button.grid(row=3, column=0, sticky="n", pady=(5,0), padx =(5,5))

def save_active_info(act):
    global info
    info = act
    print(info.Role)

class Show_Full_Recipe(CTk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        global info
        def like_combobox(choise):
            global recipe_add, info
            if self.combobox_like.get()=="like" and (not (info.Nickname in recipe_add.likes)):
                print(f" добавляем лайк --{info.Nickname}")
                recipe_add.likes.append(info.Nickname)
                self.save_like()

            else:
                print(f" удаляем лайк --{info.Nickname}")
                if info.Nickname in recipe_add.likes: recipe_add.likes.remove(info.Nickname)
                self.save_like()

        global recipe_add, list_ingr
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from recordRecipe"):
            nameBD = row[0]
            if recipe_add.name == nameBD:

                time = row[1]
                naming = row[2]
                kkal = row[3]
                cook=row[4]
                list_ingr = json.loads(row[5])
                # print(list_ingr)
                author = row[10]
                self.geometry("1000x530")
                self.title("Recipe")
                self.resizable(False, False)

                self.full_frame = CTk.CTkFrame(master=self, fg_color="white", width=1000, height=530)
                self.full_frame.grid(row=0, column=0)
                self.header_rec = CTk.CTkFrame(master=self.full_frame, fg_color="#bdd88b", width=1000, height=80)
                self.header_rec.grid(row=0, column=0, pady=(0, 5))  #
                self.logo_adding = CTk.CTkLabel(master=self.header_rec, text="Recipe", width=1000, height=80,
                                                text_color="black", font=("Courier", 18), fg_color="#bdd88b"
                                                )
                self.logo_adding.grid(row=0, column=0, pady=(0, 5))  #
                self.name_label = CTk.CTkLabel(master=self.full_frame, text=nameBD, width=1000, height=50,
                                               text_color="black", font=("Courier", 16), fg_color="white"
                                               )
                self.name_label.grid(row=1, column=0, pady=(0, 5))

                self.time_kcal_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=80)
                self.time_kcal_frame.grid(row=2, column=0, pady=(0, 5))  #
                self.time_show = CTk.CTkLabel(master=self.time_kcal_frame, text=time, width=200, height=50,
                                              text_color="black", font=("Courier", 18))
                self.time_show.grid(row=0, column=0)
                self.time_label = CTk.CTkLabel(master=self.time_kcal_frame, text=" min", width=200, height=50,
                                               text_color="black", font=("Courier", 18))
                self.time_label.grid(row=0, column=1, pady=(0, 5))
                self.razdelitel_label = CTk.CTkLabel(master=self.time_kcal_frame, text="\u2764\uFE0F", width=200,
                                                     height=50, text_color="black", font=("Courier", 18))
                self.razdelitel_label.grid(row=0, column=2, pady=(0, 5))
                self.kcal_show = CTk.CTkLabel(master=self.time_kcal_frame, text=kkal, width=200, height=50,
                                              text_color="black", font=("Courier", 18))
                self.kcal_show.grid(row=0, column=3, pady=(0, 5))
                self.kcal_label = CTk.CTkLabel(master=self.time_kcal_frame, text=" kcal", width=200, height=50,
                                               text_color="black", font=("Courier", 18))
                self.kcal_label.grid(row=0, column=4, pady=(0, 5))

                self.naming_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=50)
                self.naming_frame.grid(row=3, column=0, pady=(0, 5))  #
                self.naming_label = CTk.CTkLabel(master=self.naming_frame, text="Naming: ", width=300, height=50,
                                                 text_color="black", font=("Courier", 18))
                self.naming_label.grid(row=0, column=0)
                self.naming_show = CTk.CTkLabel(master=self.naming_frame, width=700, fg_color="white", text=naming,
                                                height=50, text_color="black", font=("Courier", 18))
                self.naming_show.grid(row=0, column=1)

                self.how_cook_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=80)
                self.how_cook_frame.grid(row=4, column=0, pady=(0, 5))  #
                self.how_cook_label = CTk.CTkLabel(master=self.how_cook_frame, text="How cook: ", fg_color="white", width=300, height=80,
                                                   text_color="black", font=("Courier", 18))
                self.how_cook_label.grid(row=0, column=0)
                self.how_cook_show = CTk.CTkLabel(master=self.how_cook_frame, width=700,  text=cook,
                                                  height=80, text_color="black", font=("Courier", 18))
                self.how_cook_show.grid(row=0, column=1)

                self.ingridients_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=50)
                self.ingridients_frame.grid(row=5, column=0, pady=(0, 5))  #
                self.ingridients_label = CTk.CTkLabel(master=self.ingridients_frame, text="Ingridients: ", width=300,
                                                      height=50, text_color="black", font=("Courier", 18))
                self.ingridients_label.grid(row=0, column=0)
                self.ingridients_show = CTk.CTkLabel(master=self.ingridients_frame, width=700, fg_color="white",
                                                     text=list_ingr, height=50, text_color="black", font=("Courier", 18))
                self.ingridients_show.grid(row=0, column=1)

                self.author_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=50)
                self.author_frame.grid(row=6, column=0, pady=(0, 10))  #
                self.author_label = CTk.CTkLabel(master=self.author_frame, text="Author: ", fg_color="white", width=300, height=50,
                                                 text_color="black", font=("Courier", 18))
                self.author_label.grid(row=0, column=0)
                self.author_show = CTk.CTkLabel(master=self.author_frame, width=700,  text=author,
                                                height=50, text_color="black", font=("Courier", 18))
                self.author_show.grid(row=0, column=1)

                self.comboBox_button_frame = CTk.CTkFrame(master=self.full_frame, fg_color="white", width=1000, height=70)
                self.comboBox_button_frame.grid(row=7, column=0)
                self.combobox_like = CTk.CTkComboBox(master=self.comboBox_button_frame,
                                                     values=["no like", "like"],
                                                     command=like_combobox,state="readonly",
                                                     button_color="#6f8e3e",
                                                     dropdown_fg_color="#bdd88b", font=("Courier", 18),
                                                     dropdown_font=("Courier", 18),
                                                     width=300, height=30, button_hover_color="#bdd88b")
                self.combobox_like.grid(row=0, column=0)



    def save_like(self):
        global recipe_add, filename, list_ingr

        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        json_like = json.dumps(recipe_add.likes)
        print(recipe_add.likes)
        about_update = """Update recordRecipe set likes = ? where name = ? """
        data = (json_like, recipe_add.name)
        cur.execute(about_update, data)
        dataBase.commit()
        print("done")
        # self.destroy()








    def open(self):
        self.grab_set()
        self.wait_window()



