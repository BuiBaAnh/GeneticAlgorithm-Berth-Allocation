from population import Population
from berth import Berth
from vessel import Vessel


N = 7
size = {1:10, 2:15, 3:6, 4:20, 5:5, 6:15, 7:7, 8:6, 9:11, 10:7, 11: 8, 12:9, 13:10, 14:11}
arrive_time = {1:10, 2:5, 3:0, 4:2, 5:15, 6:12, 7:8,8:6, 9:11, 10:7,11: 8, 12:9, 13:10, 14:11}
process_time = {1:10, 2:9, 3:5, 4:10, 5:5, 6:8, 7:10, 8:6, 9:11, 10:7,11: 8, 12:9, 13:10, 14:11}
weight = {1:1, 2:2, 3:1, 4:3, 5:1, 6:1, 7:3, 8:1, 9:1, 10:1, 11: 1, 12:1, 13:1, 14:1}
break_points = [20, 32]

S = 40
T = 200
num_generations = 40
population_size = 1000
max_population_size = 1e10
max_objective = 2000

if __name__ == "__main__":
    vessels = []
    for i in range(1, N + 1):
        vessel = Vessel(i + 1, size[i], process_time[i], arrive_time[i], weight = weight[i])
        vessels.append(vessel)
        

    p = Population(population_size, S, T, break_points, vessels)
    p.generate_population()
    fit = p.genetic(num_generations, population_size, max_population_size)


    tops = [b.objective for b in p.berths]
    idx = tops.index(min(tops))
    print('Best objective value:', min(tops))
    p.berths[idx].export_berth(is_sub=True)
