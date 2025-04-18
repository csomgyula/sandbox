# Satisfiable Negate Intersection 1

## Constraint

Samples 

1. which are satisfiable and
2. where
   1. every variable appears in both form (id, negate)
   2. every 2 clauses has at most 1 shared variable
3. which are not expandable without unsatisfying conditions 1. 2.

## Approximating random algorithm

4. Set max step
5. Choose a random value, which will be a solution
6. Loop until max step
	1. Generate a random clause
	2. Hold if conditions hold
	3. Drop if conditions do not hold

## Approximating deterministic algorithm

### condition 1.

7. Do not choose a triplet which contradicts the selected solution

### condition 2.2.

8. Memorize every pairs already appeared (in hold) hence would contradict condition 2.2

### condition 2.1. + 2.2.

procedures:

9. Memorize every variable which have not yet appeared in any triplet
10. Memorize every variable which appeared in a triplet but not in both form,  
    memorize it with its form not yet appeared
11. Memorize every pairs which have not yet appeared in any triplet
12. Connect every variable (under Proc 9, 10) with every pair (under Proc 11) where it appears
13. Connect every pairs (under Proc 11) which can be connected
14. Proc 11 fulfills Proc 8 only Proc 11 is implemented

algorithm:

15. Select next variable which have not yet appeared in any triplet (from Proc 9) if any
    1. Select from its pairs (from Proc 12) which can be connected (from Proc 13)
	2. If there is any
		1. be it the next triplet
		2. update Proc 9, 10
			1. move variable from Proc 9 to Proc 10 #that is not enough, we have 3 vars
			2. update the other two variables if necessary
		3. remove all the three pairs from the triplet from Proc 11 and its links from Proc 12, 13
	3. Else (if no such pair) then remove variable from Proc 9
16. Select next variable which have not yet appeared in both form (from Proc 10) if any
    1. Select from its pairs (from Proc 12) which can be connected (from Proc 13), if any
	2. If there is any
		1. be it the next triplet
		2. remove all the three pairs from the triplet from Proc 11 and its links from Proc 12, 13
	3. update Proc 9, 10
		1. Remove variable from Proc # that is not enough, we have 3 vars
		2. update the other two variables if necessary
17. End if Proc 9, 10 is empty, goto 15 if not


### condition 1. + 2.1. + 2.2.

algorithm:

19. Initialize Proc 9..13
20. Generate the first triplets based on the solution
21. Do the bookeeping in 15-16
22. Do the algo under condition 2.1. + 2.2.