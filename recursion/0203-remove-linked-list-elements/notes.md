# 203. Remove Linked List Elements

## Problem Statement

[LeetCode Link](https://leetcode.com/problems/remove-linked-list-elements/)

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

## Approach

**Recursion:**
- Base Case: If `head` is empty (`None`), return `None`.
- Recursive Step: Recursively call `removeElements` on the `next` node (`head.next`). Then, check if the current node's value equals `val`. If it does, return `head.next` (which skips the current node). Otherwise, return `head`.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. We visit each node exactly once.
- **Space Complexity:** $O(n)$ due to the recursion stack.
