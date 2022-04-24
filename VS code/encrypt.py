import hashlib

def hash_data(data):
    hash_object = hashlib.md5(data.encode())
    return hash_object.hexdigest()

def main():
    data = input("Enter the data to be hashed: ")
    hashed_data = hash_data(data)
    print("The hashed data is: " + hashed_data)

main()