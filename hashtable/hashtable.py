class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_tail(self, key, value):
        entry = HashTableEntry(key, value)

        if self.head == None:
            self.head = entry
            return
        
        cur = self.head

        while cur.next is not None:
            if cur.key == key:
                cur.value = value
            cur = cur.next
        
        cur.next = entry

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
    
        return None

    def delete(self, key):
        cur = self.head

        if cur.key == key:
            self.head = self.head.next
            cur.next = None
            return cur

        prev = None

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return cur
            prev = cur
            cur = cur.next

        return None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [LinkedList()] * self.capacity
        self.added_in = set()


    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5 ) + hash) + ord(x)
        return hash & 0xFFFFFFFF




    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        load_factor = len(self.added_in) / self.capacity
        if load_factor >= 0.7:
            self.resize(self.capacity * 2)
        
        index = self.hash_index(key)
        self.storage[index].add_to_tail(key, value)

        if key not in self.added_in:
            self.added_in.add(key)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index].delete(key)
        self.added_in.remove(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        return self.storage[index].find(key)

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        self.capacity = new_capacity
        new_hash_table = [LinkedList()] * self.capacity

        for i in self.storage:
            cur = i.head
            
            while cur is not None:
                
                index = self.hash_index(cur.key)
                new_hash_table[index].add_to_tail(cur.key, cur.value)

                cur = cur.next

        self.storage = new_hash_table

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize(old_capacity * 2)
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    print("")
