class Book(object):
    price = Price()

    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def __str__(self):
        return "{0} - {1}".format(self.author, self.title)
class Author(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print("getting name")
        return self.__name

    def set_name(self, value):
        print("setting name")
        self.__name = value

    def delete_name(self):
        print("deleting name")
        del self.__name

    name = property(get_name, set_name, delete_name, "Author name")
class Price(object):
    def __init__(self):
        self.__price = 0

    def __get__(self, instance, owner):
        return self.__price

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.__price = value

    def __delete__(self, instance):
        del self.__price

