
def Node(value):
    value = value;
    left = None
    right = None

def bfs(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

root = Node(1)
bfs(root)
