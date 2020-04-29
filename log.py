import h5py
import ismrmrd
import numpy as np
import matplotlib.pyplot as plt
filename = 'testdata.h5'
f = h5py.File(filename, 'r')
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[0]
print(a_group_key);
tempo = list(f[a_group_key])
print(tempo)
test=   list(f[a_group_key] ['image_1'])
print(test)
magnitude=   list(f[a_group_key] ['image_1'] ['data'])
m = np.array(magnitude)
print(m)
print(m.shape)
m2=np.transpose(m, (3, 4, 0,1,2))
print(m.shape)
print(m2.shape)
plt.figure(1)
for s in range(1, 11):
	plt.subplot(2, 5, s)
	plt.imshow(m2[:,:,s - 1,0,0], cmap="gray")
plt.show()
