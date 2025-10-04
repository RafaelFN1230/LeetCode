'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2
            carry = total//10
            current.next = ListNode(total % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next


    
# Classe ListNode e função addTwoNumbers já definidas aqui

def create_linked_list(numbers):
    """Cria uma lista ligada a partir de uma lista de números."""
    dummy = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(node):
    """Imprime os valores de uma lista ligada."""
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)

# Exemplo de uso
if __name__ == "__main__":
    # Cria as listas ligadas
    l1 = create_linked_list([2, 4, 3])  # Representa o número 342
    l2 = create_linked_list([5, 6, 4])  # Representa o número 465

    # Cria a solução
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Imprime o resultado
    print("Resultado da soma:")
    print_linked_list(result)  # Deve imprimir [7, 0, 8], que representa 807