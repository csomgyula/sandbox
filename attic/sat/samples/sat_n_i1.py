"""
Samples 

1. which are satisfiable and
2. where
   1. every variable appears in both form (id, negate)
   2. every 2 clauses has at most 1 shared variable
3. which are not expandable without unsatisfying conditions 1. 2.
"""
from enum import Enum
class VariableForm(Enum):
    """
    Role: Represents the forms(s) as the variable already apperared in clauses
    
    Possible values:
    - `NONE` - no appereance yet
    - `ID` - appeared in its identical form, e.g. $x_1$ in $(x_1 \lor ...)$
    - `NEG` - appeared in its negated form, e.g.  $x_1$ in $(\lnot x_1 \lor ...)$
    - `BOTH` - appeared in both form
        
    >>> print(VariableForm.NONE)
    VariableForm.NONE

    >>> print(VariableForm.ID)
    VariableForm.ID

    >>> print(VariableForm.NEG)
    VariableForm.NEG
    
    >>> print(VariableForm.BOTH)
    VariableForm.BOTH
    
    Operations:
    - `__add__(new_form)`: adds a new form to the existing one:  
        
        First appearence:       
        >>> print(VariableForm.NONE + VariableForm.ID)
        VariableForm.ID

        >>> print(VariableForm.NONE + VariableForm.NEG)
        VariableForm.NEG
        
        Second appereance:
        >>> print(VariableForm.ID + VariableForm.ID)
        VariableForm.ID

        >>> print(VariableForm.NEG + VariableForm.NEG)
        VariableForm.NEG
    
        Both appereance:
        >>> print(VariableForm.ID + VariableForm.NEG)
        VariableForm.BOTH

        >>> print(VariableForm.NEG + VariableForm.ID)
        VariableForm.BOTH
    """
    NONE = 0
    ID = 1
    NEG = 2
    BOTH = 3
    
    def __add__(self, new_form):
        """
        Adds a new form to the existing one
        
        - Form value is interpreted as a bitmap, where
            - index 0 shows whether it appeared in ID form
            - index 1 shows whether it appeared in NEG form
        - Hence:
            - 0/00 - no appereance yet
            - 1/10 - appeared in its identical form
            - 2/01 - appeared in its negated form
            - 3/11 - appeared in both form        
        - __add__ is implemented as bitwise OR
        """
        return VariableForm(self.value | new_form.value)
    
class Variable:
    """
    Role: Memorize variable related data:
    - in what form it already appeared (`NONE`, `ID`, `NEG`, `BOTH`)
    - the available pairs it can appear
    
    Attributes:
    - form: the form(s) already appeared
    - available_pairs: the variable pairs it can appear without contradicting condition 2.2. 
      every 2 clauses has at most 1 shared variable
    
    Operations: 
    - __init__(i): initialize the variable with 
        - form = NONE
        - available_pairs = None
    - add_available_pair
    - remove_available_pair
    
    Usage:
    - SatNI1.__init__ -> add_available_pair: available_pairs will be initialized when variable 
      pairs are initialized
    - SatNI1.??? -> remove_available_pair: called after a clause is generated hence its variable 
      pairs are not available any more
    """
    
    def __init__(self):
        """
        >>> v = Variable()
        >>> print(v.form)
        VariableForm.NONE
        >>> print(v.available_pairs)
        []
        """
        self.form = VariableForm.NONE
        self.available_pairs = []
        
    def add_available_pair(pair):
        pass
    
    def remove_available_pair(pair):
        pass
    
class VariablePair:
    pass

class SatNI1:
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