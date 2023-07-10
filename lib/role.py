from .audition import Audition

class Role:
    def __init__( self, character_name ):
        self.character_name = character_name
    
    def auditions( self ):
        return [x for x in Audition.all if x.role == self]
    
    def actors( self ):
        return [x.actor for x in self.auditions()]
    
    def locations( self ):
        return [x.location for x in self.auditions()]
    
    def silver_screen( self ):
        return [x.role.character_name for x in Audition.all if x.hired]