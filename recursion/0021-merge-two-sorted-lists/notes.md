# 21. Merge Two Sorted Lists

## Problem Statement

[LeetCode Link](https://leetcode.com/problems/merge-two-sorted-lists/)

You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

## Approach

**Recursion:**
- Base Cases: If `list1` is empty, return `list2`. If `list2` is empty, return `list1`.
- Recursive Step: Compare the values of the current nodes in `list1` and `list2`. The smaller node becomes the head, and its `next` pointer points to the result of recursively merging the rest of its list with the other list.

## Complexity
- **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `list1` and `list2`. Each recursive call processes one node.
- **Space Complexity:** $O(n + m)$ due to the recursion stack.
