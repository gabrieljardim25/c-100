class Atm:
    def __init__(self,cardnumber,pin):
       self.cardnumber = cardnumber
       self.pin = pin

    def check_ballance(self):
        print("Your ballance is 50000")

new_user = Atm(124,424)
new_user.check_ballance()