class Band:
    band_count = []
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        self.band_count.append(name)
    

    def play_solos(self):
        solos = []
        solos.append(Guitarist.play_solo(self))
        solos.append(Bassist.play_solo(self))
        solos.append(Drummer.play_solo(self))
        return solos

    
    @classmethod
    def to_list(cls):
        return cls.band_count


    
class Musician:
    def __init__(self, name, members=[], instrument=''):
        # super().__init__(name, members)
        self.name = name
        self.members = members
        self.instrument = instrument
        members.append(self)
    def get_instrument(self):
        return f"{self.instrument}"



class Guitarist(Musician):
    def __init__(self, name, members=[], instrument="guitar"):
        super().__init__(name, members, instrument)
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"



class Bassist(Musician):
    def __init__(self, name, members=[], instrument="bass"):
        super().__init__(name, members, instrument)
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def play_solo(self):
        return "bom bom buh bom"



class Drummer(Musician):
    def __init__(self, name, members=[], instrument="drums"):
        super().__init__(name, members, instrument)
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"
