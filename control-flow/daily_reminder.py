# Prompt for task input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process using match-case for priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task. Try to complete it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that needs to be done today.")
        else:
            print(f"Reminder: {task} is a medium priority task. Schedule time for it soon.")
    
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task, but it is time-bound. Don’t delay too much.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
