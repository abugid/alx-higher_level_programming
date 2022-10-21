#!/usr/bin/python3
import sys
"""
this is a program to solve the n-queen problem
"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n_size = int(sys.argv[1])


class Tree:
    """
        class for constructing a state space tree
    """

    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)


root = Tree()
solution = []

for i in range(n_size):
    cur_node = Tree(i, root)
    start_data = node_depth = 0
    while (cur_node is not root):
        for j in range(start_data, n_size):
            tmp_node = Tree(j, cur_node)
            while (tmp_node != root):
                if j == tmp_node.parent.data:
                    break
                tmp_node = tmp_node.parent
            else:
                tmp_node = cur_node
                num_depth = 1
                while (tmp_node is not root):
                    if j == tmp_node.data - num_depth or\
                         j == tmp_node.data + num_depth:
                        break
                    num_depth += 1
                    tmp_node = tmp_node.parent
                else:
                    tmp_node = Tree(j, cur_node)
                    cur_node = tmp_node
                    start_data = 0
                    node_depth += 1
                    break
        else:
            start_data = cur_node.data + 1
            cur_node = cur_node.parent
            node_depth -= 1

        if node_depth == n_size - 1:
            cur_sol = []
            tmp_node = cur_node
            while (tmp_node is not root):
                cur_sol.append(tmp_node.data)
                tmp_node = tmp_node.parent
            solution.append(cur_sol)
            start_data = cur_node.data + 1
            cur_node = cur_node.parent
            node_depth -= 1

solution.reverse()
new_sol = [[[idx, j] for idx, j in enumerate(i)] for i in solution]
for i in new_sol:
    print(i)
