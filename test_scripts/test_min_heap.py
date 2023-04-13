from MinHeap import MinHeap
from random import randint
'''
TODO: 

'''
def test_initializer_and_build_heap():
    min_heap_1 = MinHeap()
    min_heap_2 = MinHeap([6, 5, 4, 3, 2, 1, 0])
    min_heap_3 = MinHeap([0, 1, 2, 3, 4, 5, 6])
    min_heap_4 = MinHeap([0, -10, -15, -2, 4, 4])
    min_heap_5 = MinHeap([6, 5])

    assert min_heap_1.get_items_as_list() == []
    assert min_heap_2.get_items_as_list() == [0, 2, 1, 3, 5, 6, 4]
    assert min_heap_3.get_items_as_list() == [0, 1, 2, 3, 4, 5, 6]
    assert min_heap_4.get_items_as_list() == [-15, -10, 0, -2, 4, 4]
    assert min_heap_5.get_items_as_list() == [5, 6]
    
def test_size():
    min_heap = MinHeap()
    assert min_heap.size == 0
    
    min_heap.insert([1, 2, 3]) 
    assert min_heap.size == 3
    
def test_is_empty():
    min_heap = MinHeap()
    assert min_heap.is_empty is True
    
    min_heap.insert(1)
    assert min_heap.is_empty is False

def test_height():
    min_heap = MinHeap([])
    assert min_heap.height == 0
    
    min_heap = MinHeap([1])
    assert min_heap.height == 0
    
    min_heap = MinHeap([1, 2])
    assert min_heap.height == 1
    
    min_heap = MinHeap([1, 2, 3])
    assert min_heap.height == 1
    
    min_heap = MinHeap([1, 2, 3, 4])
    assert min_heap.height == 2
    
    min_heap = MinHeap([1, 2, 3, 4, 5, 6, 7])
    assert min_heap.height == 2
    
    min_heap = MinHeap([1, 2, 3, 4, 5, 6, 7])
    assert min_heap.height == 2
    
    min_heap = MinHeap([i for i in range(20)])
    assert min_heap.height == 4

def test_is_heap():
    min_heap = MinHeap([6, 5, 4, 3, 2, 1, 0])
    assert min_heap.is_heap is True
    
    min_heap.heap_sort_ascending()
    assert min_heap.is_heap is True
    
    '''
    Currently, unless the user illegally changes self._items,
    there is not a condition in the class that will make is_heap false. 
    
    The implementation of is_heap will not check heap validity, 
    instead its' truth value is changed by other methods when
    they modify the heap. The only method planned so far for this class
    that can make is_heap false, is heap_sort_descending,
    which is the "proper" heap_sort for a min heap.
    
    is_heap will eventually be changed to run an algorithm to check
    if the heap is valid.
    '''

def test_heap_sort_ascending():
    min_heap = MinHeap([randint(-1000, 1000) for _ in range(100)])
    min_heap.heap_sort_ascending()
    
    assert min_heap.size == 100
    
    # See if we can change the class so that we can loop through it, instead of having to get the list.
    items = min_heap.get_items_as_list()
    for i in range(items.__len__() - 1):
        assert items[i] <= items[i + 1]
    
    min_heap = MinHeap([1, 0])
    min_heap.heap_sort_ascending()
    assert min_heap.get_items_as_list() == [0, 1]
    
    min_heap = MinHeap([1])
    min_heap.heap_sort_ascending()
    assert min_heap.get_items_as_list() == [1]
    
    min_heap = MinHeap([])
    min_heap.heap_sort_ascending()
    assert min_heap.get_items_as_list() == []
    
    min_heap = MinHeap([0, 1, 2, 3, 4, 5, 6])
    min_heap.heap_sort_ascending()
    assert min_heap.get_items_as_list() == [0, 1, 2, 3, 4, 5, 6]
        
def test_insert():
    min_heap = MinHeap()
    
    min_heap.insert(6)
    min_heap.insert(5)
    min_heap.insert(4)
    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.insert(1)
    min_heap.insert(0)
    assert min_heap.get_items_as_list() == [0, 3, 1, 6, 4, 5, 2]
    
    min_heap.clear()
    min_heap.insert([6, 5, 4, 3, 2, 1, 0])
    assert min_heap.get_items_as_list() == [0, 3, 1, 6, 4, 5, 2]
    
    min_heap.clear()
    min_heap.insert(0)
    min_heap.insert(1)
    min_heap.insert(2)
    min_heap.insert(3)
    min_heap.insert(4)
    min_heap.insert(5)
    min_heap.insert(6)
    assert min_heap.get_items_as_list() == [0, 1, 2, 3, 4, 5, 6]
    
    min_heap.clear()
    min_heap.insert([0, 1, 2, 3, 4, 5, 6])
    assert min_heap.get_items_as_list() == [0, 1, 2, 3, 4, 5, 6]
    
    min_heap.clear()
    min_heap.insert(0)
    min_heap.insert(1)
    min_heap.insert(6)
    min_heap.insert(5)
    min_heap.insert(4)
    min_heap.insert(3)
    min_heap.insert(2)
    assert min_heap.get_items_as_list() == [0, 1, 2, 5, 4, 6, 3]
    
    min_heap.clear()
    min_heap.insert([0, 1, 6, 5, 4, 3, 2])
    assert min_heap.get_items_as_list() == [0, 1, 2, 5, 4, 6, 3]
    
    min_heap.clear()
    min_heap.insert(0)
    min_heap.insert(-1)
    min_heap.insert(-2)
    min_heap.insert(-3)
    min_heap.insert(-4)
    min_heap.insert(-5)
    min_heap.insert(-6)
    assert min_heap.get_items_as_list() == [-6, -3, -5, 0, -2, -1, -4]
    
    min_heap.clear()
    min_heap.insert([0, -1, -2, -3, -4, -5, -6])
    assert min_heap.get_items_as_list() == [-6, -3, -5, 0, -2, -1, -4]
    
    min_heap.clear()
    min_heap.insert(1)
    min_heap.insert(1)
    min_heap.insert(1)
    min_heap.insert(1)
    min_heap.insert(1)
    min_heap.insert(0)
    min_heap.insert(1)
    assert min_heap.get_items_as_list() == [0, 1, 1, 1, 1, 1, 1]
    
    min_heap.clear()
    min_heap.insert([1, 1, 1, 1, 1, 0, 1])
    assert min_heap.get_items_as_list() == [0, 1, 1, 1, 1, 1, 1]
    
def test_extract_min():
    min_heap = MinHeap() 

    min_num = 1000
    for _ in range(1000):
        num = randint(-1000, 1000)
        min_heap.insert(num)
        if num < min_num:
            min_num = num
    assert min_heap.extract_min() == min_num, f"Expected {min_num}, got {min_heap.extract_min()}"
    
    min_heap.clear()
    min_heap.insert([0, 1, 2])
    assert min_heap.extract_min() == 0
    assert min_heap.size == 2
    assert min_heap.extract_min() == 1
    assert min_heap.size == 1
    assert min_heap.extract_min() == 2
    assert min_heap.size == 0
    
    min_heap.clear()
    min_heap.insert([2, 1, 0])
    assert min_heap.extract_min() == 0
    assert min_heap.size == 2
    assert min_heap.extract_min() == 1
    assert min_heap.size == 1
    assert min_heap.extract_min() == 2
    assert min_heap.size == 0
    
    min_heap.clear()
    min_heap.insert([1, 1, 0])
    assert min_heap.extract_min() == 0
    assert min_heap.size == 2
    assert min_heap.extract_min() == 1
    assert min_heap.size == 1
    assert min_heap.extract_min() == 1
    assert min_heap.size == 0
    
    min_heap.clear()
    min_heap.insert([0, -1000, 1000])
    assert min_heap.extract_min() == -1000
    assert min_heap.size == 2
    assert min_heap.extract_min() == 0
    assert min_heap.size == 1
    assert min_heap.extract_min() == 1000
    assert min_heap.size == 0
    
    min_heap.clear()
    min_heap.insert([0, -1000])
    assert min_heap.extract_min() == -1000
    assert min_heap.size == 1
    assert min_heap.extract_min() == 0
    assert min_heap.size == 0

def test_get_min():
    min_heap = MinHeap() 

    min_num = 1000
    for _ in range(1000):
        num = randint(-1000, 1000)
        min_heap.insert(num)
        if num < min_num:
            min_num = num
    assert min_heap.get_min() == min_num, f"Expected {min_num}, got {min_heap.get_min()}"
    
    min_heap.clear()
    min_heap.insert([0, 1, 2])
    assert min_heap.get_min() == 0
    
    min_heap.clear()
    min_heap.insert([2, 1, 0])
    assert min_heap.get_min() == 0
    
    min_heap.clear()
    min_heap.insert([1, 1, 0])
    assert min_heap.get_min() == 0
    
    min_heap.clear()
    min_heap.insert([0, -1000, 1000])
    assert min_heap.get_min() == -1000
    
    min_heap.clear()
    min_heap.insert([0, -1000])
    assert min_heap.get_min() == -1000

def test_clear():
    min_heap = MinHeap([1, 2, 3])
    min_heap.clear() 
    
    assert min_heap.get_items_as_list() == []
    assert min_heap.get_items_as_list().__len__() == 0
    
    min_heap.clear()
    assert min_heap.get_items_as_list() == []
    assert min_heap.get_items_as_list().__len__() == 0
   
def test_get_items_as_list():
    min_heap = MinHeap()
    assert min_heap.get_items_as_list() == []
    
    min_heap.insert([1, 1, 1])
    assert min_heap.get_items_as_list() == [1, 1, 1]
    
    min_heap.insert(1)
    assert min_heap.get_items_as_list() == [1, 1, 1, 1]