import os
import hashlib

print("Mass Image Hashing Tool For NFT Provenance","\n")

starting_index = 6  # Change this to the starting index obtained from the smart contract.

print("Individual Hashes") # First Hash In Individual Hash List : Image Index Number = 0 

# Generated Individual Hash Storage. 
hashes = []

# Creating Hashes From Images.
for x in os.listdir():
    if x.endswith(".png"):
        with open(x,"rb") as f:
            bytes = f.read()
            hash = hashlib.sha256(bytes).hexdigest();
            hashes.append(hash)
            print(hash)

# Rearranging Hashes, Begininnig From The Starting Index Numbered Image Hash.
def loop(lst,starting_index):
    rearrange_index = []
    length = len(lst)
    for i in range(length):
        hex_index = starting_index % length
        rearrange_index.append(lst[hex_index])
        starting_index += 1
    return rearrange_index

# Creating TheConcatenated Hash String.
concatenated_hash = ''.join(loop(hashes,starting_index))
print("\nConcatenated Hash String")
print(concatenated_hash)

# Creating The Final Hash.
print("\nFinal Hash")
print(hashlib.sha256(concatenated_hash.encode('utf-8')).hexdigest())

