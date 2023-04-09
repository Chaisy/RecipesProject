import string


class Product:
    __slots__ = ['name', 'kcal']

    def __init__(self, name: str, kcal: int) -> None:
        self.name = name
        self.kcal = kcal


class Recipe:
    __slots__ = ['name', 'time', 'naming', 'kcalAll', 'how_to_cook', 'ingredients', 'likes', 'views', 'review']

    def __init__(self, name: str, time: int, naming: str, kcalAll: int, how_to_cook: str, likes: int, views: int,
                 review: string, ingredients: list[Product] = None) -> None:
        self.name = name
        self.time =time
        self.naming = naming
        self.kcalAll = kcalAll
        self.likes= likes
        self.views = views
        self.how_to_cook = how_to_cook
        self.review = review
        self.ingredients = ingredients

    def __str__(self):
        return self.name
