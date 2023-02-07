import torch
import numpy as np
x=np.ones(5)
y=torch.from_numpy(x)
np.add(x,1, out=x)
print(x)
print(y)