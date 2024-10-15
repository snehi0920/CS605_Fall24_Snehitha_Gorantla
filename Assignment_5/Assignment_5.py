class TreeNode:
    # Initialize a node with a name and phone number
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        # Left child
        self.left = None  
        # Right child
        self.right = None  

class BinarySearchTree:
    # Initialize an empty BST
    def __init__(self):
        self.root = None

    # Insert a new node with a name and phone number into the BST
    def insert(self, name, phone_number):
        # If the tree is empty, create a new root node
        if not self.root:
            self.root = TreeNode(name, phone_number)
        else:
            # Otherwise, recursively find the correct position to insert the node
            self._insert_recursive(self.root, name, phone_number)

    # Recursive helper method for insertion
    def _insert_recursive(self, node, name, phone_number):
        # If the name is smaller than the current node's name, go left
        if name < node.name:
            # If there's no left child, insert the new node here
            if node.left is None:
                node.left = TreeNode(name, phone_number)
            else:
                # Otherwise, recursively insert in the left subtree
                self._insert_recursive(node.left, name, phone_number)
        # If the name is greater than the current node's name, go right
        elif name > node.name:
            # If there's no right child, insert the new node here
            if node.right is None:
                node.right = TreeNode(name, phone_number)
            else:
                # Otherwise, recursively insert in the right subtree
                self._insert_recursive(node.right, name, phone_number)
        else:
            # If the name already exists, update the phone number
            node.phone_number = phone_number

    # Search for a node by name and return the corresponding phone number
    def search(self, name):
        return self._search_recursive(self.root, name)

    # Recursive helper method for searching
    def _search_recursive(self, node, name):
        # Base case: node is None or we found the node with the matching name
        if node is None or node.name == name:
            # Return the phone number if found, otherwise return None
            return node.phone_number if node else None
        
        # If the name is smaller than the current node's name, search in the left subtree
        if name < node.name:
            return self._search_recursive(node.left, name)
        # If the name is greater, search in the right subtree
        return self._search_recursive(node.right, name)

    # In-order traversal to print all nodes in the tree in sorted order
    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    # Recursive helper method for inorder traversal
    def _inorder_recursive(self, node):
        if node:
            # Traverse left subtree
            self._inorder_recursive(node.left)
            # Process current node
            print(f"Name: {node.name}, Phone: {node.phone_number}")
            # Traverse right subtree
            self._inorder_recursive(node.right)
    
    # Delete a node with the given name from the BST
    def delete(self, name):
        self.root = self._delete_recursive(self.root, name)

    # Recursive helper function for deletion
    def _delete_recursive(self, node, name):
        # Base case: if the current node is None, the name was not found in the tree
        if not node:
            return None

        # If the name to be deleted is smaller, go to the left subtree
        if name < node.name:
            node.left = self._delete_recursive(node.left, name)
        # If the name to be deleted is larger, go to the right subtree
        elif name > node.name:
            node.right = self._delete_recursive(node.right, name)
        else:
            # Node to be deleted is found
            # Case 1: The node has no left child or a leaf node
            if not node.left:
                # Replace the node with its right child
                return node.right  
            # Case 2: The node has no right child
            elif not node.right:
                # Replace the node with its left child
                return node.left  

            # Case 3: The node has two children.
            # Find the smallest node in the right subtree (the in-order successor)
            temp = self._min_value_node(node.right)

            # Replace the current node's name and phone number with that of the in-order successor
            node.name = temp.name
            node.phone_number = temp.phone_number

            # Recursively delete the in-order successor from the right subtree
            node.right = self._delete_recursive(node.right, temp.name)

        # Return the updated node after deletion
        return node

    # Helper function to find the node with the smallest value (leftmost node) in a subtree
    def _min_value_node(self, node):
        current = node
        # Traverse down the left children to find the smallest value
        while current.left:
            current = current.left
        # Return the leftmost node
        return current  

# Test cases
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Test case 1: Insertion and inorder traversal
    print("Test case 1: Insertion and inorder traversal")
    bst.insert("Akshay", "(530)321-5407")
    bst.insert("Himanshu", "(530)321-7038")
    bst.insert("Jayana", "(530)965-7439")
    bst.insert("Nayana", "(530)630-7166")
    bst.insert("Snehitha", "(530)636-5202")
    print("Inorder traversal after insertion:")
    bst.inorder_traversal()
    print()

    # Test case 2: Searching
    print("Test case 2: Searching")
    print("Akshay's phone number:", bst.search("Akshay"))
    print("Himanshu's phone number:", bst.search("Himanshu"))
    print("Venika's phone number:", bst.search("Venika"))  # Should return None
    print()

    # Test case 3: Deleting a leaf node
    print("Test case 3: Deleting a leaf node (Snehitha)")
    bst.delete("Snehitha")
    print("Inorder traversal after deleting Snehitha:")
    bst.inorder_traversal()
    print()

    # Test case 4: Deleting a node with one child
    print("Test case 4: Deleting a node with one child (Nayana)")
    # Reinsert Nayana
    bst.insert("Nayana", "(530)630-7166")  
    bst.delete("Nayana")
    print("Inorder traversal after deleting Nayana:")
    bst.inorder_traversal()
    print()

    # Test case 5: Deleting a node with two children
    print("Test case 5: Deleting a node with two children (Himanshu)")
    bst.delete("Himanshu")
    print("Inorder traversal after deleting Himanshu:")
    bst.inorder_traversal()
    print()

    # Test case 6: Deleting the root
    print("Test case 6: Deleting the root (Akshay)")
    bst.delete("Akshay")
    print("Inorder traversal after deleting Akshay:")
    bst.inorder_traversal()
    print()

    # Test case 7: Deleting a non-existent node
    print("Test case 7: Deleting a non-existent node (Venika)")
    bst.delete("Venika")
    print("Inorder traversal after attempting to delete Venika:")
    bst.inorder_traversal()
    print()

    # Test case 8: Updating an existing entry
    print("Test case 8: Updating Jayana's phone number")
    bst.insert("Jayana", "(530)965-7430")
    print("Inorder traversal after updating Jayana's number:")
    bst.inorder_traversal()