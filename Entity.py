class Entity:

    entityUID = 0

    def __init__(self, name, friendly=False):
        self.name = name
        self.friendly = friendly
        self.entityUID = Entity.entityUID; Entity.entityUID += 1
        self.initiative = 0
        return

