class SeparateChainingHashTable:
    def __init__(self, size=10):
        self.table = [[] for _ in range(size)]
        self.size = size

    def custom_hash_function(self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp%self.size

    def insert(self,value):
        # Get the index from the custom hash function
        index = self.custom_hash_function(value)
        bucket = self.table[index]
        bucket.append(value)

    def search(self, key):
        # Get the index from the custom hash function
        index = self.custom_hash_function(key)
        bucket = self.table[index]
        for i, value in enumerate(bucket):
            if value == key:
                return "yes"
        return bucket


hash_table = SeparateChainingHashTable(size=5)

hash_table.insert("apple")
hash_table.insert("banana")
hash_table.insert("cherry")
hash_table.insert("date")  # Demonstrating collision
print("Hash Table:")
for i, bucket in enumerate(hash_table.table):
    print(f"Bucket {i}: {bucket}")
print(hash_table.search('date'))


