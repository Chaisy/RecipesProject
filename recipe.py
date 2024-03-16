import sqlite3
import string

con = sqlite3.connect('Userdata2.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS recordRecipe(
                    name text,
                    time number,
                    naming text,
                    kcallAll number, 
                    how_cook text,  
                    ingr text,
                    likes text,
                    views text,
                    rewiew text,
                    photo blob
                )
            ''')
# cur.execute('ALTER TABLE recordRecipe ADD author text')
con.commit()
class Product:
    __slots__ = ['name', 'kcal']

    def __init__(self, name: str, kcal: int) -> None:
        self.name = name
        self.kcal = kcal


class Recipe:
    __slots__ = ['name', 'time', 'naming', 'kcalAll', 'how_to_cook', 'ingredients', 'likes', 'views', 'review', 'photo']

    def __init__(self, name: str, time: str, naming: str, kcalAll: str, how_to_cook: str, views: str,
                 review: string, ingredients: list[Product] = None,  likes: list = None,photo:list[bytes] = None) -> None:
        self.name = name
        self.time =time
        self.naming = naming
        self.kcalAll = kcalAll
        self.likes= likes
        self.views = views
        self.how_to_cook = how_to_cook
        self.review = review
        self.ingredients = ingredients
        self.photo = photo

    def __str__(self):
        return self.name
