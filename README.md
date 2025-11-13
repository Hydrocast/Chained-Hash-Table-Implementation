# Chained Hash Map Implementation

**Author:** Giannis Loizou  
**Description:** Custom implementation of a **chained hash table** (linked-list-based collision handling) with **dynamic rehashing** support.  

This project demonstrates the design, implementation, and testing of a hash table data structure, including handling collisions, automatic resizing, and an interactive command-line interface for testing and exploration.

---

## Features

- **Chained Hashing:** Handles collisions using linked lists for each bucket.
- **Rehashing:** Automatically doubles the bucket size when load factor exceeds 2.0.
- **CRUD Operations:**
  - Insert key-value pairs
  - Retrieve values by key
  - Delete entries
- **Interactive Menu:** Command-line interface to manage the hash table manually.
- **Edge Case Handling:** Supports empty hash table operations, duplicate key updates, and `None` values as data.
- **Statistics:** Displays table size, number of elements, and load factor.

---

## Technology & Concepts

- **Programming Language:** Python 3  
- **Data Structures:** Linked Lists, Hash Tables  
- **Concepts:** Collision handling, dynamic resizing (rehashing), load factor, key-value storage  
- **Soft Skills Applied:** Testing, debugging, user interaction design

---

## Project Structure

- **`ChainedHash` Class:** Core implementation of the hash table.
- **Node Class:** Internal linked-list node for collision chains.
- **Test Driver (Main):**  
  - Automatic tests for insertion, retrieval, deletion, duplicates, rehashing, and edge cases.  
  - Interactive menu for manual testing.

---

## Usage

1. Clone the repository:
git clone https://github.com/Hydrocast/Chained-Hash-Map-Implementation.git
2. cd ChainedHashMap
3. Run the Python script:
python3 chained_hash.py
4. Follow the interactive menu to:
- Insert key-value pairs
- Retrieve data
- Delete entries
- Display table structure
- View statistics

Notes: 
- Keys must be integers. Values can be strings or None.
- The system also handles rehashing automatically once the load factor exceeds 2.0.

---
 
## Testing
- The implementation includes extensive automated testing:
- Insert 20+ elements to trigger rehashing
- Retrieve inserted elements
- Delete elements (including first/last in chains)
- Test duplicate insertion updates
- Edge cases (empty table operations, None values)
- Interactive tests allow manual verification of the hash table's correctness.

