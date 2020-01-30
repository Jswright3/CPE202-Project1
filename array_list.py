"""
LAB2
CPE 202
John Wright
"""

class ArrayList:
    """Array List
    Attributes:
        capacity (int): the capacity of the list
        num_items (int): the number of items in the list
        arr (list): a python list construct which stores items
    """
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.num_items = 0
        self.arr = self.capacity * [None]

    def __eq__(self, other):
        if self.arr == self.arr:
            return True
        return False

    def __repr__(self):
        pass

def enlarge(lst):
    """double the original capacity of an array list
    Args:
        lst (ArrayList): an array list object
    Returns:
        ArrayList: an array list with double the original capacity
    """
    oldcapacity = lst.capacity
    lst.capacity *= 2
    lst.arr += [None] * oldcapacity
    return lst

def shrink(lst):
    """shrink an array list by halving the original capacity.
    Args:
        lst (ArrayList): an array list object
    Returns:
        ArrayList: an array list with half the original capacity
    """
    lst.capacity /= 2
    return lst

def insert(lst, val, idx):
    """takes an object of ArrayList lst, a integer val, and an integer idx,
    and insert the integer val to the arr of the ArrayList object at the index
    indicated by the integer idx, and returns the ArrayList object.
    The function shall enlarge the ArrayList by calling the enlarge
    function when the ArrayList is full (num_items == capacity).
    Args:
        lst (ArrayList): an array list object
        val (int): a integer value
        idx (int): the index at which the val will be inserted
    Returns:
        ArrayList: an array list with the val inserted at the idx
    """
    if lst.num_items == lst.capacity:
        lst = enlarge(lst)
    for i in range(lst.capacity - 1, idx, -1):
        lst.arr[i] = lst.arr[i - 1]
    lst.arr[idx] = val
    lst.num_items += 1
    return lst

def get(lst, idx):
    """get an item stored at the index indicated by the integer idx
    Args:
        lst (ArrayList): an array list object
        idx (int): the index at which the val will be inserted
    Returns:
        int: an integer value stored at the idx in the lst
    Raises:
        IndexError if the index is out of bound ( >= num_items).
    """
    if 0 <= idx < lst.num_items:
        return lst.arr[idx]
    raise IndexError('Index Out of Range')

def contains(lst, val):
    """searches for the value in the list, and returns True if the value is found or False if not.
    Args:
        lst (ArrayList): an array list object
        val (int): a integer value
    Returns:
        bool: True if the value exists in the list, False otherwise.
    """
    if val in lst.arr:
        return True
    return False

def search(lst, val):
    """Searches for val in an array list.
    Args:
        lst (ArrayList): an array list object
        val (int): a value to search for
    Returns:
        int: the index where the integer is stored in the lst
             It returns None if the integer is not found.
    """
    if val in lst.arr:
        for i in enumerate(lst.arr):
            if i[1] == val:
                return i[0]
    return None

def remove(lst, val):
    """removes the first occurence of the val from the lst by
    shifting items on the right by one to the left.
    If the item to be removed is the last item in the ArrayList (index == num_items - 1),
    simply decrement the value of num_items by 1 (num_items -= 1).
    The function shall shrink the ArrayList by calling the shrink function
    when the ArrayList is a quarter full (4 * num_items <= capacity), and the capacity is
    greater than 2 (capacity > 2).
    Args:
        lst (ArrayList): an array list object
        val (int): the value to be removed
    Returns:
        ArrayList: an array list with the val removed
    """
    idx = 0
    target = 0
    for i in lst.arr:
        if i == val:
            target = idx
        idx += 1
    if lst.num_items * 4 == lst.capacity and lst.capacity > 2:
        lst = shrink(lst)
    last = lst.capacity - 1
    for i in range(target, last):
        lst.arr[i] = lst.arr[i + 1]
    lst.arr[last] = None
    lst.num_items -= 1
    return lst

def pop(lst, idx):
    """removes the val from the lst by shifting items on the right by one to the left.
    If the item to be removed is the last item in the ArrayList (index == num_items - 1),
    simply decrement the value of num_items by 1 (num_items -= 1).
    The function shall shrink the ArrayList by calling the shrink function
    when the ArrayList is a quarter full (4 * num_items <= capacity), and the capacity is
    greater than 2 (capacity > 2).
    Args:
        lst (ArrayList): an array list object
        idx (int): the index at which the val will be inserted
    Returns:
        ArrayList: an array list with the val removed
        int: the removed value at the index
    Raises:
        IndexError: if idx is out of range.
    """
    if idx >= lst.num_items:
        raise IndexError('Index Out of Range')
    val = lst.arr[idx]
    if idx == lst.num_items - 1:
        lst.num_items -= 1
        return lst, lst.arr[idx]
    if lst.arr[idx] is not None:
        if lst.num_items * 4 == lst.capacity and lst.capacity > 2:
            lst = shrink(lst)
        last = lst.capacity - 1
        for i in range(idx, last):
            lst.arr[i] = lst.arr[i + 1]
        lst.arr[last] = None
        lst.num_items -= 1
    return lst, val

def size(lst):
    """returns the number of items stored in the ArrayList object (returns num_items).
    Args:
        lst (ArrayList): an array list object
    Returns:
        int: the number of items stored in the array list
    """
    return lst.num_items
