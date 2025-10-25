from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "Galaxy", +79049774583),
    Smartphone("Samsung", "Galaxy F26", +79049784583),
    Smartphone("Samsung", "Galaxy A63", +79049794583),
    Smartphone("Samsung", "Galaxy V73", +79049794683),
    Smartphone("Samsung", "Galaxy B93", +79049794783)
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
