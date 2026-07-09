/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        // We will use a hash map (unordered_map in C++) to store the mapping
        // from the original nodes to their newly created copies. This allows
        // us to find a copied node quickly when we need to assign its pointers.
        std::unordered_map<Node*, Node*> originalToCopyMap;

        // An important optimization: we add a mapping for a NULL pointer.
        // This prevents us from having to write a check (if-statement)
        // for null pointers later when we're assigning the 'next' and 'random'
        // pointers. If an original pointer is NULL, its copy should also be NULL.
        originalToCopyMap[nullptr] = nullptr;

        // --- Pass 1: Create all the new nodes ---
        // In the first pass, we simply iterate through the original list
        // and create a new node for each one. We don't worry about linking
        // them yet because the node that a 'random' pointer points to might
        // not have been created yet.
        Node* currentNode = head;
        while (currentNode != nullptr) {
            // Create a new node with the same value as the original.
            Node* copiedNode = new Node(currentNode->val);

            // Store the mapping in our hash map: original -> copy.
            originalToCopyMap[currentNode] = copiedNode;

            // Move to the next node in the original list.
            currentNode = currentNode->next;
        }

        // --- Pass 2: Assign pointers for the new nodes ---
        // Now that all the new nodes exist and are in our map, we can
        // iterate through the original list again to assign the 'next'
        // and 'random' pointers of the new nodes.
        currentNode = head;
        while (currentNode != nullptr) {
            // Get the copied node corresponding to the current original node.
            Node* copiedNode = originalToCopyMap[currentNode];

            // Assign the 'next' pointer of the new node.
            // We use the map to find the copy of the original node's 'next' pointer.
            copiedNode->next = originalToCopyMap[currentNode->next];

            // Assign the 'random' pointer of the new node.
            // We use the map to find the copy of the original node's 'random' pointer.
            copiedNode->random = originalToCopyMap[currentNode->random];

            // Move to the next node in the original list.
            currentNode = currentNode->next;
        }

        // The head of the new list is the copied version of the original head,
        // which we can retrieve from our map.
        return originalToCopyMap[head];
    }
};