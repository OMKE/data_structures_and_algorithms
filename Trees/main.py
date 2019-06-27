


from LinkedBinaryTree import LinkedBinaryTree
from BinarySearchTree import BinarySearchTree




tree = LinkedBinaryTree()
print("Tree ->", tree)
rp = tree.add_root("*")
print("RP container ", rp.container)
rlp = tree.add_left(rp, "+")
rrp = tree.add_right(rp, "-")
tree.add_left(rlp, "a")
tree.add_right(rlp, "b")
tree.add_left(rrp, "c")
tree.add_right(rrp, "d")



btree = BinarySearchTree()


rp = btree.add_root(1)

rlp = btree.add_left(rp, 2)
rrp = btree.add_right(rp, 3)

rllp = btree.add_left(rlp, 4)
rlrp = btree.add_right(rlp, 5)

rrlp = btree.add_left(rrp, 6)
rrrp = btree.add_right(rrp, 7)

rlllp = btree.add_left(rllp, 8)
rllrp = btree.add_right(rllp, 9)

for p in btree:
    print(p, end=" ")


bstree = BinarySearchTree()
bstree.insert_element(5)
bstree.insert_element(3)
bstree.insert_element(37)
bstree.insert_element(8)
bstree.insert_element(9)
bstree.insert_element(4)
bstree.insert_element(12)
bstree.insert_element(17)
bstree.insert_element(21)
bstree.insert_element(52)

print("\n")
for p in bstree:
    print(p, end=" ")

print("\n")

arg = 12
result = bstree.binary_search(arg, bstree.get_root())
if result is None:
    print("Element {} is not found in container".format(arg))
else:
    print("Element {} is found in container".format(arg))



print("\nBreath first")
for p in bstree.breadth_first():
    print(p.get_element(), end=" ")

print("\nDepth first")
for p in bstree.depth_first():
    print(p.get_element(), end=" ")



