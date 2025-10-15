pattern = np.array([x, x-d, x + d + [d[1], -d[0]], x + d + [-d[1], d[0]]])
functionEvaluated = [f(pattern[0]), f(pattern[1]), f(pattern[2]), f(pattern[3])]
minArray = np.argsort(functionEvaluated)
if(minArray[0] > 0):
  d = pattern[minArray[0]] - x
  x = pattern[minArray[0]]
else:
  d = d/2
