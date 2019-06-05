
class MaxHeap:
    """
    NOTE: this class has been modified in two places. The swap function now also swaps the auxiliary vertex array as
    needed. It also has a new method update which updates a specific node's value in the heap and proceeds to
    restore the order of the heap

    The following class is an implementation of a maximum based heap. A heaps completeness guarantees an insert and
    search time of O(depth) = O(logn) where n is the number of elements/nodes

    The following implementation was provided by the resources from FIT2085 and modified accordingly to use nodes of
    type (WORD, FREQUENCY)
        https://lms.monash.edu/pluginfile.php/6452929/mod_resource/content/11/L33_Heaps.pdf
        https://lms.monash.edu/pluginfile.php/6452930/mod_resource/content/11/L34_35_HeapsII.pdf

    @space complexity = O(n) where n is the number of elements in the heap
    @time complexity (insert) = O(depth) = O(logn) where n is the number of elements/nodes
    @time complexity (search) = O(depth) = O(logn) where n is the number of elements/nodes
    @time complexity (get root) = O(1)
    """

    def __init__(self):
        self.count = 0
        self.the_array = [None]

    def __len__(self):
        return self.count

    def swap(self, a, b):
        # swapping
        temp = self.the_array[a]
        self.the_array[a] = self.the_array[b]
        self.the_array[b] = temp

    def is_full(self):
        return self.count + 1 == len(self.the_array)

    def rise(self, k):
        while k > 1 and self.the_array[k][1] > self.the_array[k // 2][1]: #swapped < to >
            self.swap(k, k // 2)
            k = k // 2
        return k

    def add(self, element):
        has_space_left = not self.is_full()

        if has_space_left:
            self.count += 1
            self.the_array[self.count] = element
            self.rise(self.count)
        return has_space_left

    def peek_max(self):
        return self.the_array[1]

    def get_max(self):
        # pops root node off heap
        self.swap(1, self.count)
        max = self.the_array[self.count]
        self.count -= 1
        self.sink(1)
        return max

    def largest_child(self, k):
        if 2 * k == self.count or self.the_array[2 * k][1] > self.the_array[2 * k + 1][1]: #swapped < to >
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k):
        while 2 * k <= self.count:
            child = self.largest_child(k)
            if self.the_array[k][1] >= self.the_array[child][1]: #swapped to from <= to >=
                break
            self.swap(child, k)
            k = child