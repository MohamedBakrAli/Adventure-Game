import random
from utils import print_pause, player_choice, clear_screen
from choice import Choice

#
# Game main class
#
class Game:
    def __init__(self):
        # the game intro messages 
        self.__intro_messages = [
            "You are born in an era where the evil demon 'Xi Gong Di' reigns.",
            "Fed up by all the injustice,"
                " you seek to find the only weapon to defeat the demon.",
            "The weapon forged from the powers of Light and Dark.",
            "You embark on your journey with only "
                "a piece of bread and the clothes on your back.",
            "You go out of your house and see "
                "the familiar slum that you grew up in",
        ]
        # game initial state
        self.__state = self.GameState()
        # game main choices
        self.__main_choices = [
            ChinvaoChoice(self.__state),
            ImperialChoice(self.__state)
        ]

    # prints the game story.
    def print_game_story(self):
        for message in self.__intro_messages:
            print_pause(message)

    # starts the game.
    def game(self):
        clear_screen()
        self.print_game_story()
        player_choice(self.__main_choices)
    
    # play the gaim agin
    @staticmethod
    def play_again():
        player_choice([
            Choice("1", "Play agin!", Game().game),
            Choice("2", "Exit game!", exit),
        ])

    #
    # Game state wrapper
    #
    class GameState:
        def __init__(self):
            self.player_weapons = ["Bread"]
            self.player_health = 100
            self.demon_health = 100

        def is_game_over(self):
            return self.player_health <= 0

        def is_player_win(self):
            return self.demon_health <= 0

#
# Go to Chinvao choice.
#
class ChinvaoChoice(Choice):
    def __init__(self, game_state):
        self.code = "1"
        self.message = "Go to Chinvao region."
        self.action = self.go_to_chinvao
        self.game_state = game_state

    def go_to_chinvao(self):
        print_pause("You travel all the way to Chinvao region.")
        print_pause("This is the demon's home town!")
        print_pause("The demon 'Xi Gong Di' sees you!")
        print_pause("'Xi Gong Di' lunges at you! "
                    "His sharp rotten teeth bared to bite!")
        # fight or escape
        player_choice([
            FightChoice(self.game_state),
            EscapeChoice(self.game_state)
        ])

#
# Go to Imperial choice.
#
class ImperialChoice(Choice):
    def __init__(self, game_state):
        self.code = "2"
        self.message = "Go to the Imperial Capital."
        self.action = self.go_to_imperial
        self.game_state = game_state

    def go_to_imperial(self):
        print_pause("You journey to the Imperial Capital.")
        print_pause("Tall structures rise, but behind this facade "
                    "of progress and luxury, evil and corruption exists.")
    
        if 'Bread' in self.game_state.player_weapons:
            print_pause("At the corner, you caught the gaze of an old man.")
            print_pause("The old man hesitates at "
                        "first but approaches you anyway.")
            # food man or ignore him
            player_choice([
                FoodManChoice(self.game_state),
                IgnoreManChoice(self.game_state)
            ])
        else:
            print_pause("You tried to search for the old man again.")
            print_pause("He is nowhere to be seen!")
            # go to Chinvao or Imperial
            player_choice([
                ChinvaoChoice(self.game_state),
                ImperialChoice(self.game_state)
            ])
            
#
# Fight the evil choice.
#
class FightChoice(Choice):
    def __init__(self, game_state):
        self.code = "1"
        self.message = "Fight!"
        self.action = self.fight
        self.game_state = game_state

    def fight(self):
        demon_damage = round(random.randint(0, 50), -1)
        player_damage = round(random.randint(0, 50), -1)
        if 'Chaos Breaker' in self.game_state.player_weapons:
            player_damage = player_damage + 25
            demon_damage = demon_damage / 5
            print_pause("You wield the mighty Chaos Breaker!")
            self.fight_result(player_damage, demon_damage)
        elif 'Bread' in self.game_state.player_weapons:
            player_damage = player_damage / 10
            print_pause("You're fighting a demon using"
                        " a piece of Bread!")
            self.fight_result(player_damage, demon_damage)
        else:
            player_damage = player_damage / 20
            print_pause("You're fighting a demon using"
                        " no weapons!")
            self.fight_result(player_damage, demon_damage)

    def fight_result(self, player_damage, demon_damage):
        # calulate the player health
        self.game_state.player_health -= player_damage
        print_pause("You inflict " + str(player_damage) + " damage!")
        print_pause("Your health is " + str(self.game_state.player_health)
                    + " / 100")
        # calulate the demon health
        self.game_state.demon_health -= demon_damage
        print_pause("Demon inflict " + str(demon_damage) + " damage!")
        print_pause("The demon's health is "
                    + str(self.game_state.demon_health ) + " / 100")

        # check the game state
        if self.game_state.is_game_over():
            print_pause("You have been slain by the Xi Gong Di!")
            print_pause("Evil has continued to ravage the lands.")
            print_pause("GAME OVER!")
            Game.play_again()
        elif self.game_state.is_player_win():
            print_pause("You have successfully slain Xi Gong Di!!")
            print_pause("Finally, the people are free"
                        " from his tyranny!")
            print_pause("Peace has finally returned to your land.")
            print_pause("Thank you for playing!")
            Game.play_again()
        else:
            player_choice([
                FightChoice(self.game_state),
                EscapeChoice(self.game_state)
            ])
#
# Escape from the evil choice.
#
class EscapeChoice(Choice):
    def __init__(self, game_state):
        self.code = "2"
        self.message = "Escape!"
        self.action = self.escape
        self.game_state = game_state
    
    def escape(self):
        print_pause("You ran as fast as you can!")
        print_pause("You barely escaped with your life!")
        # go to Chinvao or Imperial
        player_choice([
            ChinvaoChoice(self.game_state),
            ImperialChoice(self.game_state)
        ])

#
# Foode the poor man choice.
#
class FoodManChoice(Choice):
    def __init__(self, game_state):
        self.code = "1"
        self.message = "Talk to the man."
        self.action = self.food_man
        self.game_state = game_state
    
    def food_man(self):
        print_pause("'Can you spare me some food?' "
                    "the old man said.")
        print_pause("You only have a piece of bread with you "
                    "and nothing else.")
        print_pause("You gave your bread to the man.")
        self.game_state.player_weapons.remove("Bread")
        print_pause("'Thank you kind stranger!' said the old man.")
        print_pause("'Despite not having enough for yourself, "
                    "you still gave your food to me'")
        print_pause("'Truly, you have a good heart. You may be our only hope.'")
        print_pause("'Please take this and defeat the demon "
                    "that has corrupted our land.'")
        print_pause("You have gained the legendary weapon! The Chaos Breaker!")
        self.game_state.player_weapons.append("Chaos Breaker")
        # go to Chinvao or Imperial
        player_choice([
            ChinvaoChoice(self.game_state),
            ImperialChoice(self.game_state)
        ])

#
# Ignore the poor man choice.
#
class IgnoreManChoice(Choice):
    def __init__(self, game_state):
        self.code = "2"
        self.message = "Ignore him."
        self.action = self.ignore_man
        self.game_state = game_state
    
    def ignore_man(self):
        print_pause("You averted your gaze from the old man "
                    "and continued wandering.")
        print_pause("Yet, you feel that there is something about the old man.")
        # go to Chinvao or Imperial
        player_choice([
            ChinvaoChoice(self.game_state),
            ImperialChoice(self.game_state)
        ])


if __name__ == "__main__":
    Game().game()