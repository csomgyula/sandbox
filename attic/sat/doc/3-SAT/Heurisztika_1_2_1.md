sample

- SAT = ~u or  x  or  y  
              ~x  or ~y or z
- SAT => u => 
	- (x and ~y) or (~x and y) or z 
	- (x         or (~x and y) or z) and  
	       (~y   or (~x and y) or z)
	- (
	  (x         or  ~x        or z) or  
	  (x         or         y  or z)
	  ) and  
	       (~y   or (~x and y) or z)
	- (x         or         y  or z) and  
	       (~y   or (~x and y) or z)

