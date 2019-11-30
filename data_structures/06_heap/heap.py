"""
Implementation of 06_heap data structure
We need to construct a 06_heap to operate on it so
Step 1. Construct a 06_heap

Operations which could be performed on the created
06_heap is
1. Insert a node
2. Delete a node (note: you can only delete the top most node from the 06_heap)
"""


class Heap(object):
    def __init__(self, heap_array):
        self.heap_array = []
        self.create_heap(heap_array)

    def create_heap(self, inp_array):
        """
            Method creates 06_heap during object initialization
        :param inp_array: array of elements which is used in 06_heap construction
        :return: constructed 06_heap
        """
        for node in inp_array:
            self.insert_node(node)

    def insert_node(self, node):
        # insert the node at the end of array
        self.heap_array.append(node)
        cur_node_index = len(self.heap_array) - 1
        # keep comparing node with parent nodes
        while cur_node_index > 0:
            parent_index = (cur_node_index - 1) // 2
            # if inserted node is greater than compared parent
            # swap values
            # and update cur_value
            if self.heap_array[parent_index] < node:
                self.heap_array[cur_node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = node
                cur_node_index = parent_index
            else:
                break

    def delete_top_node(self):
        if len(self.heap_array) == 0:
            print("Heap empty")
            return None
        else:
            # always pull top element from 06_heap and replace with element in the last
            extracted_element = self.heap_array[0]
            self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]
            #
            self.heap_array = self.heap_array[:len(self.heap_array) - 1]
            cur_node_index = 0
            while cur_node_index < len(self.heap_array):
                # compare last element with biggest children
                l_child_index = cur_node_index * 2 + 1 if cur_node_index * 2 + 1 < len(self.heap_array) else False
                r_child_index = cur_node_index * 2 + 2 if cur_node_index * 2 + 2 < len(self.heap_array) else False
                # find bigger children index
                if l_child_index and r_child_index:
                    bigger_children_index = l_child_index if self.heap_array[l_child_index] > self.heap_array[
                        r_child_index] else r_child_index

                    if self.heap_array[cur_node_index] < self.heap_array[bigger_children_index]:
                        buff_value = self.heap_array[cur_node_index]
                        self.heap_array[cur_node_index] = self.heap_array[bigger_children_index]
                        self.heap_array[bigger_children_index] = buff_value
                        cur_node_index = bigger_children_index
                    else:
                        break
                if l_child_index and r_child_index is False:
                    if self.heap_array[cur_node_index] < self.heap_array[l_child_index]:
                        buff_value = self.heap_array[cur_node_index]
                        self.heap_array[cur_node_index] = self.heap_array[l_child_index]
                        self.heap_array[l_child_index] = buff_value
                        cur_node_index = l_child_index
                    else:
                        break
                if r_child_index and l_child_index is False:
                    if self.heap_array[cur_node_index] < self.heap_array[r_child_index]:
                        buff_value = self.heap_array[cur_node_index]
                        self.heap_array[cur_node_index] = self.heap_array[r_child_index]
                        self.heap_array[r_child_index] = buff_value
                        cur_node_index = r_child_index
                    else:
                        break
                else:
                    break

            return extracted_element


if __name__ == "__main__":
    heap = Heap([1, 2, 3, 4, 5, 6, 7])
    heap.insert_node(10)
    heap.insert_node(12)
    heap.insert_node(15)
    heap.insert_node(20)
    heap.insert_node(40)
    print("Created 06_heap value is ", heap.heap_array)
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
    print("Deleting node in 06_heap, max value found is ", heap.delete_top_node())
