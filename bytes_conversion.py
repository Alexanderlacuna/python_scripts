from io import BytesIO

import numpy as np 

#https://stackoverflow.com/questions/53376786/convert-byte-array-back-to-numpy-array

def array_to_bytes(x:np.ndarray) -> bytes:
	np_bytes = BytesIO()

	np.save(np_bytes,x,allow_pickle =True)
	return (np_bytes.getvalue())




def bytes_to_array(b: bytes) -> np.ndarray:
    np_bytes = BytesIO(b)
    return np.load(np_bytes, allow_pickle=True)
