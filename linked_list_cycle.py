# Linked List Cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # contains_cycle = False
        while(head.next):
            print(head.val)
            head = head.next
            

        # return contains_cycle
# single node of a singly linked list
class node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
        
class linked_list:
    def __init__(self):
        self.head = None

    def insert(self, val, next=None):
        if(next):
            new_node = node(val,next)
        else:
            new_node = node(val)
        if (self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    def get_node(self, idx):
        current = self.head
        for i in range(idx):
            current = current.next
        return current
    def loop_check(self):
        current = self.head
        for i in range(10):
            print(current.val)
            current = current.next




def main():
    sol = Solution()
    LL_1 = linked_list()
    LL_1.insert(3); LL_1.insert(2); LL_1.insert(0); LL_1.insert(-4, LL_1.get_node(1))

    sol.hasCycle(LL_1.get_node(0))
    print("hello world")

if __name__ == "__main__":
    main()