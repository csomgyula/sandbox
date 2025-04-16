# AI

## operation
binary series:

- `b_permute(i_1, i_2, ...) * v`: permute a vector's dimensions 
  - `switch(i,j) * v`: switch a vector's dimensions i, j
- `b_mirror(i_1, i_2, ...) * v`: negate the values at the given dimensions 

non-binary series:

- `d_permute * v`: permute a vector's dimensions 
- `v_permute(i) * v`: permute the values at the given dimension

hence:

- `b_mirror(i_1, i_2, ...) * v = v_permute(0,1)(i_1), v_permute(0,1)(i_2), ... `

## unbias (merge)

1. distribution: a binary distribution, $R = (type bin)@R$ is given which can be biased so we want to unbias
2. sample batches: a binary matrix, $B = ((type bin) (sample_places row))@B$ is given, where every row is a random series (sample batch) from this distribution, $R$ 
   - how this matrix is obtained left to implementation, such as collect batches one by one
3. calculate the 0-1 sample distribution in every column, called cross-batch distribution: $S = ((type bin) (matrix_histogram col B))@S = (matrix_histogram col)@histogram(B)$
   - distribution is represented by a histogram with one degree of freedom, e.g. $(0.4, 0.6)$ represents 40% of 0s and 60% of 1-s
   - matrix distribution is represented by the column vector of histograms, where a distribution/row in the vector corresponds to the distribution of/same row in the matrix
4. permute rows so deviation will be in decreasing order $M,S = (decrease)@(M, S) = decrease(M,S)$
5. initialize bias vector, $bias = b@bias$ originally to the first row from the distribution $bias = S[1]$
6. loop, in each round calculate the next bias and transform:
   1. take the next row, `row` from the samples
   2. calculate the bias if it remains unchanged: $original = {bias: bias + S[next], transform: id}$
   3. calculate the bias if it is mirrored: $negated = {bias: bias + mirror S[next]$, transform: negate}$
   4. take the one which is less biased: $bias, yield (row, transform) <- less_biased(original, negated)$

## diffusion

same as unbis

## unique count

opposite of bias

## classification

opposite of bias