import daylight_util
import sure_petcare

curfew = daylight_util.get_curfew()
lock = curfew[0]
unlock = curfew[1]

with sure_petcare.SurePetFlap("your@email", "yourPassword", "device") as api:
    api.update()

api.set_enable_curfew(True, lock, unlock)
