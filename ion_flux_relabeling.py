"""
Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired spectacularly. The Commander had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. Commander Lambda is having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

   7
 3   6
1 2 4 5

Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(5, {19, 14, 28})
Output:
    21,15,29

Input:
Solution.solution(3, {7, 3, 5, 1})
Output:
    -1,7,6,3

-- Python cases --
Input:
solution.solution(3, [7, 3, 5, 1])
Output:
    -1,7,6,3

Input:
solution.solution(5, [19, 14, 28])
Output:
    21,15,29

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


def find_top(h, p):
    max_nodes = 2 ** h - 1

    if p >= max_nodes:
        return -1

    left_most_nodes = [max_nodes]
    value = max_nodes
    while value > 1:
        value = (value - 1) / 2
        left_most_nodes.append(int(value))
    left_most_nodes.sort()
    # print(left_most_nodes)

    right_most_nodes = []
    for i in range(0, h):
        right_most_nodes.append(max_nodes - i)
    right_most_nodes.sort()
    # print(right_most_nodes)

    if p in left_most_nodes:
        index = left_most_nodes.index(p)
        return left_most_nodes[index + 1]

    if p in right_most_nodes:
        index = right_most_nodes.index(p)
        return right_most_nodes[index + 1]

    # if we cannot find it in the left-most and right-most nodes
    # we should draw the tree and check one by one
    levels = []
    for i in range(0, h):
        levels.append([])

    # post-transversal (left -> right -> root)
    # start from bottom
    current_level = h - 1
    while value <= max_nodes:
        levels[current_level].append(int(value))
        value += 1
        # after inserting the value check where to insert the next value
        continue_up = True
        while continue_up:
            # check current level for p
            try:
                index_of_p = levels[current_level].index(p)
                if current_level-1 < 0:
                    return - 1
                # check if the parent already reach the expected number of nodes
                # round up so that we can get the correct number since the node can be the left node
                # for e.g. 1 node -> we expect 1 node on the parent level but 1/2 = 0.5
                expected_parent_level_nodes = int((index_of_p+1) / 2) + ((index_of_p+1) % 2 > 0)
                if expected_parent_level_nodes == len(levels[current_level-1]):
                    return levels[current_level-1][len(levels[current_level-1])-1]
            except ValueError:
                # print("Cannot find " + str(p) + " at " + str(levels[current_level]))
                pass
            # print(str(current_level) + ' ' + str(levels[current_level]))
            expected_parent_level_nodes = int(len(levels[current_level]) / 2)
            # if hit the top, reset current level to bottom
            if current_level == 0:
                current_level = h - 1
                continue_up = False
                continue
            # if the number of parent node does not correspond the child nodes (1 parent to 2 child (left & right)
            # set current level to the level of the parent node to insert the node
            elif expected_parent_level_nodes != len(levels[current_level-1]):
                current_level -= 1
                continue_up = False
                continue
            # continue to move up the mountain
            else:
                current_level -= 1

        # print('Add next node at ' + str(current_level))
        # print('-------------------------------')

    # for level in levels:
    #     print(level)


def solution(h, q):
    results = []
    for i in q:
        results.append(find_top(h, i))
    return results


if __name__ == '__main__':
    # print(solution(3, [2]))
    # print(solution(5, [19]))
    print(solution(3, [7, 3, 5, 1]))
    print(solution(5, [19, 14, 28]))
