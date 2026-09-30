# numpy muss vorher installiert werden "pip install numpy"

import numpy as np
x = np.array([2, 3, 4]) # beide Listen müssen die selbe Anzahl an Werten haben
y = np.array([2, 3, 4])
print(x @ y)
# in diesem Fall macht das @ das: (2*2) + (3*3) + (4*4) = 29