#Implemneation of a GA by James Baker

import random
import math
import datetime
from ngram_analysis_original import ngram_analysis as frequency_dicts_orginal
from ngram_analysis_edited import ngram_analysis as frequency_dicts_edited
from symbol_mapping_408 import symbol_mapping_408
from cypher_nums_408 import cypher_408
from cypher_nums_340 import cypher_340

look_up ={0: 'i', 1: 'l', 2: 'i', 3: 'k', 4: 'i', 5: 'i', 6: 'l', 7: 'i', 8: 'n', 9: 'g', 10: 'x', 11: 'n', 12: 'h', 13: 'n', 14: 'i', 15: 'e', 16: 't', 17: 'v', 18: 'e', 19: 't', 20: 'h', 21: 's', 22: 's', 23: 't', 24: 'h', 25: 'e', 26: 'a', 27: 's', 28: 'c', 29: 't', 30: 'h', 31: 'm', 32: 'e', 33: 'r', 34: 'x', 35: 'n', 36: 'h', 37: 'e', 38: 'a', 39: 't', 40: 'w', 41: 't', 42: 'w', 43: 'h', 44: 'n', 45: 'i', 46: 'i', 47: 'w', 48: 'u', 49: 'n', 50: 'w', 51: 'l', 52: 'a'}
class G_A():

	# TODO !!!
	# Looking at local optima and seeing if you can get out of it.
	# REPORT writing.
	# Looking at the avergare as well as the highest, local opitma rather than actually optima.
	# Set up a load of experiments (maybe even the worst).
	# Do it as some graphs :) 

	# The basic set up for the G_A, this can be changed in the settings at the beginning 
	# of a run through. 

	# Having run the true 408 solution through the fitness function gives a value of 374,626,893, the average I get is about 90,000,000.
	# Since the 340 is 0.833 times the size of the 408, the true answer should have a value around 312,189,077.5.

	def __init__(self, cypher,unique_symbols,pop_size, mutation_rate, crossover_points, tourney_size):
		self.cypher = cypher # the zodiacs cypher, represented as a string of numbers, where each number represents a unique symbol.
		self.unique_symbols = unique_symbols # The total number of unique symbols
		self.population_size = pop_size # The population size of the G_A, usualy around 50-100.
		self.current_population = [] # An array of chromosomes to be used in the current epoch
		self.future_population = []  # An array of chromosomes to be used in the next epoch
		self.current_age = 1 # this is the current epoch cycle, always starts at one, usually having around 20-100 cycles.
		self.mutation_rate = mutation_rate # The amount that a new chromosome is mutated as a percentage.
		self.crossover_points = crossover_points # This is how many sections of a parent chromosome is used in multipoint crossover (uniform).
		self.answer = Chromosome(symbol_mapping_408, cypher) # This is to see the value of the 408 answer.
		self.lookup = Chromosome(look_up, cypher_408)
		self.average = 0
		self.tourney_size = tourney_size


	def fitness_function(self,ngram_min, ngram_max, chromosome):

		# These are the wieghted values. I am looking at 2-5 n-grams. The likely-hood of a n-gram appearing is represented by the  
		# following formula, (The value of n=1)/((L-(n-1))/26^n). 
		# L is the length of the cypher text, n is the ngram, 26^n representing the complete possiblilties of an n-gram.
		# This formula gives us the following weighted values. [1,25,652,18750,500000]

		weight_values = [1,25,652,18750,500000,0,0]
		fitness = 0
		n = ngram_min
		while n <= ngram_max:
			n_gram_fitness = 0
			for i in range(0,len(chromosome.cypher_representation)-(n-1)):
				new_ngram = chromosome.cypher_representation[i:(i+(n-1)+1)]
				n_gram_fitness += self.find_fitness(n,new_ngram) 
			n_gram_fitness *= weight_values[n-1]
			fitness += n_gram_fitness
			n += 1
		chromosome.update_fitness(fitness)

	def find_fitness(self, ngram_size, ngram):

		# Give a certain n-gram, this function looks up the value associated with it, from the
		# frequency analysis of the letters.

		fit_value = frequency_dicts_edited[ngram_size-1].get(ngram)
		if fit_value is None:
			fit_value = 0
		return fit_value

	def create_random_population(self, chromosomes_needed, unique_cypher_symbols):

		# Used in the firs run through of the G_A to create a random population.

		chromosome_population = []
		symbol_mapping = {}
		p = 0

		while p < chromosomes_needed:
			for x in range(unique_cypher_symbols):
				symbol_mapping[x] =  chr(97 + random.randrange(0,25)) # creates a number in the range 97-122 ('a'-'z')

			chromosome_population.append(Chromosome(symbol_mapping, self.cypher))
			chromosome_population[p].create_representation(self.cypher)

			p += 1
			symbol_mapping = {}

		return chromosome_population


	def get_parents(self, size):

		# Selects n parents at random and uses a tournement to decide on the best one, picking the one with the highest fitness.

		potential_parents = []
		for x in range(0,size):
			p = random.randrange(0,len(self.current_population))
			potential_parents.append(self.current_population[p])

		parent = potential_parents[0]

		for x in potential_parents:
			if parent.fitness <= x.fitness:
				parent = x
			else:
				pass

		return parent


	def apply_single_point_crossover(self, parent1, parent2, crossover_percent):

		# Applies single point cross over between two parent, (previous selected), and creates to offspring
		# with the crorss_over percent determining how much DNA they get from parent A and B respectivly.

		p1_inheritance_size = math.floor(self.unique_symbols * crossover_percent)
		new_symobl_mapping1 = {}
		new_symobl_mapping2 = {}

		for symbol in range(0,p1_inheritance_size):
			new_symobl_mapping1[symbol] = parent1.symbol_mapping[symbol]
		for symbol in range(self.unique_symbols-1,p1_inheritance_size-1,-1):
			new_symobl_mapping1[symbol] = parent2.symbol_mapping[symbol]
		child1 = Chromosome(new_symobl_mapping1, self.cypher)

		for symbol in range(0,p1_inheritance_size):
			new_symobl_mapping2[symbol] = parent2.symbol_mapping[symbol]
		for symbol in range(self.unique_symbols-1,p1_inheritance_size-1,-1):
			new_symobl_mapping2[symbol] = parent1.symbol_mapping[symbol] 
		child2 = Chromosome(new_symobl_mapping2, self.cypher)

		return [child1,child2]


	def apply_mulitpoint_crossover(self, parent1, parent2):

		# need the number of points to cross over
		# need to get the points at which it would cross over

		# Applies mulitpoint crossover using two previous selected parents, with n amount of cross overs.
		# Noting that it is possible for a crossover point to be the same as another, meaning that a reduced
		# number of cross over point can be used when creating offspring (giving more randomness).

		new_symobl_mapping1 = {}
		new_symobl_mapping2 = {}

		crossover_points = self.get_crossover_points()

		for p in range(0,self.crossover_points+1):

			if p%2 == 0:
				for symbol in range(crossover_points[p],crossover_points[p+1]):
					new_symobl_mapping1[symbol] = parent1.symbol_mapping[symbol]
					new_symobl_mapping2[symbol] = parent2.symbol_mapping[symbol]
			else:
				for symbol in range(crossover_points[p],crossover_points[p+1]):
					new_symobl_mapping1[symbol] = parent2.symbol_mapping[symbol]
					new_symobl_mapping2[symbol] = parent1.symbol_mapping[symbol]

		child1 = Chromosome(new_symobl_mapping1, self.cypher)
		child2 = Chromosome(new_symobl_mapping2, self.cypher)

		return [child1,child2]


	def get_crossover_points(self):

		# This creates the list of points that the offspring will get from parent A and B.
		# This is completely random so could end up with 80%/20% split or 50%/50%s

		crossover_mapping = []

		crossover_mapping.append(0)						# Gives a line at the start.
		crossover_mapping.append(self.unique_symbols) 	# Gives a line at the end.
		for x in range(0,self.crossover_points):
			crossover_mapping.append(random.randrange(0,self.unique_symbols))
		crossover_mapping.sort()
		#print(crossover_mapping)
		return crossover_mapping


	def make_offspring(self, tournament_size):

		# Creates offspring for the next generation of Chromosomes, does this by using a tournement to select
		# 2 parents then calls the appropraite cross_over technique, applies mutation and adds the new offspring
		# to the next generation.

		parent1 = self.get_parents(tournament_size)
		parent2 = self.get_parents(tournament_size)

		# offspring1,offspring2 = self.apply_single_point_crossover(parent1,parent2, 0.75)

		offspring1,offspring2 = self.apply_mulitpoint_crossover(parent1,parent2)

		offspring1 = self.apply_mutation(offspring1)
		offspring2 = self.apply_mutation(offspring2)

		self.future_population.append(offspring1)
		self.future_population.append(offspring2)


	def find_most_fit_chromosomes(self):

		# Looks through the fitness of all of the current population and returns the fitest in this generation.

		fitest = self.current_population[0]
		for chromosome in self.current_population:
			if fitest.fitness < chromosome.fitness: # The higher the fitness the better.
				fitest = chromosome
			else:
				pass
		return fitest


	def record_data(self, chromosome):
		print("This is the fitest chromosome:")
		chromosome.display()
		print('\n')
		#this function will record the best chromosome of an epoch, in a text file, in future will set up graphs to see the progress.
		pass


	def find_average(self):
		# Finds the average fitness for the population.
		total = 0
		for x in range(0,len(self.current_population)):
			total += self.current_population[x].fitness
		self.average = total/len(self.current_population)


	def run_epoch(self):

		# Runs a single cycle of the G_A
		if self.current_age%30 == 0:
			self.mutation_rate = 0.18
		else:
			self.mutation_rate = 0.04
		#print(self.current_age%5)
		#print(self.mutation_rate)

		if self.current_age == 1:

#				print('The look up: \n')
#				self.lookup.create_representation(self.cypher)
#				self.fitness_function(2,5,self.lookup)
#				self.lookup.display()
#				print('\n')
#				input()


#				self.answer.create_representation(self.cypher)
#				self.fitness_function(2,5,self.answer)
#				self.answer.display()
#				input()

				self.current_population = self.create_random_population(self.population_size, self.unique_symbols)

		for chromosome in self.current_population:
			self.fitness_function(2,5,chromosome)
		
		fitest = self.find_most_fit_chromosomes()
		
		for x in range(int(len(self.current_population)/2)):
			y = int(self.tourney_size*len(self.current_population))
			if y == 0:
				y = 1
			self.make_offspring(y)

		self.record_data(fitest)
		self.find_average()
		print('The average was: ')
		print(self.average)
		self.current_age += 1
		self.current_population = self.future_population
		self.future_population = []
		return([fitest,self.average])
		# run again.


	def apply_mutation(self, child):

		# Gets a child chromosome and applies mutations to it based on the mutation rate, defined in the G_A.

		num_to_mutate = int(math.floor(self.unique_symbols * self.mutation_rate) + 1)
		mutate_mapping = []

		for x in range(0, num_to_mutate):
			mutate_mapping.append(random.randrange(0,self.unique_symbols))

		child.apply_mutation(mutate_mapping)
		child.create_representation(self.cypher)

		return child

	def apply_splicing(): # future
		pass



class Chromosome():

	# The Chromosome class, the representation of the cypher mapping key.

	def __init__(self, symbol_mapping, cypher):
		self.symbol_mapping = symbol_mapping # A mapping of the symbol to the correspoding letter
		self.cypher_representation = '' # The represnttion of the cypher when used with the symbol mapping as a key
		self.fitness = 0 # fitness of the chromosome (higher is better)

	def create_representation(self, cypher_text):
		# each unique symbol has a unique number for it's representation.
		# This take the symobl mapping and applies it to the cypher, giving us a potential
		# sollution, this will then have the fitness function applied to it later on.

		cy_rep = ''
		for t in range(0,len(cypher_text)):
			symbol = cypher_text[t]-1
			cy_rep += str(self.symbol_mapping.get(symbol))

		self.cypher_representation = cy_rep 

	def update_fitness(self, new_fitness):
		self.fitness = new_fitness
		#print(self.fitness)

	def display(self):
		# This displys the chromosome, useful to see quick information about it.
		print(self.symbol_mapping)
		print(self.cypher_representation)
		print(self.fitness)

	def apply_mutation(self, symbols_to_mutate): 
		
		# Applies the mutation to the chromosome, it is possible for the same mapping to be mutated twice (adds to randomness).

		for x in range(0, len(symbols_to_mutate)):
			new_mapping =  chr(97 + random.randrange(0,25))
			self.symbol_mapping[symbols_to_mutate[x]] = new_mapping


def find_most_fit(chromosomes):
	# Copied from above, to be used outside the G_A.
	fitest = chromosomes[0]
	for chromosome in chromosomes:
		if fitest.fitness < chromosome.fitness:
			fitest = chromosome
		else:
			pass
	return fitest

def get_most_common(array_of_dicts, unique_keys):

	# look at each of the keys and get the most common.
	# do this with another dict incrementing
	most_common = {}
	for y in range(0,unique_keys):
		place_holder_dict = {}

		for current_dict in array_of_dicts:
			if current_dict.symbol_mapping[y] in place_holder_dict:
				place_holder_dict[current_dict.symbol_mapping[y]] += 1
			else:
				place_holder_dict[current_dict.symbol_mapping[y]] = 1
		best = 0
		for key in place_holder_dict:
			if place_holder_dict.get(key) >= best:
				best = place_holder_dict.get(key)
				value = key
		most_common[y] = value
	return most_common


		# go through the dicts and get the most common one letter ('letter': value)
		# go through the dicts and count the correct ones 
		# look through the ones and choose the best
		

def get_name():
	name = ''
	name += prefix
	name += '_'
	name += str(datetime.datetime.today())[0:10]
	name += '_'
	name += str(number)
	return name


def save_data_csv(fitest, average):
		name = get_name()
		name += '.csv'
		name = str(name)
		print(name)
		with open(name, 'w') as new_csv:
			new_csv.write('Fitest')
			new_csv.write(',')
			new_csv.write('Average')
			new_csv.write('\n')
			for x in range(len(fitest)):
				new_csv.write(str(fitest[x]))
				new_csv.write(',')
				new_csv.write(str(average[x]))
				new_csv.write('\n')

def save_top_mappings(list_of_dicts):
	name = get_name()
	name += '_mappings.py'
	with open(name, 'w') as new_file:
		new_file.write('top_mappings = [ ')
		for x in list_of_dicts:
			new_file.write( str(x.symbol_mapping) )			
			new_file.write(',')
			new_file.write('\n')
		new_file.write(']')
		new_file.close()


def main(number_of_epochs, pop_size):

	# The main function, runs the entire of the program, ToDo: add better UI so that different
	# options may be picked without changing the source code.

	# What choices could you have ??
	# - Cypher
	# - Pop
	# - Epochs
	# - Number of re-runs
	# - mutation
	# - Cross-over
	# - Cross-over points.
	# - Default option ??
	try:
		x = int(input("Which Cypher would you like you to use, 408 or 340 (enter number):"))
		if x == 340:
			print("Cypher set to 340")
			cypher = cypher_340
			no_of_unique_symbols = 62
		else: 
			print("Cypher set to 408")
			cypher = cypher_408
			no_of_unique_symbols = 53
	except:
		print("Input error, Cypher set to 408")
		cypher = cypher_408
		no_of_unique_symbols = 53

	try:
		mutation = float(int(input("Enter the mutation rate (As a %, i.e. 8)(Default 8):"))/100)
	except:
		print("Invalid input, mutation set to 8%")
		mutation = 0.08

	try:
		crossover = int(input("Enter the number of crossovers (Default 9):"))
	except:
		print("Invalid input, crossover set to 9")
		crossover = 9

	try:
		tourney_size = float(int(input("Enter the tourmament size (As a percentage of the population)(Default 10):"))/100)
	except:
		print("Invalid input, tournament size set to 10%")
		tourney_size = 0.10

	fitest = []
	tops = []
	averages = []
	
	p = G_A(cypher,no_of_unique_symbols, pop_size, mutation, crossover, tourney_size)
	print('Start')

	for x in range(0, number_of_epochs):
		print(x+1)
		results = p.run_epoch()
		tops.append(results[0].fitness)
		fitest.append(results[0])
		averages.append(results[1])	

	print('\n')
	print('Most fit of all was: \n')
	y = find_most_fit(fitest)
	y.display()
	save_data_csv(tops,averages)
	save_top_mappings(fitest)
	return y


# run through a couple of hundred time, find the best of the best
# see the most common letters used and see what (if anything) pops up.
# runs = 100
best_of_best = []
#for x in range(50):
number = 1
# for experimentation I will use the basis of 200 pop, 200 cycles, 8% mutation, 9 cross over points, a tournemt size of 8% of pop (looking at top 20%)
try:
	cycles = int(input("Enter number of Cycles for the GA (Default 200): "))
except:
	print("Invalid input, cycles set to 200")
	cycles = 200

try:
	pop = int(input("Enter the populaiton size (Default 200): "))
except:
	print("Invalid input, population size set to 200")
	pop = 200

try:
	total_runs = int(input("Enter times you want the GA to run (Defualt 1): "))
except:
	print("Invalid input, total runs set to 1")
	total_runs = 1

prefix = input(str("Enter the prefix of the file name you want to save the results as (files already given the prefix will cause an error when saving): "))

for x in range(0,total_runs):
	best_of_best.append(main(cycles, pop))
	number += 1

#look_up = get_most_common(best_of_best, 53)
#
#print(look_up)

print('The Best Were: \n')
p = 1
for x in best_of_best:
	print(p)
	x.display()
	print('\n')
	p += 1
input(str("Press any key to close window"))
