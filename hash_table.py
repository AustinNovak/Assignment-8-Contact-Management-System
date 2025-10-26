# Contact class stores a name and phone number
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Node class represents each element in the linked list
class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None

# HashTable class using separate chaining for collision handling
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Simple hash function based on character sum
    def _hash(self, name):
        return sum(ord(char) for char in name) % self.size

    # Insert or update a contact
    def insert(self, name, phone):
        index = self._hash(name)
        new_contact = Contact(name, phone)
        new_node = Node(new_contact)

        # If bucket is empty, place directly
        if self.table[index] is None:
            self.table[index] = new_node
            return

        # Otherwise, handle collision (chaining)
        current = self.table[index]
        while current:
            # Update number if contact already exists
            if current.contact.name == name:
                current.contact.phone = phone
                return
            if current.next is None:
                break
            current = current.next
        current.next = new_node

    # Search for a contact by name
    def search(self, name):
        index = self._hash(name)
        current = self.table[index]
        while current:
            if current.contact.name == name:
                return current.contact.phone
            current = current.next
        return None

    # Print full hash table contents
    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.table[i]
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"- {current.contact.name}: {current.contact.phone}", end=" ")
                    current = current.next
                print()

# TEST CASES

# Create hash table
table = HashTable(10)

# Insert initial values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

# Edge Case #1 - Hash Collisions
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function
table.print_table()

'''
Expected output:
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111
Index 6: Empty
Index 7: - Rebecca: 111-555-0002
Index 8: Empty
Index 9: - John: 909-876-1234
'''

# Edge Case #2 - Duplicate Keys
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number
table.print_table()

'''
Expected output:
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111
Index 6: Empty
Index 7: - Rebecca: 999-444-9999
Index 8: Empty
Index 9: - John: 909-876-1234
'''

# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris"))  # None


'''
Design Memo:

This program demonstrates how a hash table can be used to efficiently store and manage
contact information such as names and phone numbers. Each contact is represented as an
object of the Contact class, which stores a name and a phone number. The Node class is
used to form linked lists within each hash table bucket, enabling a technique called
separate chaining to handle collisions (when two names hash to the same index).

The HashTable class defines the structure and main behaviors of the table. The _hash()
method generates an index based on the sum of character values in a contact's name.
The insert() method either adds a new contact or updates an existing one if the same
name already exists. If two contacts hash to the same index, the new contact is added
to the linked list at that index, maintaining data integrity.

The search() method locates a contact by name, returning the stored phone number or
None if not found. The print_table() method displays the current state of the table,
including all linked list contents for each index.

Edge cases were tested for:
1. Hash collisions — multiple contacts stored under the same index.
2. Duplicate entries — updating an existing contact’s number.
3. Missing contacts — searching for a name not in the table.

This structure illustrates how chaining provides a simple yet reliable way to resolve
collisions while maintaining efficient access and insertion times for contact data.
'''
