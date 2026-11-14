# import json
# from dataclasses import dataclass, asdict, field
#
#
# @dataclass
# class Kitob:
#     nom: str
#     muallif: str
#     yil: int
#     band: bool = False
#
#     def __init__(self) -> str:
#         holat = "band" if self.band else "bo'sh"
#         return f"{self.nom} - {sf.muallif} [{holat}]"
#
#
# class Kutubxona:
#     def __init__(self) -> None:
#         self._kitoblar: list[Kitob] = []
#
#     def qosh(self, kitob: Kitob) -> None:
#         self._kitoblar.append(kitob)
#
#     def qidir(self, matn: str) -> list[Kitob]:
#         m = matn.lower()
#         return [
#             k for k in self._kitoblar
#             if m in k.nom.lower()
#        ]


from datetime import datetime, timedelta
import secrets
import string
from dataclasses import dataclass
import subprocess
import sys


# 1. Bugungi sana va vaqt
print("1.", datetime.now())


# 2. Sanani 13.11.2026 ko'rinishida chiqarish
print("2.", datetime.now().strftime("%d.%m.%Y"))


# 3. Bugundan 30 kun keyingi sana
print("3.", datetime.now() + timedelta(days=30))


# 4. Tug'ilgan sanadan beri necha kun o'tgan
tugilgan_sana = datetime(2010, 5, 15)
bugun = datetime.now()
print("4.", (bugun - tugilgan_sana).days, "kun")


# 5. Yangi yilgacha necha kun qolgan
yangi_yil = datetime(2027, 1, 1)
print("5.", (yangi_yil - bugun).days, "kun")


# 6. 8 belgili tasodifiy parol
belgilar = string.ascii_letters + string.digits
parol = ''.join(secrets.choice(belgilar) for _ in range(8))
print("6. Parol:", parol)


# 7. 6 xonali tasdiqlash kodi
kod = ''.join(secrets.choice(string.digits) for _ in range(6))
print("7. Kod:", kod)


# 8. Book klassi
class Book:
    def init(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(self.title, "-", self.author)

    # 11. print(book)
    def str(self):
        return f"{self.title} - {self.author}"


# 9. Library klassi
class Library:
    def init(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

    # 10. Kitob berish
    def give_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Kitob berildi:", title)
                return
        print("Kitob topilmadi")


book1 = Book("Alpomish", "Xalq og'zaki ijodi")
book2 = Book("O'tkan kunlar", "Abdulla Qodiriy")

library = Library()
library.add_book(book1)
library.add_book(book2)

print("\n8-10. Kitoblar:")
library.show_books()

library.give_book("Alpomish")


# 12. Product klassi
@dataclass
class Product:
    name: str
    price: float

    # 13. Narx + 12%
    @property
    def price_with_tax(self):
        return self.price * 1.12


product = Product("Telefon", 2000000)

print("\n12-13.")
print("Nomi:", product.name)
print("Narxi:", product.price)
print("Soliq bilan:", product.price_with_tax)


# 14. venv yaratish
print("\n14. venv yaratilmoqda...")
subprocess.run([sys.executable, "-m", "venv", "venv"])
print("venv yaratildi.")


# 15. requests o'rnatish
print("\n15. requests o'rnatilmoqda...")
subprocess.run([sys.executable, "-m", "pip", "install", "requests"])

# requirements.txt yaratish
with open("requirements.txt", "w") as fayl:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True
    )
    fayl.write(result.stdout)

print("requirements.txt yaratildi.")