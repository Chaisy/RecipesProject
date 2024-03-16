import json

from CTkMessagebox import CTkMessagebox
from PIL import Image
import tkinter.filedialog
import sqlite3
import customtkinter as CTk
import UserFunctions
import constants
import recipe
import roles
picture_filename = "./UsersPic/user_cat.jpg"
filename = "./projectRecipes/Kitty.jpg"
list_ingr=[]
recipe_add = recipe.Recipe("None", "<5", "", "<100" ,"" ,"" ,"" ,[], [], [])
info = roles.User("", "", "", "", "", "", "")
# dataBase = sqlite3.connect('Userdata2.db')
# cur = dataBase.cursor()
# cur.execute('ALTER TABLE record2 ADD photo blob')
# dataBase.commit()
# class ScrollableCheckBoxFrame(CTk.CTkScrollableFrame):
#     def __init__(self, master, item_list, command=None, **kwargs):
#         super().__init__(master, **kwargs)
#
#         self.command = command
#         self.checkbox_list = []
#
#         dataBase = sqlite3.connect('Userdata2.db')
#         cur = dataBase.cursor()
#         for row in cur.execute("Select * from recordRecipe"):
#             name= row[0]
#             kkal=row[3]
#             time=row[1]
#             photo=row[9]#нужно хранить в стринге и просто название файла для filename
#             with open(filename, 'wb') as file:
#                 file.write(photo)
#             # print(row)
#         #     # self.call_recipe(name,kkal,time,filename,row)
#             dataBase.commit()
#          #циклом со столбиками рамки i j в главном фрейме + переменная количества рецептов у шефа + владелеф рецепта поля
#             for i, item in enumerate(item_list):
#                 for j, item in enumerate(item_list):
#                     recipe = CTk.CTkFrame(self, width=324, height=400,
#                                                fg_color="#dbdbdb")
#
#                     self.call_recipe()
#                     recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))
#                     self.checkbox_list.append(recipe)
#
#
#     def remove_item(self, item):
#         for button_recipe in self.checkbox_list:
#             if item == button_recipe.cget("text"):
#                 button_recipe.destroy()
#                 self.checkbox_list.remove(button_recipe)
#                 return

# def call_recipe(self):  # окошко с мини рецептом
#     # print(j)
#     self.recipe = CTk.CTkFrame(master=self, width=324, height=400,
#                                fg_color="#dbdbdb")
#     self.recipe.grid(row=0, column=0, padx=(0, 15), pady=(0, 15))
#     # self.recipe.grid_propagate(False)
#     self.pic = CTk.CTkImage(dark_image=Image.open(filename), size=(314, 350))
#     self.add_button = CTk.CTkButton(master=self.recipe, width=314, height=350, fg_color="#dbdbdb", text="",
#                                     hover_color="#dbdbdb", font=("Courier", 18), text_color="black",
#                                     image=self.pic)
#     self.add_button.grid(row=0, column=0, sticky="n", pady=(5, 0), padx=(5, 5))
#     self.recipe_name = CTk.CTkLabel(master=self.recipe, text=recipe_add.name, font=("Courier", 18))
#     self.recipe_name.grid(row=1, column=0, sticky="n", pady=(5, 0))
#     self.annotation_label = CTk.CTkLabel(master=self.recipe, text="min: \nkkal: ", font=("Courier", 18))
#     self.annotation_label.grid(row=2, column=0, sticky="w", padx=(60, 0), pady=(5, 0))
#
#     self.t_k_label = CTk.CTkLabel(master=self.recipe, text=f"{recipe_add.time}\n{recipe_add.kcalAll}",
#                                   font=("Courier", 18))
#     self.t_k_label.grid(row=2, column=0, sticky="e", padx=(0, 60), pady=(5, 0))
#
#     self.more_button = CTk.CTkButton(master=self.recipe, width=314, height=50, fg_color="#dbdbdb", text="More",
#                                      hover_color="#bdd88b", font=("Courier", 18), text_color="black",
#                                      )
#     self.more_button.grid(row=3, column=0, sticky="n", pady=(5, 0), padx=(5, 5))





class ChefFunc(UserFunctions.UserInt):
    def __init__(self):
        super().__init__()


        self.geometry("1400x1000")
        self.title("UserInt")
        self.resizable(False, False)

        self.userInt_frame = CTk.CTkFrame(master=self, fg_color="white", width=1400, height=1000)
        self.userInt_frame.grid(row=0, column=0)

        self.logo_text = CTk.CTkLabel(master=self.userInt_frame, width=1400, height=80, font=("Courier", 20), text_color="black",
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
        self.recommendation_button = CTk.CTkButton(master=self.menu_frame, width=233, height=100, fg_color="white",
                                                    hover_color="#6f8e3e", text = "Recommendation",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.Recomendations()
                                                    )
        self.recommendation_button.grid(row=0, column=0)
        self.search_button = CTk.CTkButton(master=self.menu_frame, width=233, height=100, fg_color="white",
                                                    hover_color="#6f8e3e", text = "Search",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.Search()
                                                    )
        self.search_button.grid(row=0, column=1)

        self.my_recipies_button = CTk.CTkButton(master=self.menu_frame, width=233, height=100, fg_color="white",
                                                    hover_color="#6f8e3e", text = "My Recipes",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.My_Recipes(info.Nickname)
                                                    )
        self.my_recipies_button.grid(row=0, column=2)

        self.liked_button = CTk.CTkButton(master=self.menu_frame, width=233, height=100, fg_color="white",
                                                    hover_color="#6f8e3e", text = "Liked",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.Liked(info.Nickname)
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

        self.profile_button = CTk.CTkButton(master=self.menu_frame, width=233, height=100, fg_color="white",
                                                    hover_color="#6f8e3e", text = "Profile",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.Profile()
                                                    )
        self.profile_button.grid(row=0, column=4)

        self.unLogIn_button = CTk.CTkButton(master=self.menu_frame, width=235, height=100, fg_color="#6f8e3e",
                                                    hover_color="#bdd88b", text = "LogOut",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.LogOut()
                                                    )
        self.unLogIn_button.grid(row=0, column=5)

        self.load_all_BD(info.Nickname)

    # def LogOut(self):
    #     self.destroy()
    #     log_in.Log_in()
    #
    # def checkbox_frame_event(self):
    #     print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")
    #
    # def Recomendations(self):
    #     self.info_frame.destroy()
    #     self.recepies_frame.destroy()
    #
    #     self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
    #     self.info_frame.grid(row=1, column=0, sticky="n")
    #
    #     self.info_label = CTk.CTkLabel(master=self.info_frame, width=1400, height=50, font=("Courier", 15),
    #                                    text_color="black",  # 50
    #                                    text="Recommendations")
    #     self.info_label.grid(row=0, column=0)
    #     self.my_recipe_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=720)
    #     self.my_recipe_frame.grid(row=2, column=0, sticky="n")
    #
    #     self.load_all_BD()
    #
    # def Liked(self):
    #     global info
    #     self.info_frame.destroy()
    #     self.recepies_frame.destroy()
    #
    #     self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
    #     self.info_frame.grid(row=1, column=0, sticky="n")
    #
    #     self.info_label = CTk.CTkLabel(master=self.info_frame, width=467, height=50, font=("Courier", 15),
    #                                    text_color="black",  # 50
    #                                    text="Liked")
    #     self.info_label.grid(row=0, column=0)
    #
    #     # self.profile_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="pink", width=1400, height=770)
    #     # self.profile_frame.grid(row=2, column=0, sticky="n")
    #     # self.profile_frame.grid_propagate(False)
    #     i = -1
    #     j = -1
    #     self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
    #                                         height=770)  # height=720)
    #     self.my_recipe_frame.grid(row=2, column=0, sticky="n")
    #     self.my_recipe_frame.grid_propagate(False)
    #     dataBase = sqlite3.connect('Userdata2.db')
    #     cur = dataBase.cursor()
    #     for row in cur.execute("Select * from recordRecipe"):
    #         j += 1
    #         if j % 4 == 0:
    #             i += 1
    #             j = 0
    #         print(i)
    #         name = row[0]
    #         like = row[6]
    #         if info.Nickname in like:
    #             kkal = row[3]
    #             time = row[1]
    #             photo = row[9]
    #             with open(f"./projectRecipes/{name}.jpg", 'wb') as file:
    #                 file.write(photo)
    #             recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
    #                                   fg_color="#dbdbdb")
    #             self.call_recipe(name, time, kkal, f"./projectRecipes/{name}.jpg", i, j)
    #             recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))



    # def Watched(self):
    #     self.recepies_frame.destroy()
    #
    #     self.liked_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
    #     self.liked_frame.grid(row=1, column=0)
    #
    #     self.infoLiked_label = CTk.CTkLabel(master=self.liked_frame, width=1400, height=820, font=("Courier", 10),
    #                                         text_color="black",  # 50
    #                                         text="Here You Can See Recipes, That You Watched")
    #     self.infoLiked_label.grid(row=0, column=0)
    #     self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
    #     self.recepies_frame.grid(row=1, column=0)
    #
    # def Profile(self):
    #     global info, picture_filename
    #     # active_info_profile = info
    #     self.info_frame.destroy()
    #     self.recepies_frame.destroy()
    #
    #     self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
    #     self.info_frame.grid(row=1, column=0, sticky="n")
    #
    #     self.info_label = CTk.CTkLabel(master=self.info_frame, width=467, height=50, font=("Courier", 15),
    #                                    text_color="black",  # 50
    #                                    text="Profile")
    #     self.info_label.grid(row=0, column=0)
    #
    #     self.profile_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=770)
    #     self.profile_frame.grid(row=2, column=0, sticky="n")
    #     self.profile_frame.grid_propagate(False)
    #
    #     self.picProf = CTk.CTkImage(dark_image=Image.open(picture_filename), size=(340, 750))
    #
    #     self.pic_labelProf = CTk.CTkLabel(master=self.profile_frame, text="", image=self.pic)
    #     self.pic_labelProf.grid(row=0, column=0, sticky="w", padx=(10,0), pady=(10,10))
    #
    #     self.menu_frame = CTk.CTkFrame(master=self.profile_frame, width=467, height=770, fg_color="white")
    #     self.menu_frame.grid(row=0, column=1, padx=(50, 0))
    #
    #     ############################
    #     self.nickname_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                       text="Nickname: ")
    #     self.nickname_text.grid(row=0, column=0, pady=(10, 0), sticky="n")
    #     self.nickname = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                  text=info.Nickname)
    #     self.nickname.grid(row=0, column=1, pady=(10, 0), sticky="n")
    #     ############################
    #     self.name_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                   text="Name: ")
    #     self.name_text.grid(row=1, column=0, pady=(10, 0), sticky="n")
    #     self.name = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                              text=info.Name)
    #     self.name.grid(row=1, column=1, pady=(10, 0), sticky="n")
    #     ############################
    #     self.surname_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                      text="Surname: ")
    #     self.surname_text.grid(row=2, column=0, pady=(10, 0), sticky="n")
    #     self.surname = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                 text=info.Surname)
    #     self.surname.grid(row=2, column=1, pady=(10, 0), sticky="n")
    #     ############################
    #     ############################
    #     self.email_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                    text="Email: ")
    #     self.email_text.grid(row=3, column=0, pady=(10, 0), sticky="n")
    #     self.email = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                               text=info.Email)
    #     self.email.grid(row=3, column=1, pady=(10, 0), sticky="n")
    #     ############################
    #     self.role_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                   text="Role: ")
    #     self.role_text.grid(row=4, column=0, pady=(10, 0), sticky="n")
    #     self.role = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                              text=info.Role)
    #     self.role.grid(row=4, column=1, pady=(10, 0), sticky="n")
    #     ###########################
    #     self.info_text = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                                   text="About: ")
    #     self.info_text.grid(row=5, column=0, pady=(10, 0), sticky="n")
    #     self.info = CTk.CTkLabel(master=self.menu_frame, width=467, font=("Courier", 14), text_color="black",
    #                              text=info.About)
    #     self.info.grid(row=5, column=1, pady=(10, 0), sticky="n")
    #
    #     self.entry_info = CTk.CTkEntry(master=self.menu_frame, width=300, height=150, placeholder_text="About me",
    #                                    font=("Courier", 18))
    #     self.entry_info.grid(row=6, column=0, sticky="n", padx=(50, 0), pady=(10, 0))
    #
    #     self.add_button = CTk.CTkButton(master=self.menu_frame, width=300, height=40, hover_color="#bdd88b",
    #                                     fg_color="#6f8e3e", text="Add", font=("Courier", 18),
    #                                     command=lambda: self.add_aboutMe()
    #                                     )
    #     self.add_button.grid(row=6, column=1)
    #
    #     self.add_pic_button = CTk.CTkButton(master=self.menu_frame, width=467, height=50, hover_color="#bdd88b",
    #                                     fg_color="white", text="Change Profile Photo", font=("Courier", 18),
    #                                     text_color="black",
    #                                     command=lambda: self.add_profile_picture()
    #                                     )
    #     self.add_pic_button.grid(row=7, column=0)
    #     # self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
    #     # self.likedResipes_frame.grid(row=1, column=0)
    #
    # def add_aboutMe(self):
    #     global info
    #     adding = self.entry_info.get()
    #     info.About = adding
    #     print(adding)
    #     self.info.configure(text=info.About)
    #     # self.info['text'] = adding
    #     print(self.info.cget('text'))
    #
    #     dataBase = sqlite3.connect('Userdata2.db')
    #     cur = dataBase.cursor()
    #     about_update = """Update record2 set about = ? where nickname = ? """
    #     data = (adding, info.Nickname)
    #     cur.execute(about_update, data)
    #     dataBase.commit()

    # def add_profile_picture(self):
    #     filetypes =( ("Изображение", "*.jpg *.gif *.png"))
    #     global picture_filename
    #     picture_filename = tkinter.filedialog.askopenfilename(title="Открыть файл",
    #                                 initialdir="/home/dari/PycharmProjects/pythonProject1/UsersPic",
    #                                    typevariable=filetypes)
    #     if picture_filename:
    #         print(picture_filename)
    #
    #     self.pic_labelProf.configure(image=CTk.CTkImage(dark_image=Image.open(picture_filename), size=(340, 750)))
    #     with open(picture_filename, 'rb') as file:
    #         blob_data = file.read()
    #     dataBase = sqlite3.connect('Userdata2.db')
    #     cur = dataBase.cursor()
    #     about_update = """Update record2 set photo = ? where nickname = ? """
    #     data = (blob_data, info.Nickname)
    #     cur.execute(about_update, data)
    #     dataBase.commit()
    #     print("done")

    # def Search(self):
    #     self.info_frame.destroy()
    #     self.recepies_frame.destroy()
    #
    #     self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
    #     self.info_frame.grid(row=1, column=0, sticky="n")
    #
    #     self.info_label = CTk.CTkLabel(master=self.info_frame, width=467, height=50, font=("Courier", 15),
    #                                    text_color="black",  # 50
    #                                    text="Search")
    #     self.info_label.grid(row=0, column=0)
    #
    #     self.menu_search = CTk.CTkFrame(master=self.info_frame, fg_color="white", width=1050, height=50)
    #     self.menu_search.grid(row=0, column=1, sticky="n")
    #
    #     self.entry_search = CTk.CTkEntry(master=self.menu_search, width=466, height=50,
    #                                    font=("Courier", 18))
    #     self.entry_search.grid(row=0, column=0)#название и ввод
    #     self.search_button = CTk.CTkButton(master=self.menu_search, width=466, height=50, fg_color="white", text="Search",
    #                                        hover_color="#bdd88b", font=("Courier", 18), text_color="black",
    #                                        command=self.search_recipe)
    #     self.search_button.grid(row=0, column=1)
    #
    #     self.my_recipe_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=770)
    #     self.my_recipe_frame.grid(row=2, column=0, sticky="n")
    #
    # def search_recipe(self):
    #     self.recepies_frame.destroy()
    #     i = -1
    #     j = -1
    #     self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
    #                                         height=770)  # height=720)
    #     self.my_recipe_frame.grid(row=2, column=0, sticky="n")
    #     self.my_recipe_frame.grid_propagate(False)
    #     dataBase = sqlite3.connect('Userdata2.db')
    #     cur = dataBase.cursor()
    #     for row in cur.execute("Select * from recordRecipe"):
    #         j += 1
    #         if j % 4 == 0:
    #             i += 1
    #             j = 0
    #         print(i)
    #         name = row[0]
    #         if self.entry_search.get()==name:
    #             kkal = row[3]
    #             time = row[1]
    #             photo = row[9]
    #             with open(f"./projectRecipes/{name}.jpg", 'wb') as file:
    #                 file.write(photo)
    #             recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
    #                                   fg_color="#dbdbdb")
    #             self.call_recipe(name, time, kkal, f"./projectRecipes/{name}.jpg", i, j)
    #             recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))



    def My_Recipes(self, active_user):
        global info
        info.Nickname = active_user
        self.info_frame.destroy()
        self.recepies_frame.destroy()

        self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
        self.info_frame.grid(row=1, column=0, sticky="n")

        self.info_label = CTk.CTkLabel(master=self.info_frame, width=350, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="My Recipes")
        self.info_label.grid(row=0, column=0)

        self.menu_recipe = CTk.CTkFrame(master=self.info_frame, fg_color="white", width=1050, height=50)
        self.menu_recipe.grid(row=0, column=1, sticky="n")

        self.add_button = CTk.CTkButton(master=self.menu_recipe, width=525, height=50, fg_color="white", text="Add",
                                        hover_color="#bdd88b", font=("Courier", 18), text_color="black",
                                        command=self.add_Recipe_Int)
        self.add_button.grid(row=0, column=0, sticky="w")

        # self.edit_button = CTk.CTkButton(master=self.menu_recipe, width=350, height=50, fg_color="white", text="Edit",
        #                                 font=("Courier", 18),hover_color="#bdd88b", text_color="black")
        # self.edit_button.grid(row=0, column=1, sticky="n")

        self.delete_button = CTk.CTkButton(master=self.menu_recipe, width=525, height=50, fg_color="white",
                                           hover_color="#bdd88b",
                                           text="Delete", command=self.delete_Recipe_Int,
                                        font=("Courier", 18), text_color="black")
        self.delete_button.grid(row=0, column=2, sticky="e")

        self.my_recipe_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=720)
        self.my_recipe_frame.grid(row=2, column=0, sticky="n")

        self.load_Author_BD()


    # def load_all_BD(self):
    #     self.recepies_frame.destroy()
    #     i = -1
    #     j = -1
    #     self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
    #                                         height=770)#height=720)
    #     self.my_recipe_frame.grid(row=2, column=0, sticky="n")
    #     self.my_recipe_frame.grid_propagate(False)
    #
    #     dataBase = sqlite3.connect('Userdata2.db')
    #     cur = dataBase.cursor()
    #
    #     for row in cur.execute("Select * from recordRecipe"):
    #         j += 1
    #         if j % 4 == 0:
    #             i += 1
    #             j = 0
    #         print(i)
    #         name = row[0]
    #         kkal = row[3]
    #         time = row[1]
    #         photo_ind = j
    #         photo = row[9]  # нужно хранить в стринге и просто название файла для filename
    #         with open(f"./projectRecipes/{name}.jpg", 'wb') as file:
    #             file.write(photo)
    #         recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
    #                               fg_color="#dbdbdb")
    #         self.call_recipe(name, time, kkal, f"./projectRecipes/{name}.jpg", i, j)
    #         recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))

    def load_Author_BD(self):
        global info
        self.recepies_frame.destroy()
        i = -1
        j = -1
        self.my_recipe_frame = CTk.CTkFrame(self.userInt_frame, fg_color="white", width=1400,
                                            height=770)#height=720)
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

            author = row[10]
            if info.Nickname == author:
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

    def add_Recipe_Int(self):
        window = Add_Recipe(self)
        user = window.open()
        self.load_Author_BD()

    def delete_Recipe_Int(self):
        window = Delete_Recipe(self)
        user = window.open()
        self.load_Author_BD()

    # def show_full_recipe(self, name):
    #     global recipe_add
    #     recipe_add.name = name
    #     print(f"recipe name -- {name}")
    #     window = Show_Full_Recipe(self)
    #     user = window.open()
    #     # self.load_all_BD()
    #
    #
    # def call_recipe(self, name, time, kcalAll, filenami,i,j):#окошко с мини рецептом
    #     # print(j)
    #     self.recipe = CTk.CTkFrame(master=self.my_recipe_frame, width=324, height=400,
    #                                      fg_color="#dbdbdb")
    #     self.recipe.grid(row=i, column=j,padx=(0, 15), pady=(0, 15))
    #     # self.recipe.grid_propagate(False)
    #     self.pic = CTk.CTkImage(dark_image=Image.open(filenami), size=(314,350))
    #     self.add_button = CTk.CTkButton(master=self.recipe, width=314, height=350, fg_color="#dbdbdb", text="",
    #                                     hover_color="#dbdbdb", font=("Courier", 18), text_color="black",
    #                                     image=self.pic)
    #     self.add_button.grid(row=0, column=0, sticky="n", pady=(5,0), padx =(5,5))
    #     self.recipe_name = CTk.CTkLabel(master=self.recipe, text=name,font=("Courier", 18))
    #     self.recipe_name.grid(row=1, column=0, sticky="n", pady=(5, 0))
    #     self.annotation_label = CTk.CTkLabel(master=self.recipe, text= "min: \nkkal: ",font=("Courier", 18))
    #     self.annotation_label.grid(row=2, column =0, sticky="w", padx = (60,0), pady = (5,0))
    #
    #     self.t_k_label = CTk.CTkLabel(master=self.recipe, text=f"{time}\n{kcalAll}",
    #                                   font=("Courier", 18))
    #     self.t_k_label.grid(row=2, column =0,sticky="e", padx=(0,60),pady = (5,0))
    #
    #     self.more_button = CTk.CTkButton(master=self.recipe, width=314, height=50, fg_color="#dbdbdb", text="More",
    #                                     hover_color="#bdd88b", font=("Courier", 18), text_color="black",
    #                                     command= lambda : self.show_full_recipe(name))
    #     self.more_button.grid(row=3, column=0, sticky="n", pady=(5,0), padx =(5,5))



def save_active_info(act):
    global info
    info = act
    print(info.Nickname, info.Role)

class Add_Recipe(CTk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        def combobox_callback(choise):
            # global info
            global list_ingr
            one=0
            if choise in list_ingr:
                one+=1
            print(one)
            if not one:
                list_ingr.append(self.combobox_add_ingrid.get())
            # info.About = adding
            self.combobox_my_ingrid.configure(values=list_ingr)
            # self.info['text'] = adding

        def clear_list_my_ingridients():
            global list_ingr
            list_ingr=[]
            self.combobox_my_ingrid.configure(values=list_ingr)

        def time_recipe_combobox(choise):
            global recipe_add
            recipe_add.time = self.combobox_time.get()
            print(recipe_add.time)

        def kcal_recipe_combobox(choise):
            global recipe_add
            recipe_add.kcalAll = self.combobox_kcall.get()
            print(recipe_add)


        self.geometry("900x500")
        self.title("Add Recipe")
        self.resizable(False, False)
        global list_ingr, filename
        list_ingr=[]
        filename ="./projectRecipes/Kitty.jpg"
        self.adding_frame = CTk.CTkFrame(master=self, fg_color="white", width=900, height=500)
        self.adding_frame.grid(row=0, column=0)
        self.header_adding = CTk.CTkFrame(master=self.adding_frame, fg_color="#bdd88b", width=900, height=70)
        self.header_adding.grid(row=0, column=0)
        self.logo_adding = CTk.CTkButton(master=self.header_adding, text="Adding", width=900, height=70,
                                        text_color="black", font=("Courier", 18),fg_color="#bdd88b",
                                       hover_color="#6f8e3e", command=self.save_recipe)
        self.logo_adding.grid(row=0, column=0)

        self.data_frame = CTk.CTkFrame(master=self.adding_frame, fg_color="white", width=900, height=430)
        self.data_frame.grid(row=1, column=0)#рамка с данными

        self.photo_frame = CTk.CTkFrame(master=self.data_frame, fg_color="white", width=300, height=430)
        self.photo_frame.grid(row=0, column=0, sticky="w")#рамка для фото и кнопки
        self.pic = CTk.CTkImage(dark_image=Image.open(filename), size=(300,370))

        self.pic_label = CTk.CTkLabel(master=self.photo_frame, text="", image=self.pic)
        self.pic_label.grid(row=0, column=0, sticky="nswe", pady=(0,5))#само фото

        self.add_photo_button = CTk.CTkButton(master=self.photo_frame, width=290, height=50, hover_color="#bdd88b",
                                       fg_color="#6f8e3e", command=self.add_picture,
                                           text="Add Photo",
                                        font=("Courier", 18), text_color="black")
        self.add_photo_button.grid(row=1, column=0)#кнопка

        self.description_frame = CTk.CTkFrame(master=self.data_frame, fg_color="white", width=600, height=430)
        self.description_frame.grid(row=0, column=1, sticky="n", padx=(0,0))#рамка для данных рецепта
        self.name_r = CTk.CTkLabel(master=self.description_frame, text="Name: ",width=70, height=50,
                                        text_color="black", font=("Courier", 18))
        self.name_r.grid(row=0, column=0, sticky="w", padx=(20,0), pady=(10,5))

        self.entry_name = CTk.CTkEntry(master=self.description_frame, width=300, height=50,
                                       font=("Courier", 18))
        self.entry_name.grid(row=0, column=1,padx=(0, 0), pady=(5, 5))#название и ввод



        self.combobox_time = CTk.CTkComboBox(master=self.description_frame,
                                             values=["<5", "10-20", "30", "60",">60"], command=time_recipe_combobox,
                                              button_color="#6f8e3e",state="readonly",
                                             dropdown_fg_color="#bdd88b",font=("Courier", 18),dropdown_font=("Courier", 18),
                                         height=30, button_hover_color="#bdd88b")
        self.combobox_time.grid(row=1, column=0, padx=(20,0),pady=(0, 0))
        self.time_r = CTk.CTkLabel(master=self.description_frame, text=" min", height=50,
                                        text_color="black", font=("Courier", 18))
        self.time_r.grid(row=1, column=1, pady=(0, 5), sticky="w")

        self.combobox_kcall = CTk.CTkComboBox(master=self.description_frame,
                                             values=["<100", "100-300", "300-600","600-1000","1000-1500", ">1500"],
                                             font=("Courier", 18), button_color="#6f8e3e",state="readonly",
                                             dropdown_fg_color="#bdd88b", dropdown_font=("Courier", 18),
                                              button_hover_color="#bdd88b", command=kcal_recipe_combobox,
                                         width=150,height=30)
        self.combobox_kcall.grid(row=1,column=1, sticky="e")
        self.kkcal_r = CTk.CTkLabel(master=self.description_frame, text=" kcal",width=70, height=50,
                                        text_color="black", font=("Courier", 18))
        self.kkcal_r.grid(row=1, column=2, pady=(0, 5), padx=(0,70))

        self.naming_r = CTk.CTkLabel(master=self.description_frame, text="Description: ", height=50,
                                        text_color="black", font=("Courier", 18))
        self.naming_r.grid(row=2, column=0, sticky="w", padx=(20,0), pady=(0,5))

        self.entry_naming = CTk.CTkEntry(master=self.description_frame, width=300, height=50,
                                       font=("Courier", 18))
        self.entry_naming.grid(row=2, column=1,padx=(0, 0), pady=(0, 5))#описание и ввод

        self.how_cook_r = CTk.CTkLabel(master=self.description_frame, text="How to cook: ", height=50,
                                        text_color="black", font=("Courier", 18))
        self.how_cook_r.grid(row=3, column=0, sticky="w", padx=(20,0), pady=(0,5))

        self.entry_how_cook = CTk.CTkEntry(master=self.description_frame, width=300, height=50,
                                       font=("Courier", 18))
        self.entry_how_cook.grid(row=3, column=1,padx=(0, 0), pady=(0, 5))#описание и ввод

        self.ingridients_r = CTk.CTkLabel(master=self.description_frame, text="Products: ", height=50,
                                        text_color="black", font=("Courier", 18))
        self.ingridients_r.grid(row=4, column=0, sticky="w", padx=(20,0), pady=(0,5))

        self.combobox_add_ingrid = CTk.CTkComboBox(master=self.description_frame,
                                             values=constants.ingridients,
                                             command=combobox_callback,state="readonly",
                                                   button_color="#6f8e3e",
                                             dropdown_fg_color="#bdd88b",font=("Courier", 18),dropdown_font=("Courier", 18),
                                        width=300, height=30, button_hover_color="#bdd88b")
        self.combobox_add_ingrid.grid(row=4, column=1,pady=(0, 0))




        self.my_ingridients_r = CTk.CTkLabel(master=self.description_frame, text="Ingridients: ", height=50,
                                        text_color="black", font=("Courier", 18))
        self.my_ingridients_r.grid(row=5, column=0, sticky="w", padx=(20,0), pady=(0,5))
        self.combobox_my_ingrid = CTk.CTkComboBox(master=self.description_frame,
                                            values=["..."], state="readonly",
                                              button_color="#6f8e3e",
                                             dropdown_fg_color="#bdd88b",font=("Courier", 18),dropdown_font=("Courier", 18),
                                        width=300, height=30, button_hover_color="#bdd88b")
        self.combobox_my_ingrid.grid(row=5, column=1,pady=(0, 0))

        self.deleteAll_ingrid_button = CTk.CTkButton(master=self.description_frame,  height=30, hover_color="#bdd88b",
                                       fg_color="#6f8e3e", command=clear_list_my_ingridients,
                                           text="Clear List",
                                        font=("Courier", 18), text_color="black")
        self.deleteAll_ingrid_button.grid(row=6, column=0, sticky="w", pady=(0,5), padx=(20,0))#кнопка



    def add_picture(self):
        filetypes =( ("Изображение", "*.jpg *.gif *.png"))
        global filename
        filename = tkinter.filedialog.askopenfilename(title="Открыть файл",
                                    initialdir="/home/dari/PycharmProjects/pythonProject1/projectRecipes",
                                       typevariable=filetypes)
        if filename:
            print(filename)

        self.pic_label.configure(image=CTk.CTkImage(dark_image=Image.open(filename), size=(300,370)))

    def save_recipe(self):
        global recipe_add, filename, list_ingr
        with open(filename, 'rb') as file:
            blob_data = file.read()
        recipe_add.name=self.entry_name.get()
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        if self.entry_name.get() and self.entry_how_cook.get() and self.entry_naming.get():
            cur.execute(
                "INSERT INTO recordRecipe VALUES (:name, :time, :naming, :kcallAll, :how_to_cook, :ingr, :likes, :views, :rewiew, :photo, :author)",
                {
                    'name': recipe_add.name,
                    'time': recipe_add.time,
                    'naming': self.entry_naming.get(),
                    'kcallAll': recipe_add.kcalAll,
                    'how_to_cook': self.entry_how_cook.get(),
                    'ingr': json.dumps(list_ingr),
                    'likes': "-",
                    'views': "-",
                    'rewiew': "",
                    'photo': blob_data,
                    'author': info.Nickname
                })
            dataBase.commit()
            print("done")
            self.destroy()
        else:
            CTkMessagebox(title="Failed", message=f"Empty Fields")






    def open(self):
        self.grab_set()
        self.wait_window()

class Delete_Recipe(CTk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("400x200")
        self.title("Delete Recipe")
        self.resizable(False, False)

        self.delete_frame = CTk.CTkFrame(master=self, width=400, height=200)
        self.delete_frame.grid(row=0, column=0, padx=(50, 50), pady=(30, 30))

        self.entry_recipe = CTk.CTkEntry(master=self.delete_frame, width=300, height=50,
                                       font=("Courier", 18), placeholder_text="Name Recipe")
        self.entry_recipe.grid(row=0, column=0, pady=(0, 30))  # название и ввод

        self.del_recipe_button = CTk.CTkButton(master=self.delete_frame, text="Delete", width=300, height=50,
                                         text_color="black", font=("Courier", 18), fg_color="#bdd88b",
                                         hover_color="#6f8e3e", command=self.deleting)
        self.del_recipe_button.grid(row=1, column=0)


    def deleting(self):
        global info
        check=0
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from recordRecipe"):
            name = row[0]
            print(f"trying delete --{name}")
            print(f"Enter --{self.entry_recipe.get()}")
            if name == self.entry_recipe.get():
                author =row[10]
                check+=1
                print(f"you --{info.Nickname}")
                if author == info.Nickname:
                    sql_delete_query = """DELETE from recordRecipe where name = ?"""
                    cur.execute(sql_delete_query, (name,))
                    dataBase.commit()
                    print("delete)")
                    self.destroy()
                else:
                    CTkMessagebox(title="Failed", message=f"You are not author of this recipe")
                    break


        if not check:
            CTkMessagebox(title="Failed", message=f"Check your Enter. We cant find this recipe!")

    def open(self):
        self.grab_set()
        self.wait_window()


# class Show_Full_Recipe(CTk.CTkToplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#
#         def like_combobox(choise):
#             global recipe_add, info
#             if self.combobox_like.get()=="like":
#                 recipe_add.likes.append(info.Nickname)
#                 self.save_like()
#
#             else:
#                 if info.Nickname in recipe_add: recipe_add.likes.remove(info.Nickname)
#                 self.save_like()
#
#         global recipe_add, list_ingr
#         dataBase = sqlite3.connect('Userdata2.db')
#         cur = dataBase.cursor()
#         for row in cur.execute("Select * from recordRecipe"):
#             nameBD = row[0]
#             if recipe_add.name == nameBD:
#
#                 time = row[1]
#                 naming = row[2]
#                 kkal = row[3]
#                 cook=row[4]
#                 list_ingr = json.loads(row[5])
#                 author = row[10]
#                 self.geometry("1000x530")
#                 self.title("Recipe")
#                 self.resizable(False, False)
#
#                 self.full_frame = CTk.CTkFrame(master=self, fg_color="white", width=1000, height=530)
#                 self.full_frame.grid(row=0, column=0)
#                 self.header_rec = CTk.CTkFrame(master=self.full_frame, fg_color="#bdd88b", width=1000, height=80)
#                 self.header_rec.grid(row=0, column=0, pady=(0, 5))  #
#                 self.logo_adding = CTk.CTkLabel(master=self.header_rec, text="Recipe", width=1000, height=80,
#                                                 text_color="black", font=("Courier", 18), fg_color="#bdd88b"
#                                                 )
#                 self.logo_adding.grid(row=0, column=0, pady=(0, 5))  #
#                 self.name_label = CTk.CTkLabel(master=self.full_frame, text=nameBD, width=1000, height=50,
#                                                text_color="black", font=("Courier", 16), fg_color="white"
#                                                )
#                 self.name_label.grid(row=1, column=0, pady=(0, 5))
#
#                 self.time_kcal_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=80)
#                 self.time_kcal_frame.grid(row=2, column=0, pady=(0, 5))  #
#                 self.time_show = CTk.CTkLabel(master=self.time_kcal_frame, text=time, width=200, height=50,
#                                               text_color="black", font=("Courier", 18))
#                 self.time_show.grid(row=0, column=0)
#                 self.time_label = CTk.CTkLabel(master=self.time_kcal_frame, text=" min", width=200, height=50,
#                                                text_color="black", font=("Courier", 18))
#                 self.time_label.grid(row=0, column=1, pady=(0, 5))
#                 self.razdelitel_label = CTk.CTkLabel(master=self.time_kcal_frame, text="\u2764\uFE0F", width=200,
#                                                      height=50, text_color="black", font=("Courier", 18))
#                 self.razdelitel_label.grid(row=0, column=2, pady=(0, 5))
#                 self.kcal_show = CTk.CTkLabel(master=self.time_kcal_frame, text=kkal, width=200, height=50,
#                                               text_color="black", font=("Courier", 18))
#                 self.kcal_show.grid(row=0, column=3, pady=(0, 5))
#                 self.kcal_label = CTk.CTkLabel(master=self.time_kcal_frame, text=" kcal", width=200, height=50,
#                                                text_color="black", font=("Courier", 18))
#                 self.kcal_label.grid(row=0, column=4, pady=(0, 5))
#
#                 self.naming_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=50)
#                 self.naming_frame.grid(row=3, column=0, pady=(0, 5))  #
#                 self.naming_label = CTk.CTkLabel(master=self.naming_frame, text="Naming: ", width=300, height=50,
#                                                  text_color="black", font=("Courier", 18))
#                 self.naming_label.grid(row=0, column=0)
#                 self.naming_show = CTk.CTkLabel(master=self.naming_frame, width=700, fg_color="white", text=naming,
#                                                 height=50, text_color="black", font=("Courier", 18))
#                 self.naming_show.grid(row=0, column=1)
#
#                 self.how_cook_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=80)
#                 self.how_cook_frame.grid(row=4, column=0, pady=(0, 5))  #
#                 self.how_cook_label = CTk.CTkLabel(master=self.how_cook_frame, text="How cook: ", fg_color="white", width=300, height=80,
#                                                    text_color="black", font=("Courier", 18))
#                 self.how_cook_label.grid(row=0, column=0)
#                 self.how_cook_show = CTk.CTkLabel(master=self.how_cook_frame, width=700,  text=cook,
#                                                   height=80, text_color="black", font=("Courier", 18))
#                 self.how_cook_show.grid(row=0, column=1)
#
#                 self.ingridients_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=50)
#                 self.ingridients_frame.grid(row=5, column=0, pady=(0, 5))  #
#                 self.ingridients_label = CTk.CTkLabel(master=self.ingridients_frame, text="Ingridients: ", width=300,
#                                                       height=50, text_color="black", font=("Courier", 18))
#                 self.ingridients_label.grid(row=0, column=0)
#                 self.ingridients_show = CTk.CTkLabel(master=self.ingridients_frame, width=700, fg_color="white",
#                                                      text=list_ingr, height=50, text_color="black", font=("Courier", 18))
#                 self.ingridients_show.grid(row=0, column=1)
#
#                 self.author_frame = CTk.CTkFrame(master=self.full_frame, width=1000, height=50)
#                 self.author_frame.grid(row=6, column=0, pady=(0, 10))  #
#                 self.author_label = CTk.CTkLabel(master=self.author_frame, text="Author: ", fg_color="white", width=300, height=50,
#                                                  text_color="black", font=("Courier", 18))
#                 self.author_label.grid(row=0, column=0)
#                 self.author_show = CTk.CTkLabel(master=self.author_frame, width=700,  text=author,
#                                                 height=50, text_color="black", font=("Courier", 18))
#                 self.author_show.grid(row=0, column=1)
#
#                 self.comboBox_button_frame = CTk.CTkFrame(master=self.full_frame, fg_color="white", width=1000, height=70)
#                 self.comboBox_button_frame.grid(row=7, column=0)
#                 self.combobox_like = CTk.CTkComboBox(master=self.comboBox_button_frame,
#                                                      values=["no like", "like"],
#                                                      command=like_combobox,
#                                                      button_color="#6f8e3e",
#                                                      dropdown_fg_color="#bdd88b", font=("Courier", 18),
#                                                      dropdown_font=("Courier", 18),
#                                                      width=300, height=30, button_hover_color="#bdd88b")
#                 self.combobox_like.grid(row=0, column=0)
#
#
#
#     def save_like(self):
#         global recipe_add, filename, list_ingr
#
#         dataBase = sqlite3.connect('Userdata2.db')
#         cur = dataBase.cursor()
#         json_like = json.dumps(recipe_add.likes)
#         about_update = """Update recordRecipe set likes = ? where name = ? """
#         data = (json_like, recipe_add.name)
#         cur.execute(about_update, data)
#         dataBase.commit()
#         print("done")
#         # self.destroy()
#
#
#
#
#
#
#
#
#     def open(self):
#         self.grab_set()
#         self.wait_window()