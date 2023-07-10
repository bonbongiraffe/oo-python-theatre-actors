
class Audition:
    all = []

    def __init__( self, actor, role, location ):
        self.actor = actor
        self.role = role
        self.location = location
        self.hired = None
        Audition.all.append(self)
    
    def call_back( self ):
        self.hired = True