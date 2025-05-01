def move(block, from_stack, to_stack, state):
    state[to_stack].append(state[from_stack].pop())

def goal_state(state, goal):
    return all(state[stack] == goal[stack] for stack in state)

def blocks_world(state, goal):
    actions = []
    while not goal_state(state, goal):
        for i, stack in state.items():
            for block in stack:
                if block != goal[i][-1]:
                    move(block, i, goal[block][-1], state)
                    actions.append(f"Move {block} to {goal[block][-1]}")
                    break
    return actions

# Example usage:
state = {'A': ['B'], 'B': ['C'], 'C': []}  # Initial state
goal = {'A': ['C'], 'B': [], 'C': ['B']}  # Goal state
print(blocks_world(state, goal))  # Output the sequence of actions
