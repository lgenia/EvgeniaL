from mailing import Mailing

to_adress = (456910, "Сатка", "Солнечная", 21, 5)
from_address = (666123, "Екатеринбург", "Космонавтов", 7, 197)
track = "Отправление"
cost = "100 рублей"


mailing = Mailing(track, to_adress, from_address, cost)

print(mailing)
