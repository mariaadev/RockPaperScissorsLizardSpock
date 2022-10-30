from enum import Enum, auto

class Result(Enum):
        EQUAL = auto() 
        WINS = auto()
        LOSES = auto()

class Play(object): 
    """
    Represents the play
    """

    def beats(self):
        """
        Returns set with the Object Plays that self can beat
        """
        pass
    
    def description(self): #
        pass 

    def compare(self,other_play): 
        """
        Compares self to other Object plays and returns the result of the comparasion
        """
        if self == other_play: 
            return  Result.EQUAL
        elif other_play in self.beats(): 
            return Result.WINS
        else:
            return Result.LOSES


    def __eq__(self,other): 
        """
        Method __eq__ to define the equality logic for comparing 2 custom objects using the equal operator
        """
        if isinstance(self, other.__class__): 
            return self.description() == other.description() 
        else:
            return False

    def __hash__(self):
        """
        Returns Hash representing self
        """
        return hash(self.description())

class Paper(Play): 
    def beats(self):
        """
        Returns set with the Object Plays that self can beat
        """
        return {Rock(),Spock()}

    def description(self):
        return "Paper"

class Scissors(Play):
    def beats(self):
        """
        Returns set with the Object Plays that self can beat
        """
        return {Paper(),Lizard()}

    def description(self):
        return "Scissors"
    
class Rock(Play):
    def beats(self):
        """
        Returns set with the Object Plays that self can beat
        """
        return {Scissors(),Lizard()}


    def description(self):
        return "Rock"
   
class Lizard(Play):
    def beats(self):
        """
        Returns set with the Object Plays that self can beat
        """
        return {Paper(),Spock()}

    def description(self):
        return "Lizard"
        
class Spock(Play):
    def beats(self):
        """
        Returns set with the Object Plays that self can beat
        """
        return {Scissors(),Rock()}

    def description(self):
        return "Spock"
