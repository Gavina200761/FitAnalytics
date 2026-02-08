class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None
    
    def insert(self, parent_name, child_name, side):
        """Insert a child node to a parent node in the tree"""
        if self.root is None:
            return
        
        # Find the parent node
        parent_node = self._find_node(self.root, parent_name)
        if parent_node is None:
            return
        
        # Create new child node
        child_node = DoctorNode(child_name)
        
        # Attach to the appropriate side
        if side == "left":
            parent_node.left = child_node
        elif side == "right":
            parent_node.right = child_node
    
    def _find_node(self, node, name):
        """Helper method to find a node by name"""
        if node is None:
            return None
        
        if node.name == name:
            return node
        
        # Search in left subtree
        left_result = self._find_node(node.left, name)
        if left_result is not None:
            return left_result
        
        # Search in right subtree
        return self._find_node(node.right, name)
    
    def preorder(self, node):
        """Preorder traversal: root, left, right"""
        if node is None:
            return []
        
        result = [node.name]
        result.extend(self.preorder(node.left))
        result.extend(self.preorder(node.right))
        return result
    
    def inorder(self, node):
        """Inorder traversal: left, root, right"""
        if node is None:
            return []
        
        result = self.inorder(node.left)
        result.append(node.name)
        result.extend(self.inorder(node.right))
        return result
    
    def postorder(self, node):
        """Postorder traversal: left, right, root"""
        if node is None:
            return []
        
        result = self.postorder(node.left)
        result.extend(self.postorder(node.right))
        result.append(node.name)
        return result




# Test your DoctorTree and DoctorNode classes here

if __name__ == "__main__":
    print("=== Testing DoctorTree and DoctorNode ===\n")
    
    # Test 1: Basic tree construction and traversals
    print("Test 1: Basic tree construction and traversals")
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")
    
    print(f"Preorder: {tree.preorder(tree.root)}")
    print(f"Inorder: {tree.inorder(tree.root)}")
    print(f"Postorder: {tree.postorder(tree.root)}")
    print()
    
    # Test 2: Insert with non-existent parent
    print("Test 2: Try to insert with non-existent parent")
    tree.insert("Dr. NonExistent", "Dr. Smith", "left")
    print(f"After insert with non-existent parent - Preorder: {tree.preorder(tree.root)}")
    print("(No change expected)")
    print()
    
    # Test 3: Insert with invalid side value
    print("Test 3: Try to insert with invalid side value")
    tree.insert("Dr. Croft", "Dr. Invalid", "middle")
    print(f"After insert with invalid side - Preorder: {tree.preorder(tree.root)}")
    print("(No change expected, invalid side is ignored)")
    print()
    
    # Test 4: Insert with valid side but non-existent parent
    tree2 = DoctorTree()
    print("Test 4: Tree with no root element")
    tree2.insert("Dr. Someone", "Dr. Anyone", "left")
    print(f"Attempting to insert into empty tree - Root is None: {tree2.root is None}")
    print()
    
    # Test 5: Single node tree traversal
    print("Test 5: Single node tree traversal")
    tree3 = DoctorTree()
    tree3.root = DoctorNode("Dr. Solo")
    print(f"Preorder: {tree3.preorder(tree3.root)}")
    print(f"Inorder: {tree3.inorder(tree3.root)}")
    print(f"Postorder: {tree3.postorder(tree3.root)}")
    print()
    
    # Test 6: Overwriting an existing child
    print("Test 6: Overwriting an existing child")
    tree.insert("Dr. Croft", "Dr. NewDoctor", "left")
    print(f"After overwriting left child of Dr. Croft - Preorder: {tree.preorder(tree.root)}")
    print(f"(Dr. Phan and its subtree are replaced by Dr. NewDoctor)")
