class Mailing:
    def __init__(self, track, to_addres, from_address, cost):
        self.to_addres = to_addres
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"{self.track} из {self.from_address} в {self.to_addres}"
                f"Стоимость {self.cost} ")
