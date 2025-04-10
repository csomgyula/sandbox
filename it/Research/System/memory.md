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
	
> Every time you make a function call in Zig, an amount of space in the stack is reserved for this particular function call (Chen and Guo 2022; Zig Software Foundation 2024). The value of each function argument given to the function in this function call is stored in this stack space. Also, every local object that you declare inside the function scope is usually stored in this same stack space.  
> [..]	 
> Virtually any application that behaves as a server is a classic use case of the heap. A HTTP server, a SSH server, a DNS server, a LSP server, … any type of server. In summary, a server is a type of application that runs for long periods of time, and that serves (or “deals with”) any incoming request that reaches this particular server.	

https://pedropark99.github.io/zig-book/Chapters/01-memory.html
https://courses.grainger.illinois.edu/cs225/fa2022/resources/stack-heap/

## research

every memory item is like this:

```
(address, type, id, version, timestamp, value)
```

where:

- address is the memory address
- type is the type of the item (data, function, whatever)
- id is logical unique id of the object (which never changes, even if it is relocated or even if it is historical)
- version is the counter how much time the item changed, if Every
- timestap when the item in its current state was created or updated
- the actual value of the item

question:

- we also need a flag whether the item is online or archive?