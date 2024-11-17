class ListNode:
    """
    Definition for a singly-linked list node.
    """

    def __init__(self, value=0, next_node=None):
        """
        Initialize a ListNode.

        Args:
            value (int): The value of the node.
            next_node (ListNode): The next node in the linked list.
        """
        self.value = value
        self.next = next_node


class LinkedListOperations:
    """
    Class containing operations on a linked list.
    """

    @staticmethod
    def delete_middle_node(head: ListNode) -> ListNode:
        """
        Delete the middle node of a singly linked list.
        If the list has only one node, return None.

        Args:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The head of the modified linked list.
        """
        if not head or not head.next:
            return None  # Return None if the list is empty or has only one node

        # Initialize pointers for traversal
        previous_node = head
        slow_pointer = head
        fast_pointer = head

        # Traverse the list to find the middle node
        while fast_pointer and fast_pointer.next:
            previous_node = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        # Remove the middle node
        previous_node.next = slow_pointer.next
        slow_pointer.next = None

        return head


# Example usage
if __name__ == "__main__":
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list of values
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result

    # Create a linked list
    values = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(values)

    # Perform the delete middle node operation
    linked_list_operations = LinkedListOperations()
    modified_list = linked_list_operations.delete_middle_node(linked_list)

    # Convert the modified linked list back to a list and print it
    print(linked_list_to_list(modified_list))


# Expected Output
# [1, 2, 4, 5]
