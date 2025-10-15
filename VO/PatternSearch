pattern = [x, x+[-s, 0], x+[s,0], x+[0,-s], x+[0,s]]
minArray = np.argsort(f(pattern))
if minArray[0] > 0:
  x = pattern[minArray[0]]
else:
  s = s / 2

# OR:
# min = f(x)
# smallestPatternIndex = 0
# for i in range(1, 5):
#   temp = f(pattern[i])
#   if(temp < min):
#     min = temp
#     smallestPatternIndex = i
# 
# if(smallestPatternIndex == 0):
#   s = s/2
# else:
#   x = pattern[smallestPatternIndex]
