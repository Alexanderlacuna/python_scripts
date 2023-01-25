import lmdb
import numpy as np

N = 1000

# let pretend this is interesting data

X = np.zeros((N,3,32,32), dtype = np.uint8)

Y = np.zeros(N, dtype= np.int64)

#print(X)

#print(len(Y))
#print(Y)

# we need to prepare the database for the size,we'll set it 10 times

#  greater than what we theoritically need


sampl = np.random.uniform(low=0.5, high=13.3, size=(50,))

print(sampl)
print(len(sampl))
print(sampl.tobytes())
map_size = sampl.nbytes * 10
env = lmdb.open('mylmdb')


with env.begin(write= True ) as txn:

#	data = sampl[i].tobytes()
	lst = [[1,2,3,4,5]]

	lst_k  = [bytes(lt) for lt in lst]

	breakpoint()

	for i in range(5):
		txn.put(str(i).encode(),bytes(lst_k))



# reading from life




with  env.begin() as txn:
	cursor = txn.cursor()

	for (key,value) in cursor:
		print(key.decode(),list(value))
