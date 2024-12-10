class Character:
    className = "Character"

    def __init__(self, health_points, stamina_points, damage):
        self.health_points = health_points
        self.stamina_points = stamina_points
        self.damage = damage

    def calculate_hits_before_stamina_exhausts(self):
        hits = self.stamina_points // self.damage
        print(f"{self.className} can deal {hits} hits before stamina runs out.")
        return hits

    def _str_(self):
        return f"{self.className}: HP={self.health_points}, Stamina={self.stamina_points}, Damage={self.damage}"


class Enemy(Character):
    className = " _Enemy_"

    def __init__(self, health_points, stamina_points, damage, speed):
        super().__init__(health_points, stamina_points, damage)
        self.speed = speed

    def calculate_hits_to_defeat(self, opponent_damage):
        hits = -(-self.health_points // opponent_damage)
        print(f"{self.className} takes {hits} hits to be defeated.")
        return hits

    def _str_(self):
        return super()._str_() + f", Speed={self.speed}"


class Boss(Character):
    className = "_Boss_"

    def __init__(self, health_points, stamina_points, damage, special_ability):
        super().__init__(health_points, stamina_points, damage)
        self.special_ability = special_ability

    def calculate_hits_to_defeat(self, opponent_damage):
        hits = -(-self.health_points // opponent_damage)
        print(f"{self.className} takes {hits} hits to be defeated.")
        return hits

    def _str_(self):
        return super()._str_() + f", Special Ability={self.special_ability}"


# Example usage:
weak_enemy = Enemy(health_points=50, stamina_points=30, damage=5, speed=10)
boss = Boss(health_points=200, stamina_points=100, damage=20, special_ability="Fireball")

print(weak_enemy)
weak_enemy.calculate_hits_before_stamina_exhausts()
weak_enemy.calculate_hits_to_defeat(opponent_damage=15)

print("\n" + str(boss))
boss.calculate_hits_before_stamina_exhausts()
boss.calculate_hits_to_defeat(opponent_damage=15S