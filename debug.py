import ipdb
from lib import *

# Test your code below...
# Audition: actor, role, location, hired
# Audition#role returns an instance of role associated with this audition.
# Audition#actor returns an instance of actor associated with this audition.
# Audition#call_back() will change the the hired attribute to True.
# Actor: name
# Actor#auditions returns a list of auditions this actor attended.
# Actor#roles returns a list of roles the actor auditioned for.
# Actor#characters returns a list of strings with all the different character names this actor auditioned for.
# Actor#paychecks returns a list of strings with all the different character names that this actor has been hired for.
# Roles: character_name
# Role#auditions returns all of the auditions associated with this role.
# Role#actors returns a list of names from the actors associated with this role.
# Role#locations returns a list of locations from the auditions associated with this role.
# Role.silver_screen returns a unique list of strings for all the character names who have been hired.
c1 = Actor("Paul")
c2 = Actor("Lizzie")
c3 = Actor("Robert")
r1 = Role("Vision")
r2 = Role("Iron Man")
a1 = Audition(c1, r1, "NYC")
a2 = Audition(c1, r2, "DC")
a3 = Audition(c3, r2, "Boston")
# the below line allows us to stop & try stuff!
ipdb.set_trace()