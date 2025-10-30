class Mailing:
    def __init__(self, track, to_address, from_address, cost):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"{self.track} из {self.from_address} в {self.to_address}"
                f"Стоимость {self.cost}")
