import time
import datetime
class FsmEfe:
    def __init__(self):

        self.erste_farbe = "ROT"
        self.zweite_farbe = "GELB"
        self.letzte_farbe = "GRÜN"

        self.state_farbe = "GRÜN"

        self.erste_farbe_zeit = 10
        self.zweite_farbe_zeit = 2
        self.letzte_farbe_zeit = 15

        self.start_letzte_farbe = 0
        self.start_erste_farbe = time.time()
        self.start_zweite_farbe = 0


    def rot_anmachen(self):
        if self.state_farbe  == self.letzte_farbe and self.letzte_farbe_zeit <= time.time() - self.start_letzte_farbe:
            print(self.erste_farbe)
            self.state_farbe  = self.erste_farbe
            self.start_erste_farbe = time.time()

            

    def gelb_anmachen(self):
        if self.state_farbe == self.erste_farbe  and self.erste_farbe_zeit <= time.time() - self.start_erste_farbe:
            print(self.zweite_farbe )
            self.state_farbe  = self.zweite_farbe
            self.start_zweite_farbe = time.time()



    def grün_anmachen(self):
        if self.state_farbe  == self.zweite_farbe and self.zweite_farbe_zeit <= time.time() - self.start_zweite_farbe:
            print(self.letzte_farbe)
            self.state_farbe  = self.letzte_farbe
            self.start_letzte_farbe = time.time()






