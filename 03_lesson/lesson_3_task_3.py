from mailing import Mailing
from address import Address

to_address = Address("456910", "Сатка", "Солнечная", 21, 5)
from_address = Address("666123", "Екатеринбург", "Космонавтов", 7, 197)
track = "Отправление"
cost = "100 рублей"


mailing = Mailing(track, to_address, from_address, cost)

print(mailing)
