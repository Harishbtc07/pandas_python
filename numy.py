#Numpy

#Creating arrays
import numpy as np
a=[10,20,30]
b=np.array(a)
print(b)

a=[[10,20],[40,50]]
b=np.array(a)
print(b)

print(a[0][1])

a=[[[10,20],[30,40]],[[50,60],[80,90]]]
b=np.array(a)
print(b)

print(a[1][0][1])

a=[10,20,30]
b=np.asarray(a,float)
print(b)

a=[[10,20],[30,40]]
b=np.asarray(a,float,'c')
print(b)