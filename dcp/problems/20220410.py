"""This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute
path to a file within our file system. For example, in the second example
above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and
its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""
from collections import namedtuple

from dcp import harness


def build_fs(fs):
    """
    runtime: O(n^2)
    space: O(n)
    """
    # filesystem will be a tree
    tree = {}
    current_path = []
    for path in fs.split("\n"):
        # number of preceding tabs tells us depth
        depth = 0
        while "\t" in path:
            depth += 1
            path = path[1:]

        current_node = tree
        for subdir in current_path[:depth]:
            current_node = current_node[subdir]

        if "." in path:
            current_node[path] = True
        else:
            current_node[path] = {}

        current_path = current_path[:depth]
        current_path.append(path)

    return tree


def longest_path(root):
    """
    runtime: O(n)
    space: O(n)
    """
    paths = []
    for key, val in root.items():
        if val is True:
            paths.append(key)
        else:
            paths.append(key + "/" + longest_path(val))

    valid_paths = [p for p in paths if "." in p]
    if valid_paths:
        return max(valid_paths, key=len)
    return ""


if __name__ == "__main__":
    tc = namedtuple("TestCase", "fs expected")
    cases = (
        tc("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
        tc(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            32,
        ),
    )

    harness(cases, lambda t: len(longest_path(build_fs(t.fs))))
