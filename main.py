import random
from matplotlib import pyplot
import math

n = 20
found = 0
while found < n:


    x = random.uniform(-0.5,0.5)
    y = random.uniform(-0.5,0.5)
    x2 = x + random.uniform(-0.5, 0.5) / 1000
    y2 = y + random.uniform(-0.5, 0.5) / 1000

    dx = x2 - x
    dy = y2 - y
    d0 = math.sqrt(dx*dx + dy*dy)

    a = [random.uniform(-2, 2) for i in range(12)]

    x_values = [x]
    y_values = [y]

    conv = False
    lyapunov = 0

    for i in range(10000):

        xnew = a[0] + a[1]*x + a[2]*x*x + a[3]*y + a[4]*y*y + a[5]*x*y
        ynew = a[6] + a[7]*x + a[8]*x*x + a[9]*y + a[10]*y*y + a[11]*x*y

        if xnew > 1e10 or ynew > 1e10 or xnew < -1e10 or ynew < -1e10:
            conv = True
            break

        if abs(x - xnew) < 1e-10 and abs(x - ynew) < 1e-10:
            conv = True
            break

        if i > 1000:
            x2new = a[0] + a[1] * x2 + a[2] * x2 * x2 + a[3] * y2 + a[4] * y2 * y2 + a[5] * x2 * y2
            y2new = a[6] + a[7] * x2 + a[8] * x2 * x2 + a[9] * y2 + a[10] * y2 * y2 + a[11] * x2 * y2

            dx = x2new - xnew
            dy = y2new - ynew
            d = math.sqrt(dx * dx + dy * dy)

            #lyapunov exponent:
            lyapunov += math.log(abs(d/d0))

            x2 = xnew + d0*dx/d
            y2 = ynew + d0*dy/d


        x = xnew
        x_values.append(x)
        y = ynew
        y_values.append(y)

    if not conv and lyapunov >= 10:
        found += 1

        pyplot.scatter(x_values, y_values, s=0.1)
        pyplot.show()