import random
import itertools
import operator
import datetime
 
MAX_X = 100
MAX_Y = 100
 
def random_cities(number):
    ''' Generate a number of cities located on random places '''
 
    cities = [ (random.randrange(0, MAX_X),
                random.randrange(0, MAX_Y))
                for i in range(number) ]
 
    return cities
 
def path_lenght(path):
    ''' Get the lenght of a path '''
    lenght = 0
    for i in range(len(path) - 1):
        # Add the distance between two cities
        lenght += abs(complex(path[i][0], path[i][1])
                       - complex(path[i + 1][0], path[i + 1][1]))
 
    return lenght
 
def find_path_bruteforce(cities):
    ''' Find the smallest path using brute force '''
 
    lenghts = []
 
    for path in itertools.permutations(cities, len(cities)):
        # Get the length of the path, adding the returning point
        total_path = path + (path[0],)
        lenght = path_lenght(total_path)
        lenghts.append((total_path, lenght))
 
    # Get minimum
    lenghts.sort(key=operator.itemgetter(1))
    return lenghts[0]
 
def find_path_nearest(cities):
    ''' Find the closest neibour '''
 
    lenghts = []
    for city in cities:
        lenght = 0
        actual_cities = cities[:]
        actual_city = actual_cities.pop(actual_cities.index(city))
        path = [actual_city, ]
        # Find nearest neibour
        while actual_cities:
            min_lenght = []
            for next_city in actual_cities:
                min_lenght.append((next_city, abs(complex(city[0], city[1])
                                                 - complex(next_city[0], next_city[1]))))
            # Get closest neibor
            min_lenght.sort(key=operator.itemgetter(1))
 
            actual_city = min_lenght[0][0]
            lenght += min_lenght[0][1]
            actual_cities.pop(actual_cities.index(actual_city))
            path.append(actual_city)
 
        # Complete the trip with the first city
        path.append(city)
 
        lenghts.append((tuple(path), path_lenght(path)))
 
    # Get minimum
    lenghts.sort(key=operator.itemgetter(1))
    return lenghts[0]
 
if __name__ == '__main__':
    for i in range(3, 10):
        print('Number of cities: ', i)
        cities = random_cities(i)
 
        time1 = datetime.datetime.now()
        path2, lenght_neighbor = find_path_nearest(cities)
        time2 = datetime.datetime.now()
        print( path2, lenght_neighbor)
        time_neighbor = time2 - time1
        print('Time neighbor: ', time_neighbor)
 
        time1 = datetime.datetime.now()
        path1, lenght_brute = find_path_bruteforce(cities)
        time2 = datetime.datetime.now()
        print(path1, lenght_brute)
        time_brute = time2 - time1
        print('Time brute force: ', time_brute)
        print('Diff: ', float(lenght_neighbor - lenght_brute) / lenght_brute * 100, '%')