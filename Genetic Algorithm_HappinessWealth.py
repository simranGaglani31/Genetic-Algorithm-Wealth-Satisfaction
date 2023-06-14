import random
import numpy as np 
import pandas as pd
from math import e

# columns
# w = 10  
# M = 100 
# N = 100 
# black dot variable v 
v = 1
# T black dots dispersed across grid when healthy 
T = 100
I = 0 
k = .01021 
# HEALTH 
# starting health
health = 70
#LIFE ENJOYMENT
# L represents life investment of player 
L = 1

#LOOP
n = range(10)
currentPeriod = 0
portion_Solution_Tracker = [] 

for x in n:
    profit = v * T * (health/100)
    # Health and Life Enjoyment Investment Choices 
    random_Choice_Portion = random.random()
    health_Invest = random_Choice_Portion * profit
    life_Enjoy_Invest = abs(profit - health_Invest)
    print("Health investment this period is: ",health_Invest)
    print("Life Enjoyment investment this peirod is: ",life_Enjoy_Invest)
    print("")

    # Keep track of choices for solution
    portion_Solution_Tracker.append(random_Choice_Portion)
    rounded_Solutions = [round(num, 2) for num in portion_Solution_Tracker]

    def regen(health,investment):
        k = .01021
        H=health
        I=investment    
        return (100 * (e**(k*I)/e**(k*I)+(100-H/H)) - H)

    def joy(health, joy_spending):
        c = 464.53
        a = 32 
        L=joy_spending
        return (c * (health/100)*(L/L+a))

# Solution 
print("SOLUTIONS: ", rounded_Solutions)
print("")

# Create Population
population_1 = []
# create a population of 50 arrays
print("Population of 50: ")
times = range(50) 

for i in (times):
    rnum = [random.random() for x in range(10)]
    round_rnum = [round(num, 2) for num in rnum]
    print(round_rnum)
    #Create a repository of the arrays of solution (population of 50)
    population_1.append(round_rnum)

#sample two arrays and assign them to parents 
sampleParent1, sampleParent2  = random.sample(population_1,2)
print("")
print("Parent 1: ", sampleParent1)
print("Parent 2: ", sampleParent2)
print('')

#how to find children 
#crossover function 
def onePointCross(sampleParent1, sampleParent2):
    #to exclude beginning and end index 
    rnum2 = random.randint(1,len(sampleParent1))
    children = sampleParent1[:rnum2] + sampleParent2[rnum2:]
    children2 = sampleParent2[:rnum2] + sampleParent1[rnum2:]
    return(children, children2)

#call the function and pass the inputs through to show 
c1,c2 = onePointCross(sampleParent1,sampleParent2)
print("child 1:",c1)
print("child 2:",c2)
print('')
def mutation(children):
    index = random.randint(0,len(children)-1)
    children[index]=random.random()
    return children

bigLoop = 10000
for x in range(bigLoop):
# Carry out the Mutation 
    mut_children = []
    for _ in range(len(population_1)):
        sampleParent1, sampleParent2  = random.sample(population_1,2)
        child1,child2= onePointCross(sampleParent1,sampleParent2)
        mutantc1 = mutation(child1)
        mutantc2 = mutation(child2)
        mut_children.append(mutantc1)
        mut_children.append(mutantc2)

    # computer does this 10,000 times 
    # Combine parents and children into one list 
    # we have fifty children mutants, and 50 parents
    # 100 total 
    new_population100 = mut_children + population_1

    # survival - fitness 
    def fitness(solution, H, T, v,enjoyment):
        for per in range(len(solution)):
            if H > 0:
                money = v*T*H/100
                Health_Spending = round(money*solution[per],1)
                Joy_Spending = money - Health_Spending
                H = H+regen(H,Health_Spending)-(10+per+1)
                enjoyment+=joy(H,Joy_Spending)
        return enjoyment

    # from that list of 100 pick 2 at random 
    # rand1_fromPop100, rand2_fromPop100  = random.sample(new_population100,2)
    # Test fitness for both; the better one gets put into a whole new population2 
    new_population50 = []
    fiftyMore_times = 50
    for x in range(fiftyMore_times):
        # test1 = fitness(rand1_fromPop100,health,T,v,joy)
        # test2 = fitness(rand2_fromPop100,health,T,v,joy)
        test1, test2 = random.sample(new_population100,2)
        if test1 > test2:
            new_population50.append(test1)
        else:
            new_population50.append(test2)

    # then add 50 new mutants back to original population for a new total of = 100 
    secondPopof100 = new_population50 + population_1

    # from that list of 50 pick 2 at random 
    # rand1_fromPop50, rand2_fromPop50  = random.sample(secondPopof100,2)
    # then use fitness to get the 100 back down to 50 again. 

    second_new_population50 = []
    for x in range(fiftyMore_times):
        # test2 = fitness(rand1_fromPop50,health,T,v,joy)
        # test3 = fitness(rand2_fromPop50,health,T,v,joy)
        test3, test4 = random.sample(secondPopof100,2)
        if test3 > test4:
            new_population50.append(test3)
        else:
            new_population50.append(test4)

    final_parent_list = new_population50

    # calculate fitness for all solutions in final parents list(50)
    # highest fitness is correct solution 
    solution = []
    for i in final_parent_list:
          # mostOptimal = fitness(i,health,T,v,joy)
          # solutionFinal.append(mostOptimal)
# print(solutionFinal)
        optimal = random.sample(final_parent_list,1)
        solution.append(optimal)
    break
final_Solution = random.sample(solution,1)
print('Final Parent List: ')
print(final_parent_list)
print('')
print("-------------------------------------------------")
print('')

print("Optimal Solution after 10,000 Iterations: ", np.round(final_Solution,2))