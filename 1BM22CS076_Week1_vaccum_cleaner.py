def vacuum_world():
    # Initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # User input for vacuum's location and room status
    location_input = input("Enter Location of Vacuum (A/B): ")
    status_input = input("Enter status of " + location_input + " (0 for clean, 1 for dirty): ")
    status_input_complement = input("Enter status of the other room (0 for clean, 1 for dirty): ")

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        # Vacuum is placed in Location A
        print("Vacuum is placed in Location A")

        if status_input == '1':
            print("Location A is Dirty.")
            # Clean the dirt in A
            goal_state['A'] = '0'
            cost += 1
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

        if status_input_complement == '1':
            # If B is Dirty
            print("Location B is Dirty.")
            print("Moving RIGHT to Location B.")
            cost += 1  # cost for moving right
            print("Cost for moving RIGHT: " + str(cost))
            # Clean the dirt in B
            goal_state['B'] = '0'
            cost += 1
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean. No action required.")
    else:
        # Vacuum is placed in Location B
        print("Vacuum is placed in Location B")

        if status_input == '1':
            print("Location B is Dirty.")
            # Clean the dirt in B
            goal_state['B'] = '0'
            cost += 1
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

        if status_input_complement == '1':
            # If A is Dirty
            print("Location A is Dirty.")
            print("Moving LEFT to Location A.")
            cost += 1  # cost for moving left
            print("Cost for moving LEFT: " + str(cost))
            # Clean the dirt in A
            goal_state['A'] = '0'
            cost += 1
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean. No action required.")

    # Display final goal state and performance
    print("GOAL STATE: " + str(goal_state))
    print("Performance Measurement: " + str(cost))

# Running the vacuum_world function
vacuum_world()
