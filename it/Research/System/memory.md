# Memory management

## zone-based (bottom up approach)

### zones 

- zone is which is responsible for memory management
- a zone can be 
	- either builtin, such as a function (stack) and object (heap)
	- or custom, developer made (such as an object graph) but then the developer is responsible for memory management
  
### ownerships and references  
- module, object, function, etc.
	- either owns data, object, function, etc. in that case
		- the owner is responsible for managing the life cycle
	- or refers to it, in that case reference is not direct (by address) but through the owner
		- which is slow! but safe
		
### discussion
		
- hence you are 
	- either fast but then you take care of safety
		- even in this case unsafety is encapsulated within the boundaries of the owner
		  once the owner goes out of scope it is cleaned up
	- or safe with but this comes with a price in speed
- the lang is a tool not a framework, it provides you the choice
- open questions and tasks:
	- can we still add gc to unsafe code?
		- ?extended escape analysis, which still does not work for graphs with very long pathes
		- ?algorithm inspired by blood circulation
	- can ownership change? without copy?
		- something between ownership and reference? lease, borrow? 
		- study Rust, Cyclone (https://cyclone.thelanguage.org/) techniques
		- study Zig ?flexible memory management
		
## goal based (top down approach)
- everything has an actor and goal (usage by actor)
	- actor is 
		- either directly an external user (e.g. human user, system)
		- or an internal caller
	- goal is 
		- either inherited from caller, owner or split (goal parts) -> goal algebra
		- hard goal (functional) or soft (good enough)
- everything that is			
	- service = runnable functions, accessible data
	- running function = has a goal		