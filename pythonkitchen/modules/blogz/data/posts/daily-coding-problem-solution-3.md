title: Daily Coding Problem Solution 3
slug: daily-coding-problem-solution-3
pub: Mon, 22 Mar 2021 19:48:55 +0000
authors: Abdur-RahmaanJ

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class


```python
class Node: 
    def __init__(self, val, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right 

```


The following test should pass:


```python
node = Node('root', Node('left', Node('left.left')), Node('right')) 
assert deserialize(serialize(node)).left.left.val == 'left.left'

```



---


### 2 Internet Solutions



```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        cur = root
        stk = []
        res = []

        while cur or stk:
            if cur:
                res.append(str(cur.val))
                stk.append(cur)
                cur = cur.left
            else:
                res.append("#")
                cur = stk.pop()
                cur = cur.right
        else:
            res.append("#")

        return " ".join(res)  

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        strings = data.split(" ")        

        root = Node(strings[0])
        cur = root
        stk = []

        for string in strings[1:]:
            node = None
            if string == "#":
                node = None
            else:
                node = Node(string)

            if cur:
                cur.left = node
                stk.append(cur)
                cur = cur.left
            else:
                cur = stk.pop()
                cur.right = node
                cur = cur.right

        return root


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = []

        queue = deque([root])

        while queue:
            tmp = deque()

            while queue:
                node = queue.popleft()
                if not node:
                    output.append('#')
                else:
                    output.append(str(node.val))
                    tmp.append(node.left)
                    tmp.append(node.right)

            queue = tmp

        return ' '.join(output) if output[0] != '#' else ''


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        data = data.split(' ')

        root = Node(data[0])
        i = 1

        queue = deque([root])

        while i < len(data):
            tmp = deque()

            while queue:
                node = queue.popleft()

                if data[i] == '#':
                    node.left = None
                else:
                    node.left = Node(data[i])
                    tmp.append(node.left)

                i += 1

                if data[i] == '#':
                    node.right = None
                else:
                    node.right = Node(data[i])
                    tmp.append(node.right)

                i += 1

            queue = tmp

        return root

y = Codec()
y2 = Codec2()
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert y.deserialize(y.serialize(node)).left.left.val == 'left.left'
assert y2.deserialize(y2.serialize(node)).left.left.val == 'left.left'
assert 

```

