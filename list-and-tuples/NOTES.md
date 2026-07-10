- mutable - assign new value , delete (individual or as a slice, append items , prepending items with iterables)
- dynamic
- can next
- ordered
- indexed starting from 0
- accessed by index position
- can be accessed in reverse - by negative index
- can use built-in functions (max, min , len, del)
- slicing with strides
- List methods (modify the target list in place and returns nothing as against string that creates a new object and returns it without modifying the target object !)
- list methods
    - append(<obj>) is different from concatenation.
    - extend(<iterable>)
    - insert(int,<obj>) 
    - remove(<obj>) - removes first occurance
    - clear() - emptys the list
    - sort(<key=None>, <reverse= False>) - key can be a function to apply - default is ascending - if list is mixed , the sort will not work
    - reverse() - same as a[::-1]
- list mothods that return values 
    - pop(<index=-1>) - default is last item and returns the removed value.
    - index(<obj>,start,stop]) - search withing the list with optional start and stop range to search in 
    - count(<obj>)
    - copy() - shallow copy - values are the same but objects are different, nested lists are references to original so be careful when changing 


# Tuples
- cousin of List
- immutable 
- better performance compared to list
- use when you want immutable collections 
- can do teh same things liek slicing , reversing , accessing by index etc like lists
- comma separated values without round brackets is a tuple 
- can pack and unpack tuples

The common practice is to use lists for homogeneous objects and tuples for heterogeneous objects. Lists are typically used when all elements are of the same type, while tuples are used when elements are of different types.

Lists don’t have a fixed length and are mutable, so they’re appropriate for storing homogeneous objects. In contrast, tuples have a fixed length and are immutable, so the position of objects in a tuple can have meaning, supporting heterogeneous data.