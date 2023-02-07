'''We think summartion of -1+1-1+1....n times will mostly zero, which is similar to dice flip
where we decide probability of getting head or tail is 1/2 but that is not the case, this example will prove that'''

import numpy as np
import matplotlib.pyplot as pt

d={}
for i in range(500):
    rand_array=2*(np.random.rand(1,1000)>0.5)-1
    v=sum(rand_array[0])
    d[v]=d.get(v,0)+1
x_axis=d.keys()
y_axis=d.values()
pt.bar(x_axis,y_axis,color="red",width=0.4)
pt.xlabel("sum of dice flip")
pt.ylabel("count")
pt.title("showing dice flip probability for larger number is not always 1/2")
pt.show()