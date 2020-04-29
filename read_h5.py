import h5py
import ismrmrd
import numpy as np
import matplotlib.pyplot as plt
filename = 'out.h5'

f = h5py.File(filename, 'r')


# List all groups
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[0]

# Get the data
tempo = list(f[a_group_key])
print("tempo: %s" % tempo)

test=   list(f[a_group_key] ['image_1'])
print(test)

magnitude=   list(f[a_group_key] ['image_1'] ['data'])
phase=   list(f[a_group_key] ['image_1'] ['data'])

m= np.array(magnitude)
p= np.array(phase)

print (m.shape)
print (p.shape)

m_y= m[:,0,0,:,:]
p_y= p[:,0,0,:,:]

print (m_y.shape)

m_x=np.transpose(m_y, (2, 1, 0))
p_x=np.transpose(p_y, (2, 1, 0))

vec_size=m_x.shape;

dimx=vec_size[0]
dimy=vec_size[1]
unknow=int(vec_size[2])
number_of_repetitions=4
number_of_slices=int(unknow)//number_of_repetitions


print (m_x.shape)
print (m_x.shape)
print (dimx, dimy, unknow, number_of_slices, number_of_repetitions)

plt.figure(1)

#fig, axs = plt.subplots(2, 1, constrained_layout=True)

for l in range(number_of_slices, number_of_slices*number_of_repetitions ,  number_of_slices):

    for s in range(0, number_of_slices):
        im_m=m_x[:,:,s+l]
        im_p=p_x[:,:,s+l]
        print(s+1)	
        plt.subplot(8, number_of_slices/4, s+1)
        plt.imshow(im_m, cmap="gray")
        plt.axis('off')
        print(s+1+number_of_slices)
        plt.subplot(8, number_of_slices/4, s+1+number_of_slices)
        plt.imshow(im_p, cmap="gray")
        plt.axis('off')
	
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()

#plt.show()
	
    plt.show(block=False)
    #if l==number_of_slices:
    	#fig.suptitle('This is a somewhat long figure title', fontsize=16)
    plt.pause(2)

plt.close()

#quit()
