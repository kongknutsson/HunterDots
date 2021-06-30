import random
import math

class Dot():
    # 29 og 14 er bare antagelse at vi har et brett på 30x30. Burde egt byttes.
    def __init__(self, goalx, goaly, maxSteps=100, path=True, posx=29, posy=14):
        self.posx = posx                       # lagrer pos info om dotten
        self.posy = posy
        self.pos = [self.posx, self.posy]
        self._startposx = posx
        self._startposy = posy
        self.step = 0                          # hvor mange skritt doten har tatt
        self.maxSteps = maxSteps               # ... samt max steps før den dør. Denne har MYE å si på runtime til programmet.
        if path == True:                       # brukes for å lagre hvilken vei dotten tar
            self.path = self._createPath()
        else:
            self.path = path
        self.dead = False
        self.fitness = 100
        self.goal = [goalx, goaly]
        self.won = False

    # Får dotten til å bevege seg. Dotten sin bevegelse blir hentet fra self.path
    def move(self):
        if self.dead == False:
            self.step += 1;
            if (self.step == self.maxSteps):
                self._setDead()
                return
            else:
                try:
                    if self.path[self.step] == 0:
                        self._moveUp()
                    elif self.path[self.step] == 1:
                        self._moveDown()
                    elif self.path[self.step] == 2:
                        self._moveLeft()
                    elif self.path[self.step] == 3:
                        self._moveRight()
                except:
                    print("out of bounds. len path is", len(self.path), "step is", self.step)
                    return
        else:
            return

    # Fitness kalkuleres avhengig av skritt tatt, avstand til mål, og om man er i mål.
    def _calculateFitness(self):
        gx = self.goal[0]
        gy = self.goal[1]
        goalDist = calculateDistance(self.posx, self.posy, gx, gy)
        if self.pos == self.goal:
            self.fitness += 20
        self.fitness = self.fitness - goalDist*10
        self.fitness = self.fitness - self.step


    def _setDead(self):
        self.dead = True
        self._calculateFitness()

    # Gir en liten sjanse for å endre på path
    def mutate(self):
        mutateChance = 20
        newPath = []
        for move in self.path:
            if (random.randint(0, 100) <= mutateChance):
                move = random.randint(0,3)
            else:
                move = move
            newPath.append(move)
        self.path = newPath

    def clone(self):
        # Hvis maxStep har sunket så burde vi også senke lengden på pathen til clonen.
        # Det er fordi clone dotten aldri kommer frem til de stepsene som er høyere enn maxStep uansett.
        # Vi legger forsåvidt inn + 5 slik at den faktisk kan ha litt slingringsrom.
        # if (self.step > len(self.path)):
        #     del self.path[-1]

        # Setter dotten sin maxstep til å være vår egen step.
        # Det gjør at for hver dot så beveger vi oss alltid enten like mange steps, eller færre.
        clone = Dot(self.goal[0], self.goal[1], path = self.path)
        return clone

    def _setPath(self, path):
        self.path = path

    # lagrer stedene som dotten skal gå. den går ikke flere skritt enn maxSteps
    # beveger seg randomly opp, ned, venstre, eller høyre.
    def _createPath(self):
        tmp = []
        for x in range(0, self.maxSteps):
            tmp.append(random.randint(0,3))
        return tmp

    def getX(self):
        return self.posx

    def getY(self):
        return self.posy

    def getPos(self):
        return self.pos

    def getStep(self):
        return self.step

    def isDead(self):
        return self.dead

    def redoDot(self):
        self.dead = False
        self.step = 0
        self.posx = self._startposx
        self.posy = self._startposy
        self.pos = [self.posx, self.posy]

    def getFitness(self):
        return round(self.fitness)

    def setWinner(self):
        self.won = True

    def isWinner(self):
        return self.won

    def printInfo(self):
        print("FIT: ", self.getFitness(), end=" \t")
        print("STEPS:", self.getStep(), end="\t")
        if self.isWinner():
            print("WON: True", end="\t")
        else:
            print("WON: - ", end="\t")

    def _moveUp(self):
        self.posx -= 1
        if self.posx == -1:
            self._setDead()
            return
        self.pos = [self.posx, self.posy]
    def _moveDown(self):
        self.posx += 1
        if self.posx == 30:
            self._setDead()
            return
        self.pos = [self.posx, self.posy]
    def _moveLeft(self):
        self.posy -= 1
        if self.posy == -1:
            self._setDead()
            return
        self.pos = [self.posx, self.posy]
    def _moveRight(self):
        self.posy += 1
        if self.posy == 30:
            self._setDead()
            return
        self.pos = [self.posx, self.posy]


def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
