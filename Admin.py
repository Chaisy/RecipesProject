import customtkinter as CTk


class ScrollableCheckBoxFrame(CTk.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            for j, item in enumerate(item_list):
                button_recipe = CTk.CTkButton(self, text=item, width=324, height=400, fg_color="#dbdbdb",
                                              hover_color="#bdd88b")
                if self.command is not None:
                    button_recipe.configure(command=self.command)
                button_recipe.grid(row=i, column=j, padx=(0, 15), pady=(0, 15))
                self.checkbox_list.append(button_recipe)

    def remove_item(self, item):
        for button_recipe in self.checkbox_list:
            if item == button_recipe.cget("text"):
                button_recipe.destroy()
                self.checkbox_list.remove(button_recipe)
                return


class AdminInt(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1400x1000")
        self.title("UserInt")
        self.resizable(False, False)

        self.admfInt_frame = CTk.CTkFrame(master=self, fg_color="white", width=1400, height=1000)
        self.admfInt_frame.grid(row=0, column=0)

        self.logo_text = CTk.CTkLabel(master=self.admfInt_frame, width=1400, height=80, font=("Courier", 20),
                                      text_color="black",
                                      text="Afflatus")
        self.logo_text.grid(row=0, column=0, sticky="n")

        self.recepies_frame = CTk.CTkFrame(master=self.admfInt_frame, fg_color="white", width=1400, height=820)
        self.recepies_frame.grid(row=1, column=0)

        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.recepies_frame, width=1356, height=820,
                                                                 command=self.checkbox_frame_event,
                                                                 fg_color="transparent",
                                                                 item_list=[f"item {i}" for i in
                                                                            range(4)])  # количество окошек
        self.scrollable_checkbox_frame.grid(row=1, column=0, sticky="ns")
        # self.scrollable_checkbox_frame.add_item("new item")

        self.menu_frame = CTk.CTkFrame(master=self.admfInt_frame, width=1400, height=100)
        self.menu_frame.grid(row=2, column=0)
        menu_list = ['Recommendation', 'Search', 'Liked', 'Watched', 'Blocked', 'Complaints', 'Profile']
        for r in range(7):
            self.recommendation_button = CTk.CTkButton(master=self.menu_frame, width=200, height=100, fg_color="white",
                                                       hover_color="#6f8e3e",
                                                       text_color="black", text=menu_list[r], font=("Courier", 18))
            self.recommendation_button.grid(row=0, column=r)

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")



    def Blocked(self):

        self.recepies_frame.destroy()

        self.liked_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
        self.liked_frame.grid(row=1, column=0)

        self.infoLiked_label = CTk.CTkLabel(master=self.liked_frame, width=1400, height=820, font=("Courier", 10), text_color="black",#50
                                     text="Here You Can Find That You Blocked Recipes")
        self.infoLiked_label.grid(row=0, column=0)
        self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
        self.recepies_frame.grid(row=1, column=0)

    def Complaints(self):

        self.recepies_frame.destroy()

        self.liked_frame = CTk.CTkFrame(master=self.userInt_frame, fg_color="white", width=1400, height=820)
        self.liked_frame.grid(row=1, column=0)

        self.infoLiked_label = CTk.CTkLabel(master=self.liked_frame, width=1400, height=820, font=("Courier", 10), text_color="black",#50
                                     text="Here You Can Find Peoples Complaints")
        self.infoLiked_label.grid(row=0, column=0)
        self.likedResipes_frame = CTk.CTkFrame(master=self.liked_frame, fg_color="white", width=1400, height=770)
        self.recepies_frame.grid(row=1, column=0)









