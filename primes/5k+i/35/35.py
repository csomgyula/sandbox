class Sys:
    def non_zero(x):
        return not(x == 0)
            
    def nzero(x):
        if x == 0:
            return 1
        else:
            return 0
            
    def this_dir():
        import sys
        return sys.path[0]
        
    def file_here(file):
        import os
        return os.path.join(Sys.this_dir(), file)
            
def main(p, q):
    """
    Cél: mod 35 számtani sorozatok heatmapje:
    num:
         1,  2,  3, ..., 35
         2,  4,  6, ..., 70
        ...
        34, 33, 32, ...,  1
    mark:
        1, ha osztható 5-el vagy 7-el
        0, ha nem
    """
    base = p * q
    
    # determine numbers relative prime to p*q
    relative_primes = []
    for num in range(base):
        if Sys.non_zero(num % p) and Sys.non_zero(num % q):
            relative_primes.append(num)
        
    # create empty matrices    
    num_matrix =  [None] * len(relative_primes)
    mark_matrix = [None] * len(relative_primes)
    
    # calculate/fill matrices        
    for row, relative_prime in enumerate(relative_primes):
        # calculate nums
        nums = [(j * relative_prime) % base for j in range(1, base)]
        
        # calculate marks for each num
        marks = [0] * base
        for col, num in enumerate(nums):
            marks[col] = Sys.nzero(num % p) + Sys.nzero(num % q)

        # add nums and marks to num and mark matrices
        num_matrix[row] = nums
        mark_matrix[row] = marks    
        
    # save matrices
    import csv

    with open(Sys.file_here("num.csv"), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(num_matrix)
            
    with open(Sys.file_here("mark.csv"), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(mark_matrix)
            
if __name__ == "__main__":
    main(5, 7)            