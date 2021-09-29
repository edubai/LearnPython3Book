""" A simple python program to understand string encoding
and decoding """



original = '27岁少妇生孩子后变老' # python uses unicode for strings
type(original) #<class 'str'>
encoded = original.encode('utf-8')
print(encoded) # b'27\xe5\xb2\x81\xe5\xb0\x91\xe5\xa6\x87\xe7\x94\x9f\xe5\xad\xa9\xe5\xad\x90\xe5\x90\x8e\xe5\x8f\x98\xe8\x80\x81'
type(encoded) # <class 'bytes'>
decoded = encoded.decode('utf-8')
print(decoded) # 27岁少妇生孩子后变老
