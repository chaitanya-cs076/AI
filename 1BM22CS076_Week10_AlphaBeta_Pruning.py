# Function to evaluate a leaf node (example heuristic function)
def evaluate(node):
    return node  # For leaf nodes, the value itself is returned

# Alpha-Beta Pruning Function
def alphaBeta(node, depth, alpha, beta, isMaximizer, path=[]):
    # Base case: if we reach a leaf node or maximum depth
    if depth == 0 or not isinstance(node, list):
        print(f"Leaf Node {node} -> Returning: {evaluate(node)}")
        return evaluate(node)

    if isMaximizer:
        value = float('-inf')  # Initialize value to negative infinity
        print(f"Maximizer at Node {path}, Alpha: {alpha}, Beta: {beta}")
        for i, child in enumerate(node):  # Traverse all children
            value = max(value, alphaBeta(child, depth - 1, alpha, beta, False, path + [i]))
            alpha = max(alpha, value)  # Update alpha
            print(f"Maximizer Updated Alpha: {alpha} at Node {path + [i]}")
            if alpha >= beta:  # Pruning condition
                print(f"Pruning at Node {path + [i]} (Alpha: {alpha} >= Beta: {beta})")
                break  # Prune remaining branches
        return value
    else:
        value = float('inf')  # Initialize value to positive infinity
        print(f"Minimizer at Node {path}, Alpha: {alpha}, Beta: {beta}")
        for i, child in enumerate(node):  # Traverse all children
            value = min(value, alphaBeta(child, depth - 1, alpha, beta, True, path + [i]))
            beta = min(beta, value)  # Update beta
            print(f"Minimizer Updated Beta: {beta} at Node {path + [i]}")
            if alpha >= beta:  # Pruning condition
                print(f"Pruning at Node {path + [i]} (Alpha: {alpha} >= Beta: {beta})")
                break  # Prune remaining branches
        return value

# Function to build a tree from user input
def buildTree(depth, leaf_nodes):
    current_level = leaf_nodes  # Start with the leaf nodes
    while depth > 0:
        # Pair consecutive nodes to create the parent level
        next_level = [current_level[i:i + 2] for i in range(0, len(current_level), 2)]
        current_level = next_level
        depth -= 1
    return current_level[0]  # Root node of the tree

# Main Program
print("Enter the depth of the tree:")
depth = int(input())  # User input for the depth of the tree

print("Enter the leaf node values, separated by spaces:")
leaf_nodes = list(map(int, input().split()))  # User input for all leaf nodes

# Ensure the number of leaf nodes is 2^depth
expected_leaf_count = 2 ** depth
if len(leaf_nodes) != expected_leaf_count:
    print(f"Error: Expected {expected_leaf_count} leaf nodes, but got {len(leaf_nodes)}.")
    exit(1)

# Build the tree from the input
tree = buildTree(depth, leaf_nodes)

# Display the constructed tree for reference
print("\nConstructed Tree:")
print(tree)

# Alpha-Beta Pruning
alpha = float('-inf')
beta = float('inf')
print("\nStarting Alpha-Beta Pruning...")
best_value = alphaBeta(tree, depth, alpha, beta, True)
print("\nBest Value for Root Node:", best_value)
