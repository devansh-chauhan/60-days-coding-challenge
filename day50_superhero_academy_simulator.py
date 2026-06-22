class Hero:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def attack(self):
        return f"{self.name} performs a basic attack!"

    def show_info(self):
        print(f"Hero: {self.name} | Energy: {self.energy}")

class SpeedHero(Hero):

    def attack(self):
        return f"{self.name} uses Lightning Dash ⚡"

class FireHero(Hero):
    def attack(self):
        return f"{self.name} launches Fire Blast 🔥"

class IceHero(Hero):
    def attack(self):
        return f"{self.name} casts Frost Strike ❄️"

hero1 = SpeedHero("FlashX", 100)
hero2 = FireHero("Inferno", 120)
hero3 = IceHero("Glacier", 110)

heroes = [hero1, hero2, hero3]
print("=== Superhero Academy ===\n")
for hero in heroes:
    hero.show_info()
    print(hero.attack())
    print()