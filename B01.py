def max_shops(S, E, K):
    # Combine the start and end times into a list of tuples
    activities = list(zip(S, E))
    
    # Sort the activities by their end times
    activities.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of selected shops and end time of last selected shop
    selected_shops = 0
    last_end_time = -1
    
    # Iterate through the sorted activities
    for activity in activities:
        start_time, end_time = activity
        
        # If the start time of the current shop is greater than or equal to the end time of the last selected shop,
        # it means this shop can be visited by a person
        if start_time >= last_end_time:
            selected_shops += 1
            last_end_time = end_time
        
        # If the number of selected shops reaches K, break the loop
        if selected_shops == K:
            break
    
    return selected_shops

# Example usage
S = [1, 8, 3, 2, 6]
E = [5, 10, 6, 5, 9]
K = 2

result = max_shops(S, E, K)
print(result)  # Output: 4
