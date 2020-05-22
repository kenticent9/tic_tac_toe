import random
import timeit

from binary_search_tree.linkedbst import LinkedBST

with open('words.txt') as f:
    words = random.sample(f.read().splitlines(), 900)
random_words = [random.choice(words) for _ in range(10000)]
sorted_tree = LinkedBST(sorted(words))
tree = LinkedBST(words)
balanced_tree = LinkedBST(words)
balanced_tree.rebalance()


def search_list():
    for random_word in random_words:
        words.index(random_word)


def search_tree_sorted():
    for random_word in random_words:
        sorted_tree.find(random_word)


def search_tree():
    for random_word in random_words:
        tree.find(random_word)


def search_tree_balanced():
    for random_word in random_words:
        balanced_tree.find(random_word)


print("List:", timeit.timeit(search_list, number=10))
print("Sorted tree:", timeit.timeit(search_tree_sorted, number=10))
print("Tree:", timeit.timeit(search_tree, number=10))
print("Balanced tree:", timeit.timeit(search_tree_balanced, number=10))
