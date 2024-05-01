# /*__________________ MD ASADUZZAMAN SHUVO ______________________ */


def initialize():
    return [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]

def calculate_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] > state[j]:
                cost += 1
    return cost

def generate_neighbors(current_state):
    neighbors = []
    for i in range(len(current_state)):
        for j in range(i+1, len(current_state)):
            new_state = current_state.copy()
            new_state.insert(i, new_state.pop(j))
            neighbors.append(new_state)
    return neighbors

def state_generation(current_state):
    while True:
        current_state_cost = calculate_cost(current_state)
        print(current_state, current_state_cost)
        
        min_next_cost = float('inf')
        min_next_state = None
        
        for neighbor in generate_neighbors(current_state):
            next_state = neighbor
            next_state_cost = calculate_cost(next_state)
            
            if next_state_cost < min_next_cost:
                min_next_cost = next_state_cost
                min_next_state = next_state
        
        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print("Final State:", current_state, current_state_cost)
            break

def main():
    state = initialize()
    state_generation(state)

main()
