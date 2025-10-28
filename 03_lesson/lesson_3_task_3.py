from mailing import Mailing

to_address = ("456910", "Сатка", "Солнечная", "21", "5")
from_address = ("666123", "Екатеринбург", "Космонавтов", "7", "197")
track = "Отправление"
cost = "100 рублей"


mailing = Mailing(track, to_address, from_address, cost)

print(mailing)
