from .audition import Audition

# Actor#auditions returns a list of auditions this actor attended.
# Actor#roles returns a list of roles the actor auditioned for.
# Actor#characters returns a list of strings with all the different character names this actor auditioned for.
# Actor#paychecks returns a list of strings with all the different character names that this actor has been hired for.

class Actor:
    def __init__( self, name ):
        self.name = name

    def auditions( self ):
        #list of all auditions 
        return [x for x in Audition.all if x.actor == self]
    
    def roles( self ):
        return [x.role for x in self.auditions()]
    
    #list of character names *auditioned* for
    def characters( self ):
        character_list = []
        for role in self.roles():
            character_list.append(role.character_name)
        return character_list

    #list of character names *hired* for
    def paychecks( self ):
        character_list = []
        for audition in self.auditions():
            if audition.hired == True:
                character_list.append(audition.role.character_name)
        return character_list

