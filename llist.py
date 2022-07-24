from node import Node


def insert_begin(head, item):
    """Insert an item to the beginning of the list."""
    return Node(item, head)


def insert_end(head, item):
    """Insert an item to the end of the list."""
    if not head:
        return Node(item)
    head.link = insert_end(head.link, item)
    return head


def insert_at(head, item, index):
    """Insert an item before the position (index) in the list."""
    if not head:
        return Node(item)
    elif index == 0:
        return Node(item, head)
    head.link = insert_at(head.link, item, index - 1)
    return head


def insert_in_sorted(head, item):
    """Insert an item in sorted list at appropriate position maintaining its monotonicity."""
    if not head:
        return Node(item)
    elif head.val > item:
        return Node(item, head)
    head.link = insert_in_sorted(head.link, item)
    return head


def remove_begin(head):
    """Remove an item present at the beginning of the list."""
    if not head:
        return
    return head.link


def remove_end(head):
    """Remove an item present at the end of the list."""
    if not head:
        return
    elif not head.link:
        return
    head.link = remove_end(head.link)
    return head


def remove_at(head, index):
    """Remove an item present at the position (index) in the list."""
    if not head:
        return
    elif index == 0:
        return head.link
    head.link = remove_at(head.link, index - 1)
    return head


def remove_first_occurance(head, item):
    """Remove first occurance of item from the list."""
    if not head:
        return
    elif head.val == item:
        return head.link
    head.link = remove_first_occurance(head.link, item)
    return head


def remove_last_occurance(head, item):
    """Remove last occurance of item from the list."""
    if not head:
        return

    curr = head
    prev_to_curr = None
    this = prev = None

    while curr:
        if curr.val == item:
            prev = prev_to_curr
            this = curr
        prev_to_curr = curr
        curr = curr.link

    if this:
        if prev:
            prev.link = this.link
            return head
        else:
            return this.link


def remove_all_occurance(head, item):
    """Remove all occurance of item(s) from the list."""
    if not head:
        return
    elif head.val == item:
        return remove_all_occurance(head.link, item)
    head.link = remove_all_occurance(head.link, item)
    return head


def reverse(head):
    """Reverse the current order of items."""
    if not head:
        return
    elif not head.link:
        return head
    last = reverse(head.link)
    head.link.link = head
    head.link = None
    return last


def begin(head, n):
    """Return the nth node from beginning."""
    if not head:
        return
    elif n == 0:
        return head
    return begin(head.link, n - 1)


def end(head, n):
    """Return the nth node from end."""
    this = head
    while n >= 0:
        if not head:
            return
        head = head.link
        n -= 1

    while head:
        this = this.link
        head = head.link

    return this


def middle(head):
    """Return the middle node in the list. If length is even then returns floor(n / 2)."""
    lo = hi = head
    while hi and hi.link:
        lo = lo.link
        hi = hi.link.link

    return lo


def count(head, item):
    """Count the frequency of occurance of item in the list."""
    if not head:
        return 0
    elif head.val == item:
        return 1 + count(head.link, item)
    return count(head.link, item)


def contains(head, item):
    """Return True when item present in the list, False otherwise."""
    if not head:
        return False
    elif head.val == item:
        return True
    return contains(head.link, item)


def index(head, item):
    """Return the index of an item present in the list. Raises IndexError if not present."""
    i = 0
    while head:
        if head.val == item:
            return i
        i += 1
        head = head.link
    raise IndexError


def display(head):
    """Print a list item to the console."""
    if not head:
        print()
        return
    print(head.val, end=' ')
    display(head.link)


def rdisplay(head):
    """Print a list items to the console in reverse order."""
    if not head:
        return
    rdisplay(head.link)
    print(head.val, end=' ')


def length(head):
    """Return the length (number of items) of the list."""
    if not head:
        return 0
    return 1 + length(head.link)


def split_in_middle(head):
    """Split the list in two equal half. If the length is odd, then second list should have one extra node."""
    lo = hi = head
    prev = None
    while hi and hi.link:
        prev = lo
        lo = lo.link
        hi = hi.link.link

    if prev:
        prev.link = None

    return head, lo


def is_palindrome(head):
    """Return True if list is palindrome, False otherwise."""
    if not head:
        return
    first, second = split_in_middle(head)
    second = reverse(second)
    while first and second:
        if first.val != second.val:
            return False
        first = first.link
        second = second.link
    return True


def segregate_evens(head):
    """Move all even number to the beginning of the list."""
    evens = odds = None
    last_even = last_odd = None

    while head:
        if head.val % 2 == 0:
            if not evens:
                evens = last_even = head
            else:
                last_even.link = head
                last_even = last_even.link
        else:
            if not odds:
                odds = last_odd = head
            else:
                last_odd.link = head
                last_odd = last_odd.link
        head = head.link

    if last_odd:
        last_odd.link = None

    if last_even:
        last_even.link = odds
        return evens
    else:
        return odds


def merge_two_sorted(headA, headB):
    """Merge two sorted list together into single sorted list."""
    if not headA:
        return headB
    elif not headB:
        return headA

    if headA.val < headB.val:
        headA.link = merge_two_sorted(headA.link, headB)
        return headA
    else:
        headB.link = merge_two_sorted(headA, headB.link)
        return headB


def intersection_node(headA, headB):
    """Return the insertion node to two list."""
    short, long = headA, headB
    lenA = length(headA)
    lenB = length(headB)
    if lenA > lenB:
        short, long = headB, headA

    diff = abs(lenA - lenB)

    while diff:
        long = long.link
        diff -= 1

    while short and long:
        if short == long:
            return short
        short = short.link
        long = long.link


def pairwise_swap(head):
    """Pair wise swap the items of the list."""
    if not head:
        return
    elif not head.link:
        return head
    first = head
    second = head.link
    rest = second.link
    second.link = first
    first.link = pairwise_swap(rest)
    return second


def remove_duplicates_from_sorted(head):
    if not head:
        return
    elif not head.link:
        return head
    next_node = remove_duplicates_from_sorted(head.link)
    if head.val == next_node.val:
        head.link = next_node.link
    else:
        head.link = next_node
    return head


def merge_sort(head):
    """Return the sorted list in ascending order using merge sort algorithm."""
    if not head:
        return
    elif not head.link:
        return head

    first, second = split_in_middle(head)
    first = merge_sort(first)
    second = merge_sort(second)
    head = merge_two_sorted(first, second)
    return head


def has_cycle(head):
    """Return True when list has cycle in it, False otherwise."""
    if not head:
        return
    fast = slow = head
    while fast and fast.link:
        slow = slow.link
        fast = fast.link.link

        if slow == fast:
            return slow  # True if slow else False
    return False


def cycle_begins_at(head):
    """Return the beginning node of the cycled list (list that has cycle in it)."""
    if not head:
        return
    one = has_cycle(head)
    if one:
        two = head
        while one != two:
            one = one.link
            two = two.link
        return one


def cycle_length(head):
    """Return the length of the cycle in the list."""
    if not head:
        return
    cnt = 0
    node = has_cycle(head)
    if node:
        curr = node.link
        cnt += 1
        while curr != node:
            curr = curr.link
            cnt += 1
    return cnt


def genlist(iterable):
    """Generate and return the list from an iterable."""
    llist = None
    for item in reversed(iterable):
        llist = insert_begin(llist, item)
    return llist
