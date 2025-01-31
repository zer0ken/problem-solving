import sys

N = int(sys.stdin.readline())

tree = {}

for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = [left, right]


def preorder(node):
    if node == '.':
        return
    sys.stdout.write(node)
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    sys.stdout.write(node)
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    sys.stdout.write(node)

preorder('A')
sys.stdout.write('\n')
inorder('A')
sys.stdout.write('\n')
postorder('A')
sys.stdout.write('\n')