# Analysis of Algorithms
**Exercise I**: _Give an analysis of the running time of each snippet of pseudocode with respect to the input size n of each of the following:_
```
a)  a = 0                      # O(1)
    while (a < n * n * n)      # O(n^3)???
      a = a + n * n            # how many n^3 are there in an n^2?
                               # = n = O(n)
```
```
b)  sum = 0                                     # O(1)
    for (i = 0; i < n; i++)                     # O(n)
      for (j = i + 1; j < n; j++)               # O(n)
        for (k = j + 1; k < n; k++)             # O(n)
          for (l = k + 1; l < 10 + k; l++)      # O(1)
            sum++                               # O(1)

                                for (l = k + 1; l < 10 + k; l++)  === O(1)
                                explained:
                                 K    loop runs
                                 0    1 to 9, for a total of 9 runs
                                 10   11 to 19, for a total of 9 runs
                                 100  101 to 109, for a total of 9 runs
                                 no matter what k is, this line is running 9 times
                                 = O(1)
```
```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```

**Exercise II**:
Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.
