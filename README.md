Read Me:

This is the readme file for undergrad-diss.

There are four main areas to the file system.

The top level (where this file is kept) and the three directories.

'findings' contains all the data gathered from the experiments, each experiment is labelled 
and has a corresponding '.py' file contatining the best symbol mappings and a '.csv' file that 
contains the fitnesses of the average and best at each generation.

'letters_orginal' contains all the letters in their original state, also included is the 
letter_analysis.py file that will anaylse the letters returning a file with the n-grams in it.
Can be run to gather the appropriate information. (though not needed to be run in order to run GA.py in the top level).

'letters_edited' contains all the letters in their edited state (having 'this is the murderer/zodiac' 
removed, also included is the letter_analysis.py file that will anaylse the letters returning a file 
with the n-grams in it. Can be run to gather the appropriate information. (though not needed to be run in order to run GA.py in the top level).

The top level contains all of the files need to run 'GA.py', there is also the file 'GA - final experiment.py',
this file is the setup used in the final experiments seen within the project.

In order to run the GA simply run GA.py (or 'GA - final experiment.py'), simply run it, it will then ask for
some simple inputs from the user before running the GA. If an incorrect value is enter the defualt value will be used.

The default values for the GA are:
Cipher: 408
Cycles: 200
Population: 200
Mutation: 8
Crossover: 9

When the GA is running it will show the symbol mapping for the best in the generation, 
it will show the text representation based on the cipher, then it will display the fitness of the above mapping.
When the GA has finished it will display the best solution of all the cycles done.
When finished with the GA press ENTER to close it.