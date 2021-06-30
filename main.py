from track import Track
from dot import Dot
import random
import time
import math

def findBestDot(listOfDots):
    maxFitness = -math.inf
    bestDot = None
    for dot in listOfDots:
        if dot.getFitness() > maxFitness:
            maxFitness = dot.getFitness()
            bestDot = dot
    return bestDot

def rerunDot(current_dot):
    current_dot.redoDot()
    while not current_dot.isDead():
        track.update(current_dot)
        track.draw()

def nextGen(parentDot, gen):
    childDot = parentDot.clone()
    childDot.mutate()
    wave = 0
    deadDots = []
    while wave < 500:                       # så mange dots vi lager i en gen.
        track.update(childDot)              # oppdaterer dotten vår.
        if childDot.isDead():               # om dotten er død lager vi en ny og øker wave.
            deadDots.append(childDot)
            childDot = parentDot.clone()
            childDot.mutate()
            wave += 1
    return deadDots

if __name__ == "__main__":
    trackSize = 30
    start = [29, 14]
    goal = [0, 14]
    track = Track(trackSize);                # kvadrat med trackSize høyde og tracksize bredde
    track.setGoal(goal[0], goal[1])          # x,y/row,col - for å midstille y ta (trackSize/2) - 1
    initialDot = Dot(goal[0], goal[1])      # init en dot

    # For å starte systemet vårt trenger vi en gruppe med dots som har 100% randome uavhengige egenskaper.
    # Uten denne vil vi ofte sette oss fast i første skrittet.
    dots = 0
    firstGen = []
    while dots < 500:                         # så mange dots vi lager i første generasjon
        track.update(initialDot)
        if initialDot.isDead():               # om init dotten er død lager vi en ny
            firstGen.append(initialDot)
            initialDot = Dot(goal[0], goal[1])
            dots += 1

    reruns = input(" - Do you want reruns of the best dots? y/n: ").lower()
    print(" - Done with initial generation.")
    print(" - Starting child generation with best suited parent.")
    if reruns == "n":
        print("\n\nfitness score\tSteps taken\tReached goal\tTime")

    bestDot = findBestDot(firstGen)
    generations = 0
    generationsMax = 500

    while generations < generationsMax:
        start_time = time.time()
        newDots = nextGen(bestDot, generations)
        bestDot = findBestDot(newDots)
        print("")                           # Aner ikke hvorfor men programmet printer ikke ut noe med mindre den er her.
        if reruns == "y":
            rerunDot(bestDot)
        else:
            bestDot.printInfo()

        if bestDot.getStep() == 25 and bestDot.isWinner():
            print("Reached optimal solution of 25 steps.")
            print("Reaching this point took", round(elapsed_time), "s", "and", gen, "generations.")
            break

        generations += 1
        nextGen(bestDot, generations)

        print("T: ", round(time.time() - start_time, 2), end="")







