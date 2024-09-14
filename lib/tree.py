from collections import deque

class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, element_id):
        return self._bfs(self.root, element_id)

    def _bfs(self, node, element_id):
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current['id'] == element_id:
                return current
            queue.extend(current['children'])
        return None
