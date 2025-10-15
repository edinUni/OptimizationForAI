a, b, c = trpl  # Unpacking the array into variables
phi = (1 + np.sqrt(5)) / 2

if (b - a > c - b):
    d = c + (a-c)/phi
    if(f(d) < f(b)):
        trpl = np.array([a, d, b])
    else:
        trpl = np.array([d, b, c])
else:
    d = c + (b-c)/phi
    if(f(d) < f(b)):
        trpl = np.array([b, d, c])
    else:
        trpl = np.array([a, b, d])

trpl = np.array(trpl)
