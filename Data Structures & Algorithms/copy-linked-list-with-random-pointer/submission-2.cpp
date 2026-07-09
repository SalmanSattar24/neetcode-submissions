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

        unordered_map<Node*, Node*> nodes_map;
        nodes_map[NULL] = NULL;

        Node* cur = head;
        while (cur != NULL) {
            Node* copy = new Node(cur->val);
            nodes_map[cur] = copy;
            cur = cur->next;
        }

        cur = head;
        while (cur != NULL) {
            Node* copy = nodes_map[cur];
            copy->next = nodes_map[cur->next];
            copy->random = nodes_map[cur->random];
            cur = cur->next;
        }

        return nodes_map[head];
        
    }
};
