# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space - where n is the number of nodes in the tree and 
# h is the height of the tree
def sumBsts(tree):
    return get_tree_info(tree).total_sum_of_bsts

def get_tree_info(tree):
    if tree is None:
        return TreeInfo(
            True,
            float("-inf"),
            float("inf"),
            0,
            0,
            0
        )
    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)

    satisfies_bst_prop = tree.value > left_tree_info.max_value and tree.value <= right_tree_info.min_value

    is_bst = satisfies_bst_prop and left_tree_info.is_bst and right_tree_info.is_bst

    max_value = max(tree.value, max(left_tree_info.max_value, right_tree_info.max_value))
    min_value = min(tree.value, min(left_tree_info.min_value, right_tree_info.min_value))

    bst_sum = 0
    bst_size = 0

    total_sum_of_bsts = left_tree_info.total_sum_of_bsts + right_tree_info.total_sum_of_bsts

    if is_bst:
        bst_sum = tree.value + left_tree_info.bst_sum + right_tree_info.bst_sum
        bst_size = 1 + left_tree_info.bst_size + right_tree_info.bst_size

        if bst_size >= 3:
            total_sum_of_bsts = bst_sum

    return TreeInfo(
        is_bst,
        max_value,
        min_value,
        bst_size,
        bst_sum,
        total_sum_of_bsts,
    )

class TreeInfo:
    def __init__(self, is_bst, max_value, min_value, bst_size, bst_sum, total_sum_of_bsts):
        self.is_bst = is_bst
        self.max_value = max_value
        self.min_value = min_value
        self.bst_size = bst_size
        self.bst_sum = bst_sum
        self.total_sum_of_bsts = total_sum_of_bsts
