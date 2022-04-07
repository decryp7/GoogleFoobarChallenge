"""
Elevator Maintenance
====================

You've been assigned the onerous task of elevator maintenance -- ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on.

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
Output:
    0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

Input:
solution.solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
Output:
    1.0,1.0.2,1.0.12,1.1.2,1.3.3

-- Java cases --
Input:
Solution.solution({"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"})
Output:
    0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

Input:
Solution.solution({"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"})
Output:
    1.0,1.0.2,1.0.12,1.1.2,1.3.3

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

def solution(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        solution(left)
        solution(right)

        i = 0  # index for left
        j = 0  # index for right
        k = 0  # index for main

        while i < len(left) and j < len(right):
            # print('Comparing ' + left[i] + ' and ' + right[j])
            left_version_spilt = left[i].split('.')
            right_version_spilt = right[j].split('.')

            # fill up version
            # left_version_spilt = left_version_spilt + ['0'] * (3 - len(left_version_spilt))
            # right_version_spilt = right_version_spilt + ['0'] * (3 - len(right_version_spilt))

            for version_number in range(0, 3):
                # print(left_version_spilt[version_number] + ' ' + right_version_spilt[version_number])
                if int(left_version_spilt[version_number]) == int(right_version_spilt[version_number]):
                    # if there are more version numbers to compare
                    if len(left_version_spilt) > version_number + 1 and len(right_version_spilt) > version_number + 1:
                        continue
                    else:
                        # compare length of version number
                        if len(left_version_spilt) < len(right_version_spilt):
                            l[k] = left[i]
                            i += 1
                            break
                        else:
                            l[k] = right[j]
                            j += 1
                            break
                elif int(left_version_spilt[version_number]) < int(right_version_spilt[version_number]):
                    l[k] = left[i]
                    i += 1
                    break
                elif int(left_version_spilt[version_number]) > int(right_version_spilt[version_number]):
                    l[k] = right[j]
                    j += 1
                    break
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1

    return l

if __name__ == '__main__':
    print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
    print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))