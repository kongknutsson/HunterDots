import os
import time

class Track():
    def __init__(self, size):
        self.map = []
        self.goal = [0, 0]  # goal er default i øverste venstre hjørne.
        for row in range(0, size):
            self.map.append([])
            for col in range(0, size):
                self.map[row].append(".")

    # henter ut selve map listen som Track-classen kontrollerer.
    def getMap(self):
        return self.map

    # erstatter gamle goal med "." gir ny pos og setter nye goal til "X"
    def setGoal(self, x, y):
        self.map[self.goal[0]][self.goal[1]] = "."
        self.goal[0] = x
        self.goal[1] = y
        self.map[x][y] = "x"

    # returnerer goal
    def getGoal(self):
        return self.goal

    # tegner tracken, samt goal om goal er satt.
    def draw(self):
        time.sleep(0.00)
        clear = lambda: os.system("cls")
        clear()
        print("\n"*10)
        for row in self.map:
            print(""*5, end="")
            for col in row:
                print(col + " ", end="")
            print()
        print()

    # oppdaterer dotten i tracken
    def update(self, dot):
        #visker ut der den var
        self.map[dot.getX()][dot.getY()] = "."
        #flytter den til nytt sted
        dot.move()
        #om den døde av å flyttes så avslutter vi
        if dot.isDead():
            return
        #om ikke tegnes den på nytt
        self.map[dot.getX()][dot.getY()] = "ø"
        #om der den tegnes er goal, så vinner den, og dør.
        if dot.getPos() == self.getGoal():
            dot._setDead()
            dot.setWinner()

