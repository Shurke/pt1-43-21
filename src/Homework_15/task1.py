"""
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле, покупка билета в
транспортной компании, или простая РПГ. Создайте несколько объектов классов, которые описывают
ситуацию. Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -
вызывать методы, взаимодействие объектов и т.д.
"""


from random import randint
from time import sleep


class Character:
    """The basic class Character contain five parameters:
        - health
        - attack
        - defend
        - experience
        - level [TOP level = 5]
        and dictionary which contains hero's level as a key, and list
        with [string name of level, minimum exp points for level up, health points].
        And two class method: 'status' and 'random_skill_up'"""
    SKILL = {1: ['Level 1', 0, 2],
             2: ['Level 2', 2, 4],
             3: ['Level 3', 4, 8],
             4: ['Level 4', 8, 10],
             5: ['TOP level', 16, 16]}

    def __init__(self, health: int, attack: int, defend: int, experience: int = 0, level: int = 1):
        self.health = health
        self.attack = attack
        self.defend = defend
        self.experience = experience
        self.level = level
        for characteristic in (health, attack, defend, experience, level):
            if type(characteristic).__name__ != 'int':
                raise "Incorrect input: characteristic must be a integer!"
            if characteristic < 0:
                raise "Characteristics can't be less than 0!"

    def status(self):
        """This method return characteristics of the hero."""
        return f"The {self.__class__.__name__} status:\n" \
               f"Health: {self.health}\n" \
               f"Attack: {self.attack}\n" \
               f"Defend: {self.defend}\n" \
               f"Exp: {self.experience}\n" \
               f"Level: {self.level}"

    def random_skill_up(self):
        """This method randomize the attack and defence points distribution for element
           of surprise in automatic mod. In real game, we need to provide for the possibility
           of distributing skills in manual mode"""
        flag = 0
        while True:
            chance = randint(0, 1)
            self.attack += chance
            flag += chance
            if flag == 2:
                break
            chance = randint(0, 1)
            self.defend += chance
            flag += chance
            if flag == 2:
                break


class Hero(Character):
    """This is a class of hero. It contain parameters of parent class and
       one unique method 'level_up'."""
    def __init__(self, health, attack, defend, experience=0, level=1):
        super().__init__(health, attack, defend, experience, level)

    def level_up(self):
        """This method used for skills up hero's if points of hero's experience more
           than point of exp in second list element with key 'level + 1' in SKILL dictionary.
           Maximum level is 5, upon reaching this level and subsequent hero gets 2 skill points
           (distributed randomly) and health points are restored."""
        if self.level == 5 and self.experience >= 16:
            self.health = self.SKILL.get(self.level)[2]
            self.random_skill_up()
            self.experience = 0
            print('*** You have the maximum level! ***')
        elif self.experience >= self.SKILL.get(self.level + 1)[1]:
            temp_level = self.SKILL.get(self.level + 1)
            print(f'*** You level UP! Now the hero is {temp_level[0]}! ***')
            self.health = temp_level[2]
            super(Hero, self).random_skill_up()
            self.experience = 0
            self.level += 1


class Enemy(Character):
    """Enemy class inherited from the class Character"""


class SuperBoss(Enemy):
    """Inherited from Enemy class with high parameters"""
    def __init__(self, health=30, attack=5, defend=8):
        super().__init__(health, attack, defend, experience=99, level=99)


class Action:
    """Class describes the logic of interaction between two classes: the classes "attacker"
       and "defender". Damage = attack * random coefficient (from 0 to 4) - defense points
       of the defender. If the Hero defeats the Enemy, he gets 2 experience points and
       the "level_up()" method is also called, which checks if there are enough points
       to increase the experience. The class also displays messages to simulate interactivity."""
    def __init__(self, attacker, defender):
        coefficient = randint(0, 4)
        print(f'{attacker.__class__.__name__} move:')
        if coefficient:
            damage = coefficient * attacker.attack - defender.defend
            if coefficient == 4:
                print('It\'s critic hit!')
            if damage > 0:
                defender.health -= damage
                print(f'{attacker.__class__.__name__} hit and deal {damage} damage!', '\n')
            else:
                print(f'{attacker.__class__.__name__} attacked and can\'t pierce the armor!', '\n')
        else:
            print(f'{attacker.__class__.__name__} missed!', '\n')
        if defender.health <= 0 and attacker.__class__.__name__ == 'Enemy':
            setattr(defender, 'health', 0)
            print('You die!', 'Game Over', defender.status(), sep='\n')
        elif defender.health <= 0 and attacker.__class__.__name__ == 'Hero':
            setattr(defender, 'health', 0)
            if defender.__class__.__name__ == 'SuperBoss':
                print('***** Evil Orc defeated! The victory is yours! Congratulations!!! *****')
                print('Game Over.')
            else:
                print(f'{defender.__class__.__name__} die! You win and get 2 exp point!')
                attacker.experience += 2
                attacker.level_up()


"""
This function for automatic fight hero with enemy
The cycle creates enemy instances from the Enemy class,
the enemy's health is assigned from the SKILL dictionary and
the "attack" and "defend" skills are randomly distributed using the
random_skill_up method from Character Class.

With "Action" class Enemy attacked Hero and Hero attacked Enemy one by one.

When Hero get level 5 - called SuperBoss for final fight!
"""


def run():
    hero = Hero(2, 10, 10)
    enemy = Enemy(1, 1, 1)
    print(hero.status(), '\n')
    while hero.health and hero.level != 5:
        # if the enemy instance is destroyed, a new instance is created.
        if enemy.health == 0:
            enemy = Enemy(1, 1, 1)
            enemy.health = Character.SKILL[hero.level][2]
            enemy.level = hero.level
            print(enemy.status())
            # Enemy get some random points "attack" and "defence" for balance.
            for lvl in range(hero.level - 1):
                enemy.random_skill_up()
        else:
            Action(enemy, hero)
            print()
            if hero.health == 0:
                break
            Action(hero, enemy)
            print()
    # If Hero survived - the final fight is started!
    if hero.health:
        print('\n', "OMG, a huge evil Orc is heading towards you!!!", '\n')
        boss = SuperBoss()
        sleep(2)
        print(hero.status(), '\n')
        print(boss.status(), '\n')
        sleep(3)
        print('Let\'s fight!', '\n')
        while hero.health and boss.health:
            Action(boss, hero)
            sleep(1)
            if hero.health == 0:
                print('After a huge number of great victories, you are not'
                      ' holding back the onslaught of the mighty Orc! '
                      'Your hero dies in an unequal battle!')
                sleep(1)
                print(hero.status())
                print('Try Again!')
                break
            Action(hero, boss)
            sleep(1)
            if boss.health == 0:
                sleep(1)
                print(hero.status())
                break
