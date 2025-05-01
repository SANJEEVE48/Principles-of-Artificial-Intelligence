def minimax(node, depth, maximizing_player, evaluate, get_children):
    if depth == 0 or not get_children(node): return evaluate(node)
    
    if maximizing_player:
        return max(minimax(child, depth-1, False, evaluate, get_children) for child in get_children(node))
    else:
        return min(minimax(child, depth-1, True, evaluate, get_children) for child in get_children(node))

# Example usage
def evaluate(node): return node  # Simplified evaluation function
def get_children(node): return []  # Simplified children function for a leaf node

root = 0  # Example root node
depth = 3  # Example depth
is_maximizing_player = True  # Maximizing player starts
result = minimax(root, depth, is_maximizing_player, evaluate, get_children)
print(result)
