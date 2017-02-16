import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLinkList:
    def __init__(self):
        self.head = self.tail = None

    def dq_append(self, node):
        if self.tail:
            print 'dq: insert at end', node.data
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        else:
            print 'dq: first insert', node.data
            self.head = self.tail = node

    def delete(self, node):
        if self.head == node and self.head == self.tail:
            self.head = self.tail = None
            return

        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
            return

        if self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def __repr__(self):
        ptr = self.head
        result = list()
        while ptr:
            result.append(str(ptr.data))
            ptr = ptr.next

        return " ".join(result)

def find_digest(text, word_set):

    found = set()
    i = j = 0
    start = -1
    end = len(text)
    # go over all the strings in the array
    while i < len(text):
        # if string is in the search set
        word = text[i]
        print word
        if word in word_set:
            # found keyword, add it to found set and start exploring
            found.add(word)
            update_entry(word, i)
            j = max(j, i + 1)
            while j < len(text) and word_set-found:
                wd = text[j]
                print 'j- word', wd
                if wd in word_set - found:
                    found.add(wd)
                    update_entry(wd, j)
                    print word_set
                    print found
                j += 1

            # found all keywords
            if not word_set-found:
                if get_subarray_length() < end-start:
                    start = dq.head.data
                    end = dq.tail.data

        # Increment i pointer

        if text[i] in lookup:
            lookup.pop(text[i])
            found.remove(text[i])
            if dq.head:
                if dq.tail == dq.head:
                    dq.head = dq.tail = None
                else:
                    dq.head = dq.head.next
        i += 1

    if start > -1:
        return (start, end)
    else:
        return (None, None)

def update_entry(word, i):
    # if node representing the string already exists
    if word in lookup:
        print 'update entry: updating word location'
        # delete node from dict and dq
        node = lookup.pop(word)
        dq.delete(node)
        # add new node with updated index
        node = Node(i)
        lookup[word] = node
        dq.dq_append(node)
    # if node doesn't already exist
    else:
        print 'update entry: inserting word first time'
        node = Node(i)
        dq.dq_append(node)
        lookup[word] = node

def get_subarray_length():
    if dq.tail and dq.head:
        return dq.tail.data - dq.head.data
    else:
        return sys.maxint

lookup = dict()
dq = DLinkList()
input = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "cat", "dog"]
ans = find_digest(input, set(['banana', 'cat']))
print ans[0], ans[1]