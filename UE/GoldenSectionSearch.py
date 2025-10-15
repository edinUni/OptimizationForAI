a, b, c = trpl
if (b - a > c - b):
    nominator = f(a) - f(c)
    denominator = (max(f(c), f(a)) - f(b)) * 2.1
    d = a + (b - a) * (nominator / (denominator) + 0.5)
    if(f(d) < f(b)):
        trpl = np.array([a, d, b])
    else:
        trpl = np.array([d, b, c])
else:
    nominator = f(c) - f(a)
    denominator = (max(f(a), f(c)) - f(b)) * 2.1
    d = c + (b - c) * (nominator / (denominator) + 0.5)
    if(f(d) < f(b)):
        trpl = np.array([b, d, c])
    else:
        trpl = np.array([a, b, d])

trpl = np.array(trpl)
