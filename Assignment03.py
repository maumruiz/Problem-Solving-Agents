from Objects import *
from CleanupPuzzleEnvironment import CleanupPuzzleEnvironment

if __name__ == "__main__":
    environment = CleanupPuzzleEnvironment()

    ball = Ball()
    environment.add_thing(ball, (1,1))

    print(environment)
