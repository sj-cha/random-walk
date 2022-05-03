# random-walk
This code deals with a particle randomly moving in a 2D lattice, with four degrees of freedom: up, down, left, or right. 

Let n be an integer indicating a number of steps a particle takes. 

Since the plane is two-dimensional, we will take two axis, `x` and `y`, separately. 

The arrays below are used to store the position of the particle in the respective axis at *n* th steps. Therefore, the size is *n* and they are initially filled with 0, assuming the starting point is (0, 0).

```python
x = np.zeros(n)
y = np.zeros(n)
```

For each step, the particle randomly moves to an adjacent unit. The particle's current coordinate can be determined by the snippet below.

```python 
for i in range(1,n):
    val = random.randint(1,4)
    if val == 1: 
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1 # a particle moving up, (0, 1)
    if val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] # a particle moving to the left, (-1, 0)
    if val == 3:
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1 # a particle moving down, (0, -1)
    if val == 4:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] # a particle moving to the right, (1, 0)
```

After iterating *n* times, the trace of the particle can be simply plotted using the arrays `x` and `y`.

## Result

![histogram 1](https://raw.githubusercontent.com/sj-cha/random-walk/main/n%20%3D%201000.png)
![histogram 1](https://raw.githubusercontent.com/sj-cha/random-walk/main/n%20%3D%20100000.png)

A trace of a particle when *n* = 1000 (left), and when *n* = 100000 (right)

A random walk in a 3D plane is a trivial case and is left as an exercise to the reader.
