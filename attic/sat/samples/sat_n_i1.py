"""
This module implements a $Sat \ N \ I1$ 3-SAT sample generator. 

A $Sat \ N \ I1$ sample is such that:

1. it is satisfiable ($Sat$) and
2. where
   1. every variable appears in both form: identical and negated ($N$)
   2. every 2 clauses has at most 1 shared variable, their intersection is at most one ($I1$)
3. which are not expandable without unsatisfying conditions 1. 2.
"""
from enum import Enum
class VariableForm(Enum):
    """
    Role: Represents the variable forms(s) already apperared in clauses, can be one of:
    - `NONE` - variable did not appear in any clause
    - `IDENTICAL` - appeared in its identical form, e.g. $x_1$ in $(x_1 \lor ...)$
    - `NEGATED` - appeared in its negated form, e.g.  $x_1$ in $(\lnot x_1 \lor ...)$
    - `BOTH` - appeared in both form
        
    >>> print(VariableForm.NONE)
    NONE

    >>> print(VariableForm.IDENTICAL)
    IDENTICAL

    >>> print(VariableForm.NEGATED)
    NEGATED
    
    >>> print(VariableForm.BOTH)
    BOTH
    
    Operations:
    - `__add__(new_form)`: adds a new form to the existing one:  
        
        First appearence:       
        >>> print(VariableForm.NONE + VariableForm.IDENTICAL)
        IDENTICAL

        >>> print(VariableForm.NONE + VariableForm.NEGATED)
        NEGATED
        
        Second appereance:
        >>> print(VariableForm.IDENTICAL + VariableForm.IDENTICAL)
        IDENTICAL

        >>> print(VariableForm.NEGATED + VariableForm.NEGATED)
        NEGATED
    
        Both appereance:
        >>> print(VariableForm.IDENTICAL + VariableForm.NEGATED)
        BOTH

        >>> print(VariableForm.NEGATED + VariableForm.IDENTICAL)
        BOTH
    """
    NONE = 0
    IDENTICAL = 1
    NEGATED = 2
    BOTH = 3
    
    def __add__(self, new_form):
        """
        Adds a new form to the existing one
        
        - Form value is interpreted as a bitmap, where
            - index 0 shows whether it appeared in `IDENTICAL` form
            - index 1 shows whether it appeared in `NEGATED` form
        - Hence:
            - 0/00 - no appereance yet
            - 1/10 - appeared in its identical form
            - 2/01 - appeared in its negated form
            - 3/11 - appeared in both form        
        - __add__ is implemented as bitwise OR
        """
        return VariableForm(self.value | new_form.value)
    
    def __str__(self):
        return f"{self.name}"
        
class Variable:
    """
    Role: Memorize variable related data:
    - in what form it already appeared (`NONE`, `IDENTICAL`, `NEGATED`, `BOTH`)
    - the available pairs it can appear
    
    Attributes:
    - `appearance`: the variable form(s) already appeared in clauses
    - `available_pairs`: the variable pairs it can appear without contradicting condition 2.2. 
      (every 2 clauses has at most 1 shared variable)
    
    Operations: 
    - `__init__(id)`: initialize the variable 
    
    Usage:
    - SatNI1.__init__ -> 
        - `available_pairs.add`: available_pairs will be initialized when variable 
      pairs are initialized
    - SatNI1.??? -> after a clause is generated
        - `appearance + new_form`: add the new form according to the clause 
        - `available_pairs.remove`: remove pairs from clause not available any more
    """
    
    def __init__(self, id):
        """
        initialize the variable 
        - `id = id`
        - `appearance = NONE`
        - `available_pairs = {}`
    
        >>> v = Variable(1)
        >>> print(v.id)
        1
        >>> print(v.appearance)
        NONE
        >>> print(v.available_pairs)
        {}
        >>> print(v)
        var_1 appearance NONE
        """
        self.id = id
        self.appearance = VariableForm.NONE
        self.available_pairs = {}
        
    def __str__(self):
        return f"var_{self.id} appearance {self.appearance}"
    
class VariablePair:
    """
    Role: Memorize available pairs which can be used for clauses
    
    Attributes:
    - `source`: variable pairs are directed, this is the source in the pair
    - `target`: this is the target in the pair
    - `available_siblings`: the sibling pairs which can be used to make 3-SAT clause without 
      contradicting condition 2.2. (every 2 clauses has at most 1 shared variable)
    
    Operations: 
    - `__init__(source, target)`: initialize the variable 
    
    Usage:
    - SatNI1.__init__ -> 
        - `__init__`: all pairs created during initialization  
          note this is when the pair is also added to the variable as available
        - `available_siblings.add`: siblings will be initialized during initialization
    - SatNI1.??? -> after a clause is generated
        - `available_siblings.remove`: remove siblings (part of the clause) not available any more  
          note that once a pair does not have any siblings it will be removed from the source variable
    """
    
    def __init__(self, source, target):
        """
        initialize the variable pair
        - `source = source`
        - `target = target`
        - `available_siblings = {}`

        >>> vp = VariablePair(Variable(1), Variable(2))
        >>> print(vp.source)
        var_1 appearance NONE
        >>> print(vp.target)
        var_2 appearance NONE
        >>> print(vp.available_siblings)
        {}
        >>> print(vp)
        var_1 appearance NONE -> var_2 appearance NONE
        """
        self.source = source
        self.target = target
        self.available_siblings = {}
        
    def __str__(self):
        return f"{self.source} -> {self.target}"

class Clause3:
    """
    Role: Represents a clause with 3 variables
    
    Samples: 
    
    - $var_1 \lor var_2 \lor var_3$
    - $var_1 \lor var_2 \lor \lnot var_4$
    """
    
class SatNI1Sample:
    pass
    
class SampleGenerator:
    pass
    
class Obfuscator:
    """
    Initially the solution is $(x1=True, x2=True, x3=True)$
    We obfuscate it:
    - randomly permute indexes
    - randomly negate some logic in the clauses
    """    
    
if __name__ == '__main__':    
    import doctest
    doctest.testmod()