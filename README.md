# CS605_Fall24_Snehitha_Gorantla

The TreeNode class represents a single node in the tree, which holds a name, phone number, and pointers to its left and right children.

•	self.left: The left child (where names are smaller).

•	self.right: The right child (where names are larger).

The BinarySearchTree class defines the BST operations:

__ init__ function initializes an empty tree i.e., root is None.

The insert function inserts a new node with a given name and phone number into the correct position in the BST.

•	If the tree is empty, it creates the new node as the root.

•	It uses the helper function _insert_recursive to compare names and recursively find the correct position for the new node.

•	If the name is already present, it updates the phone number.

The search function searches for a node with a given name and returns its phone number.

•	It uses a recursive helper function _search_recursive to traverse the tree.

•	It compares the name with each node then, goes left for smaller names and right for larger names.


The inorder_traversal function prints all the nodes of the tree in sorted order which is alphabetical by name.

•	It uses _inorder_recursive, a recursive helper function, to first visit the left subtree, print the current node, and then visit the right subtree.

The delete function deletes a node with a given name from the tree.

•	It uses the helper function _delete_recursive, which finds the node to delete and handles three cases: deleting a leaf node, deleting a node with one child and deleting a node with two children.

•	For deleting a node with two children the node’s data is replaced by its in-order successor which is the smallest node in the right subtree and the in-order successor is removed from the tree.

The _min_value_node function is used to find the smallest node or leftmost node in the right subtree when deleting a node with two children.

Output:

![image](https://github.com/user-attachments/assets/d9beffc3-2216-4509-bbc6-45b0407b17b8)
![image](https://github.com/user-attachments/assets/336d87cd-00b3-4ac9-9a3e-4d673b822268)
