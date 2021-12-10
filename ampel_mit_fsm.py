from ampel import FsmEfe
import time


class AmpelFsm(FsmEfe):
    pass


ampel = FsmEfe()  # ampel = FsmEfe("ROT", "GELB", "GRÜN", 10, 2, 10)


while True:

    ampel.rot_anmachen()

    ampel.gelb_anmachen()

    ampel.grün_anmachen()


