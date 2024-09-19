Approach 1: Recursive Approach
The first method to solve this problem is using recursion. This is the classical method and is straightforward. We can define a helper function to implement recursion.

class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

Complexity Analysis

Time complexity: O(n)

The time complexity is O(n) because the recursive function is T(n)=2⋅T(n/2)+1.
Space complexity: O(n)

The worst case space required is O(n), and in the average case it's O(logn) where n is number of nodes.

--------------------------------------------------------------------------------------------------------------
Approach 2: Iterating method using Stack
The strategy is very similiar to the first method, the different is using stack.

class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

Complexity Analysis

Time complexity: O(n)

Space complexity: O(n)






