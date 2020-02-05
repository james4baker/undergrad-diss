Read Me:

This is the readme file for undergrad-diss.

In order to run the GA simply run GA.py (or 'GA - final experiment.py'), simply run it, it will then ask for
some simple inputs from the user before running the GA. If an incorrect value is enter the defualt value will be used.  
At the end it will stop and say "press any key to close window".

The default values for the GA are:  
Cipher: 408  
Cycles: 200 (The number of times the algorthim runs)  
Population: 200 (The pool of possible solutions per cycle)  
Mutation: 8 (The chance each individual chromosome (mapping) has to mutate and change per cycle)  
Crossover: 9 (Dictates the regions within the parent chromosomes that are used for creating the child)

The fitness function uses n-gram analysis (based on the english language and on the letters from the zodiac killer).  
Each string of 1-6 letters has a corresponding value based on the use of it within the letters nd english language
(more common string of letters "e","th","est" will hold a higher value over less common strings "x","tn","spb").  
These values are weigthed based on how long they are, with longer strings being given a higher weight and thus a higher value.  
All the values are then summed up and given as the final result of the fitness function.  
Since the 408 cypher is already solved we can use this as a comparible value for the "fitness" of a solution. 
The 408 value is slightly above 312,000,000. 

When the GA is running it will show the symbol mapping for the best in the generation.  
It will also show the text representation based on the cipher, then it will display the fitness of the above mapping.  
When the GA has finished it will display the best solution of all the cycles done.  
When finished with the GA press ENTER to close it.
