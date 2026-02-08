class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []
    
    def heapify_up(self, index):
        """Move a patient up the heap if their urgency is lower than parent"""
        while index > 0:
            parent_index = (index - 1) // 2
            
            if self.data[index].urgency < self.data[parent_index].urgency:
                # Swap with parent
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break
    
    def heapify_down(self, index):
        """Move a patient down the heap if their urgency is higher than a child"""
        while True:
            smallest = index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            
            # Check if left child exists and has lower urgency
            if left_child_index < len(self.data) and self.data[left_child_index].urgency < self.data[smallest].urgency:
                smallest = left_child_index
            
            # Check if right child exists and has lower urgency than current smallest
            if right_child_index < len(self.data) and self.data[right_child_index].urgency < self.data[smallest].urgency:
                smallest = right_child_index
            
            # If smallest is not the current index, swap and continue
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break
    
    def insert(self, patient):
        """Add a new patient to the heap and reorder using heapify_up"""
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)
    
    def print_heap(self):
        """Print all patients in the current queue"""
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")
    
    def peek(self):
        """Return the patient with highest priority without removing them"""
        if len(self.data) > 0:
            return self.data[0]
        return None
    
    def remove_min(self):
        """Remove and return the patient with highest priority (lowest urgency)"""
        if len(self.data) == 0:
            return None
        
        # Get the root (highest priority patient)
        min_patient = self.data[0]
        
        # Move last patient to root
        self.data[0] = self.data[-1]
        self.data.pop()
        
        # Restore heap property
        if len(self.data) > 0:
            self.heapify_down(0)
        
        return min_patient




# Test your MinHeap class here including edge cases

if __name__ == "__main__":
    print("=== Testing MinHeap Edge Cases ===\n")
    
    # Test 1: Basic operations
    print("Test 1: Basic insertions and print_heap()")
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    print()
    
    # Test 2: Peek and remove
    print("Test 2: Peek and remove_min()")
    next_patient = heap.peek()
    print(f"Peek: {next_patient.name} (urgency {next_patient.urgency})")
    removed = heap.remove_min()
    print(f"Removed: {removed.name}")
    heap.print_heap()
    print()
    
    # Test 3: Empty heap edge case
    print("Test 3: Empty heap operations")
    empty_heap = MinHeap()
    print(f"Peek on empty heap: {empty_heap.peek()}")
    print(f"Remove from empty heap: {empty_heap.remove_min()}")
    print()
    
    # Test 4: Single element
    print("Test 4: Single element heap")
    single_heap = MinHeap()
    single_heap.insert(Patient("Solo", 7))
    single_heap.print_heap()
    single_heap.remove_min()
    print(f"After removal, heap is empty: {len(single_heap.data) == 0}")

# MEMO 
# A tree structure is ideal for representing a doctor hierarchy because it models reporting and organizational chains of command. 
# Each doctor has a single supervisor, parent, and can oversee multiple subordinates (children). This is very similiar to real world 
# medical departments where authority rains down. Trees also enable efficient searching for specific doctors and allow easy 
# traversal of entire reporting structures.

# Preorder traversal is useful when processing a hierarchy top-down. Traversal works well for outputting data in a partially sorted manner, 
# like generating an organized list of doctors by department level. Postorder traversal is essential for bottom-up processing. 
# These methods are critical for different reporting and management tasks in organizational hierarchies.

# Heaps are essential for emergency intake systems because they automatically maintain priority ordering with minimal computation. 
# Unlike sorting an entire patient list each time someone arrives, a min-heap insertion operates in O(log n) time, meaning that a hospital 
# can instantly add new patients and always know who needs immediate attention without expensive sorting operations. As patients are 
# treated and removed, the heap reorganizes itself. This real-time priority management is crucial in emergency rooms where delays can be life-threatening.