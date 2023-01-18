import lmdb

env = lmdb.open("./train", map_size=1099511627776) 

txn = env.begin(write=True) 
  
# Add data and key values 
txn.put(key = '1'.encode(), value = 'aaa'.encode()) 
  
# Delete data by key value 
txn.delete(key = '1'.encode()) 
  
# Modifying data 
txn.put(key = '3'.encode(), value = 'ddd'.encode()) 
  
# Commit changes through the commit() function 
txn.commit() 
#env.close()
#

txn = env.begin(buffers=True) 

buf = txn.get("3".encode())

b

breakpoint()
env.close()

