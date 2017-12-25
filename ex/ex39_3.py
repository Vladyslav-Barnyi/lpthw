animal = 0
class Dog(object):

    def create(self, color, alias, breed, behaviour):
        print "HAF!"
        global animal
        animal +=   1
        self.color = color
        self.alias = alias
        self.breed = breed
        self.behavior = behaviour

    def delete(self):
        print "MIAY!"
        global animal
        animal += 1
        self.color = None
        self.alias = None
        self.breed = None
        self.behavior = None

    def update(self, color=None, alias=None, breed=None, behaviour=None):
        if color is not None:
            self.color = color
        if alias is not None:
            self.alias = alias
        if breed is not None:
            self.breed = breed
        if behaviour is not None:
            self.breed = breed
