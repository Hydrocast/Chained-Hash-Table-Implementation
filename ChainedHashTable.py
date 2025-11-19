# ==============================
# Chained Hash Map Implementation
# Author: Giannis Loizou
# Description: Custom implementation of a chained hash table
# linked-list based collision handling with rehashing support.
# ==============================

class EmptyHash(Exception):
    """Raised when attempting to operate on an empty hash table."""
    pass


class ChainedHash:
    INITIAL_SIZE = 5        # Initial number of buckets
    REHASH_RATIO = 2.0      # Load factor threshold for rehashing

    class _Node:
        """Linked list node used for chaining collisions."""
        def __init__(self, key, data, prev=None, nextt=None):
            self._key = key
            self._prev = prev
            self._next = nextt
            self._data = data

    def __init__(self):
        self._hash = [None] * self.INITIAL_SIZE
        self._bsize = self.INITIAL_SIZE  # Current bucket count
        self._hsize = 0                  # Total number of stored elements

    def hlen(self):
        """Returns number of elements currently stored."""
        return self._hsize

    def blen(self):
        """Returns current number of buckets."""
        return self._bsize

    def is_empty(self):
        """Checks if hash table contains no elements."""
        return self._hsize == 0

    def display(self):
        """Displays hash table structure and chains."""
        print("--")
        if self.is_empty():
            print("Hash table is empty.")
            return
        for bucket in self._hash:
            current = bucket
            flag = False
            if current is not None:
                flag = True
                print(f"{current._key} --> ", end='')
            while current is not None:
                current = current._next
                if current is not None:
                    if current._next is not None:
                        print(f"{current._key},", end=' ')
                    else:
                        print(f"{current._key}", end='')
            if flag:
                print()
        print("--")

    def rehash(self):
        """Doubles table size and redistributes existing elements."""
        new_size = self.blen() * 2
        new_hash = [None] * new_size

        for bucket in self._hash:
            current = bucket
            while current is not None:
                # Reinserts element into new table based on new size
                self.insert(current._key, current._data, new_hash)
                current = current._next
        self._hash = new_hash
        self._bsize = new_size
        print('TABLE REHASHED')

    def insert(self, key, data=None, hash_table=None):
        """Inserts or updates an element."""
        flag = False
        if hash_table is None:
            flag = True
            hash_table = self._hash
        index = key % len(hash_table)
        if hash_table[index] is None:
            new_node = self._Node(key, data)
            hash_table[index] = new_node
        else:
            current = hash_table[index]
            while current is not None:
                if current._key == key:  # Update if key exists
                    current._data = data
                    return
                if current._next is None:
                    break
                current = current._next
            new_node = self._Node(key, data, current)
            current._next = new_node

        # Trigger rehash if load factor exceeded
        if flag:
            self._hsize += 1
            if self.hlen() / self.blen() >= self.REHASH_RATIO:
                self.rehash()

    def delete(self, key):
        """Deletes element with given key, if exists."""
        if self.is_empty():
            print("Hash table is empty.")
            return
        delete = None

        index = key % self.blen()
        current = self._hash[index]

        while current is not None:
            if current._key == key:
                delete = current
            current = current._next

        if delete is None:
            print('No such key exists to delete.')
            return

        if delete == self._hash[index]:
            self._hash[index] = delete._next
            if self._hash[index] is not None:
                self._hash[index]._prev = None
        else:
            if delete._prev is not None:
                delete._prev._next = delete._next
            if delete._next is not None:
                delete._next._prev = delete._prev
        delete._prev = None
        delete._next = None
        self._hsize -= 1

    def retrieve(self, key):
        """Retrieves (key, data) tuple if found, otherwise prints error."""
        if self.is_empty():
            raise EmptyHash("Hash is empty.")
        index = key % self.blen()
        current = self._hash[index]
        found = None
        while current is not None:
            if current._key == key:
                found = current
                break
            current = current._next
        if found is None:
            print('Can not retrieve. No such key exists.')
            return None
        else:
            return found._key, found._data


# ===========================================================
#                TEST DRIVER (MAIN)
# ===========================================================

if __name__ == "__main__":

    hash_table = ChainedHash()

    # Test 1: Insert multiple elements to trigger rehashing
    print("Test 1: Inserting elements to trigger rehashing")
    for i in range(20):
        hash_table.insert(i, f"Data {i}")
    hash_table.display()

    # Test 2: Retrieve inserted elements
    print("\nTest 2: Retrieving elements")
    for i in range(20):
        result = hash_table.retrieve(i)
        assert result == (i, f"Data {i}"), f"Failed to retrieve correct data for key {i}"
    print("All retrievals are successful.")

    # Test 3: Delete some elements
    print("\nTest 3: Deleting elements")
    hash_table.delete(5)
    hash_table.delete(15)
    hash_table.display()

    # Test 4: Retrieve deleted elements
    print("\nTest 4: Retrieving deleted elements")
    assert hash_table.retrieve(5) is None, "Should return None for deleted key 5"
    assert hash_table.retrieve(15) is None, "Should return None for deleted key 15"

    # Test 5: Deleting first and last elements in a chain
    print("\nTest 5: Deleting first and last elements in a chain")
    hash_table.delete(0)
    hash_table.delete(19)
    hash_table.display()

    # Test 6: Inserting duplicate keys
    print("\nTest 6: Inserting duplicate keys")
    print(hash_table.retrieve(10))
    hash_table.insert(10, "New Data for 10")
    print(hash_table.retrieve(10))

    # Test 7: Handling empty hash table and exceptions
    print("\nTest 7: Retrieving from an empty hash table")
    empty_table = ChainedHash()
    try:
        empty_table.retrieve(1)
    except EmptyHash:
        print("Caught expected EmptyHash exception.")

    # Test 8: Delete from an empty hash table
    print("\nTest 8: Deleting from an empty hash table")
    try:
        empty_table.delete(1)
    except Exception as e:
        print(f"Error while deleting from empty table: {e}")

    # Test 9: Inserting None as data
    print("\nTest 9: Inserting None as data")
    hash_table.insert(25, None)
    assert hash_table.retrieve(25) == (25, None), "Failed to handle None as valid data"
    print("Inserted None as data successfully.")

    # Additional inserts for stress testing
    for i in range(0, 1000, 31):
        hash_table.insert(i, f"Data {i}")
    hash_table.display()
    for i in range(0, 1000, 7):
        hash_table.insert(i, f"Data {i}")
    hash_table.display()

    # Test random retrievals
    test_keys = [0, 961, 644, 20, 999, 50]
    for key in test_keys:
        try:
            result = hash_table.retrieve(key)
            if result is not None:
                print(f"Key {key} found with value: {result}")
            else:
                print(f"Key {key} not found.")
        except EmptyHash:
            print("Hash table is currently empty. Cannot retrieve.")

    # Additional reinsertions to test rehashing stability
    for i in range(0, 1000, 31):
        hash_table.insert(i, f"Data {i}")
        hash_table.display()

    # --- Interactive Menu System ---
    print("\n" + "="*50)
    print("INTERACTIVE HASH TABLE MANAGEMENT SYSTEM")
    print("="*50)

    while True:
        print("\nOptions:")
        print("1. Insert key-value pair")
        print("2. Retrieve value by key")
        print("3. Delete key-value pair")
        print("4. Display hash table structure")
        print("5. Show table statistics")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        try:
            if choice == '1':
                # Insert operation
                key = int(input("Enter key (integer): "))
                data = input("Enter data (string): ")
                hash_table.insert(key, data)
                print(f"Successfully inserted key {key} with data: '{data}'")

            elif choice == '2':
                # Retrieve operation
                key = int(input("Enter key to retrieve: "))
                result = hash_table.retrieve(key)
                if result is not None:
                    print(f"Key {result[0]} found with data: '{result[1]}'")
                else:
                    print(f"Key {key} not found in the hash table.")

            elif choice == '3':
                # Delete operation
                key = int(input("Enter key to delete: "))
                hash_table.delete(key)
                print(f"Attempted to delete key {key}")

            elif choice == '4':
                # Display hash structure
                print("\nCurrent Hash Table Structure:")
                hash_table.display()

            elif choice == '5':
                # Display statistics
                print(f"\nHash Table Statistics:")
                print(f"Total elements: {hash_table.hlen()}")
                print(f"Number of buckets: {hash_table.blen()}")
                print(f"Load factor: {hash_table.hlen() / hash_table.blen():.2f}")
                print(f"Table is empty: {hash_table.is_empty()}")

            elif choice == '6':
                print("Thank you for using the Hash Table Management System!")
                break

            else:
                print("Invalid choice! Please enter a number between 1–6.")

        except ValueError:
            print("Invalid input! Please enter an integer where required.")
        except EmptyHash as e:
            print(f"Error: {e}")
        except Exception as e:
            # Unexpected runtime errors
            print(f"Unexpected error occurred: {e}")


