import miiCreator as mc
import miiEvent as me

my_first_mii = mc.miiCreator("Mark Ira", "10-24-2002", "Visionary")
my_second_mii = mc.miiCreator("Another Mii", "1-1-2000", "Visionary")

event = me.miiEvent()

event.mii_talking_event(my_first_mii, my_second_mii)

