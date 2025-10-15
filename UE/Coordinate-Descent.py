coordinates = [x, y, z]
derivatives = [(10 - 12*y - 6*z)/10, (60 - 12*x - 36*z)/80, (30 - 6*x - 36*y)/26]

help = [f(derivatives[0], y, z), f(x, derivatives[1], z), f(x, y, derivatives[2])]
minArray = np.argsort(help)
coordinates[minArray[0]] = derivatives[minArray[0]]

x,y,z = coordinates
