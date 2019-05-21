import pickle

print ('Data_1-1:')
with open('Data_1-1.bin', 'rb') as f:
    data = pickle.load(f)
print (data[:20])   
print ()

print ('Data_1-2:')
with open('Data_1-2.bin', 'rb') as f:
    data = pickle.load(f)
    for i in data.most_common(10):
        print(i)
print ()
