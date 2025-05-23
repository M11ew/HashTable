class HashTable:
    def __init__(self, size):
        self.size = size 
        self.value = [None]*self.size

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """
        Return a hashed location using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - The largest value to be returned will be less than size.   
        Remember to compress the return value to fit the table size.
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """

        p = 31
        m = 1000000009
        hashValue = 0
        pPow = 1

        for i in range(1,len(key)):
            charValue = ord(key[i]) - ord('a') + 1 
            hashValue = (hashValue + charValue* pPow) % m 
            pPow = (pPow * p) % m
        
        return hashValue % self.size

    def setitem(self, key: str, value: dict) -> None:
        """
        updates and adds an item into the list of values
        """
        index = self._hash(key)
        message = "Data successfully updated!"
        if self.value[index] is None:
            message = "Data successfully added!"
        self.value[index] = value
        print(message)

    def getitem(self, key: str) -> 'dict | None':
        """
        returns the value of the key that is being looked for
        """
        index = self._hash(key)
        if self.value[index] is None:
            return "Destination is empty!"
        else:
            return self.value[index]
        
    def delitem(self, key: str) -> None:
        """
        deletes an item from the destination 
        """
        index = self._hash(key)
        if self.value[index] is None:
            return 'Unable to remove. Destination is empty!'
        else:
            self.value[index] = None
            return 'Data successfully removed'