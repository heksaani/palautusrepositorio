from matchers import *

class QueryBuilder:
    def __init__(self, quu = All()):
        self.querly_object = quu

    def build(self):
        return self.querly_object
    
    def playsIn(self, team):
        return QueryBuilder(And(self.querly_object, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.querly_object, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.querly_object, HasFewerThan(value, attr)))
    
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))
    