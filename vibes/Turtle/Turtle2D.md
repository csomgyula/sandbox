# Turtle programming language

1. Grid is the tape, where you can move
	- either in discrete steps (such as e.g. TUI) or continuously (think of SVG)
	- either in elementary steps (Turing machine) or long moves (turtle graphics) 
2. Program is hosted by the Turtle
	- either a low level state machine (Turing machine) or a high level program (turtle graphics)
	- machine is: Turing, Neumann, Harvard
3. IO is two-layered
	- at the core level (coding) inputs and outputs are numbers
	- at the representation level display is either 
		- textual, character based (stories told)
		- color (stories drawn, which yields 2+1D)
		- that is every word, story is mapped to a geometry drawing (asperger syndrome)
- Ideas: 
	- Display: transform between color and num/text  
	  (not just through blindless recoding, but through similarity)
	- Progam moves to data (data gravity, edge): 
		- add networking, where code moves along with data, Turtle is hosted within a container
		- add hyperlinks between grids (as a whole)
		- grids can be simple grids or more complex graphs/topologies
	- Model real life problems
		- Communication grid, where: 
			- grid contains multiple turtles
			- grid cells represent: 
				- messages (raw for any or structured for turtle)
				- messengers (turtle)
				- homes (or senders and receivers, where turtle starts from and returns to)
			- grid activities represent communication, collaboration
			- model gravitation and other forces like that
		- Necessity grid which extends communication grid, where 
			- grid cells may also represent energy (raw energy for any, energy for turtle)
			- grid activities represent food necessities: energy seeking, consuming and producing
			- model ant colonies (stigmergies, tabus with halving energy, back to home, seeking by collective tradition, randomly)
		- What about builds, self-assembly, reporuduction?
		
Inspirations:

- https://en.wikipedia.org/wiki/Turtle_graphics
	- https://docs.python.org/3/library/turtle.html
		- clearscreen
		- pos, forward, left, right, 
		- color, fill_color, up?, down?, begin_fill, end_fill
		- https://github.com/asweigart/simple-turtle-tutorial-for-python

Others: todo 
- https://en.wikipedia.org/wiki/L-system
- https://en.wikipedia.org/wiki/Logo_(programming_language)
- https://en.wikipedia.org/wiki/Joy_(programming_language)