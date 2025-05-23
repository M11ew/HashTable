from hashtable import HashTable
import csv
if __name__ == "__main__":
    ht = HashTable(30)
    """
    1. Extract the records from the student_data file
    and add them one at a time, as a Python dict, 
    containing the name, class and their associated
    data as key-value dict pairs, to the hashtable
    
    2. You can use the id as the hash table key for 
    each of the above records.
    """
    
    # Test your hashtable using appropriate methods
    # from your implementation
    
    with open('student_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ht.setitem(row['id'], row)
    ht.getitem('s0014d') 
    ht.delitem('s0014d')
    print(ht.getitem('s0014d'))
    

