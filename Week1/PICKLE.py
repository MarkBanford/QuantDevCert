import pickle

data = {
    'How many burgers eaten': [1.0, 1, 3, 1 + 6j],
    'Types of burgers': ("burger", b"Big Mac burger byte string"),
    'How truthful was the burger': {None, True, False}
}

# dump from memory to disk

with open('burger.pkl', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

# read back in

with open('burger.pkl','rb') as f:
    data=pickle.load(f)
    

print(data)