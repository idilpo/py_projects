class Tree:

    def __init__(self, value, *children):
        self.value = value
        self.children = children

def longest_path(tree):

    def longest_path_rec(current, parent_value=0, parent_path_length=0):
        if (current.value == parent_value + 1):
            current_path_length = parent_path_length + 1
        else:
            current_path_length = 1
        max_length = current_path_length

        for child in current.children:
            max_child_length = longest_path_rec(child, current.value, current_path_length)
            max_length = max(max_length, max_child_length)
        return max_length

    return longest_path_rec(tree)


