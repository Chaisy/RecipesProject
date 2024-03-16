import sqlite3
from itertools import count
from tkinter import ttk

import customtkinter as CTk
from CTkMessagebox import CTkMessagebox

import ChefFunctions
import UserFunctions
import recipe
import roles

picture_filename = "./UsersPic/user_cat.jpg"
filename = "./projectRecipes/Kitty.jpg"
list_ingr=[]
recipe_add = recipe.Recipe("None", "<5", "", "<100" ,"" ,"" ,"" ,[], [], [])
info = roles.User("", "", "", "", "", "", "")

# class ScrollableCheckBoxFrame(CTk.CTkScrollableFrame):
#     def __init__(self, master, item_list, command=None, **kwargs):
#         super().__init__(master, **kwargs)
#
#         self.command = command
#         self.checkbox_list = []
#         for i, item in enumerate(item_list):
#             for j, item in enumerate(item_list):
#                 button_recipe = CTk.CTkButton(self, text=item, width=324, height=400, fg_color="#dbdbdb",
#                                               hover_color="#bdd88b")
#                 if self.command is not None:
#                     button_recipe.configure(command=self.command)
#                 button_recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))
#                 self.checkbox_list.append(button_recipe)
#
#     def remove_item(self, item):
#         for button_recipe in self.checkbox_list:
#             if item == button_recipe.cget("text"):
#                 button_recipe.destroy()
#                 self.checkbox_list.remove(button_recipe)
#                 return


class AdminInt(ChefFunctions.ChefFunc):
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
        self.recommendation_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                                   hover_color="#6f8e3e", text="Recommendation",
                                                   text_color="black", font=("Courier", 18),
                                                   command=lambda: self.Recomendations()
                                                   )
        self.recommendation_button.grid(row=0, column=0)
        self.search_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                           hover_color="#6f8e3e", text="Search",
                                           text_color="black", font=("Courier", 18),
                                           command=lambda: self.Search()
                                           )
        self.search_button.grid(row=0, column=1)

        self.my_recipies_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                                    hover_color="#6f8e3e", text = "My Recipes",
                                                    text_color="black", font=("Courier", 18),
                                                    command= lambda : self.My_Recipes(info.Nickname)
                                                    )
        self.my_recipies_button.grid(row=0, column=2)

        self.roles_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                                hover_color="#6f8e3e", text="Roles",
                                                text_color="black", font=("Courier", 18),
                                                command=lambda: self.Roles()
                                                )
        self.roles_button.grid(row=0, column=3)

        self.liked_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                          hover_color="#6f8e3e", text="Liked",
                                          text_color="black", font=("Courier", 18),
                                          command=lambda: self.Liked(info.Nickname)
                                          )
        self.liked_button.grid(row=0, column=4)
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

        self.profile_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                            hover_color="#6f8e3e", text="Profile",
                                            text_color="black", font=("Courier", 18),
                                            command=lambda: self.Profile()
                                            )
        self.profile_button.grid(row=0, column=5)

        self.unLogIn_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="#6f8e3e",
                                            hover_color="#bdd88b", text="LogOut",
                                            text_color="black", font=("Courier", 18),
                                            command=lambda: self.LogOut()
                                            )
        self.unLogIn_button.grid(row=0, column=6)

        self.load_all_BD(info.Nickname)

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")



    # def Blocked(self):
    #
    #     self.recepies_frame.destroy()
    #
    #     self.liked_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
    #     self.liked_frame.grid(row=1, column=0)
    #
    #     self.infoLiked_label = CTk.CTkLabel(master=self.liked_frame, width=1400, height=820, font=("Courier", 10), text_color="black",#50
    #                                  text="Here You Can Find That You Blocked Recipes")
    #     self.infoLiked_label.grid(row=0, column=0)
    #     self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
    #     self.recepies_frame.grid(row=1, column=0)
    #
    # def Complaints(self):
    #
    #     self.recepies_frame.destroy()
    #
    #     self.liked_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
    #     self.liked_frame.grid(row=1, column=0)
    #
    #     self.infoLiked_label = CTk.CTkLabel(master=self.liked_frame, width=1400, height=820, font=("Courier", 10), text_color="black",#50
    #                                  text="Here You Can Find Peoples Complaints")
    #     self.infoLiked_label.grid(row=0, column=0)
    #     self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
    #     self.recepies_frame.grid(row=1, column=0)
    def Roles(self):
        self.info_frame.destroy()
        self.recepies_frame.destroy()

        self.info_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=50)
        self.info_frame.grid(row=1, column=0, sticky="n")

        self.info_label = CTk.CTkLabel(master=self.info_frame, width=700, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="Roles")
        self.info_label.grid(row=0, column=0)

        self.role_button = CTk.CTkButton(master=self.info_frame, width=700, height=50, font=("Courier", 15),
                                       text_color="black",  # 50
                                       text="Roles", fg_color="white",hover_color="#bdd88b",command=self.change_role_newWindow)
        self.role_button.grid(row=0, column=1)
        self.recepies_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=720)
        self.recepies_frame.grid(row=2, column=0, sticky="n")
        self.recepies_frame.grid_propagate(False)

        set = ttk.Treeview(self.recepies_frame)
        set.grid(row=0, column=0)

        set['columns'] = ('Nickname', 'Role', 'Name','Surname','Email','About')
        set.column("#0", width=0, stretch=False)
        set.column("Nickname", anchor="center", width=233)
        set.column("Role", anchor="center", width=233)
        set.column("Name",anchor="center", width=233)
        set.column("Surname", anchor="center", width=233)
        set.column("Email", anchor="center", width=233)
        set.column("About",anchor="center", width=235)



        set.heading("#0", text="", anchor="center")
        set.heading("Nickname", text="Nickname", anchor="center")
        set.heading("Role", anchor="center", text="Role")
        set.heading("Name",anchor="center",  text="Name")
        set.heading("Surname", anchor="center",  text="Surname")
        set.heading("Email", anchor="center",  text="Email")
        set.heading("About",anchor="center", text="About")

        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()

        for row in cur.execute("Select * from record2"):
            nickname= row[0]
            role = row[1]
            name = row[2]
            surname = row[3]
            email = row[4]
            about = row[6]
            set.insert(parent='', index='end', text='',
                   values=(nickname, role, name, surname,email,about))

        dataBase.commit()
        # # data
        # data = [
        #     [1, "Jack", "gold"],
        #     [2, "Tom", "Bronze"]
        #
        # ]
        #
        # global count
        # count = 0
        #
        # for record in data:
        #     set.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
        #
        #     count += 1
        #
        # Input_frame = ttk.Frame(master=self.my_recipe_frame)
        # Input_frame.grid(row=1, column=0)
        #
        # id = ttk.Label(Input_frame, text="ID")
        # id.grid(row=0, column=0)
        #
        # full_Name = ttk.Label(Input_frame, text="Full_Name")
        # full_Name.grid(row=0, column=1)
        #
        # award = ttk.Label(Input_frame, text="Award")
        # award.grid(row=0, column=2)
        #
        # id_entry = ttk.Entry(Input_frame)
        # id_entry.grid(row=1, column=0)
        #
        # fullname_entry = ttk.Entry(Input_frame)
        # fullname_entry.grid(row=1, column=1)
        #
        # award_entry = ttk.Entry(Input_frame)
        # award_entry.grid(row=1, column=2)
        #
        # def input_record():
        #     global count
        #
        #     set.insert(parent='', index='end', iid=count, text='',
        #                values=(id_entry.get(), fullname_entry.get(), award_entry.get()))
        #     count += 1
        #
        #     id_entry.delete(0, "END")
        #     fullname_entry.delete(0, "END")
        #     award_entry.delete(0, "END")
        #
        # # button
        # Input_button = ttk.Button(master=self.my_recipe_frame, text="Input Record", command=input_record)
        #
        # Input_button.grid(row=2, column=0)

    def change_role_newWindow(self):
        window = Change_Role(self)
        user = window.open()
        # self.load_Author_BD()

def save_active_info(act):
    global info
    info = act
    print(info.Nickname, info.Role)

class Change_Role(CTk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("400x200")
        self.title("Admin Role")
        self.resizable(False, False)

        self.role_frame = CTk.CTkFrame(master=self, width=400, height=200)
        self.role_frame.grid(row=0, column=0, padx=(50,50), pady=(30,30))

        self.entry_nick = CTk.CTkEntry(master=self.role_frame, width=300, height=50,
                                       font=("Courier", 18), placeholder_text="User Nickname")
        self.entry_nick.grid(row=0, column=0, pady=(0, 30))#название и ввод

        self.role_adding = CTk.CTkButton(master=self.role_frame, text="Admin", width=300, height=50,
                                        text_color="black", font=("Courier", 18),fg_color="#bdd88b",
                                       hover_color="#6f8e3e", command=self.check_nick_give_role)
        self.role_adding.grid(row=1, column=0)

    def check_nick_give_role(self):
        check=0
        dataBase = sqlite3.connect('Userdata2.db')
        cur = dataBase.cursor()
        for row in cur.execute("Select * from record2"):
            nickname = row[0]
            print(f"trying change --{nickname}")
            print(f"Enter --{self.entry_nick.get()}")
            if nickname == self.entry_nick.get():
                check+=1
                role = row[1]
                print(f"trying change --{nickname}")
                if role =="C":
                    role_admin = "A"
                    about_update = """Update record2 set role = ? where nickname = ? """
                    data = (role_admin, nickname)
                    cur.execute(about_update, data)
                    dataBase.commit()
                    print("changed)")
                    self.destroy()
                else:
                    CTkMessagebox(title="Failed", message=f"Check your Enter. Its just user or admin already.")
                    break

        if not check:
            CTkMessagebox(title="Failed", message=f"Check your Enter. We cant find this user!")


    def open(self):
        self.grab_set()
        self.wait_window()












