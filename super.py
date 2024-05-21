class Superhero():
    def __init__(self, hero_name, secret_identity, super_power, arch_enemy):
        self.name = hero_name
        self.identity = secret_identity
        self.power = super_power
        self.enemy = arch_enemy



    def secret(self, secret_lair):
        self.lair = secret_lair
        print(f"{self.name} secret lair is {self.lair}")

    # def transform(self):
    #     print(f"{self.identity} has transform into {self.name}")
