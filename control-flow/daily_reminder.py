task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        p= " is high task"
    case "medium":
        p= "is the medium task"
    case "low":
        p="is the low task." 
if time_bound == "yes":
    print(f"Reminder: '{task}' {p} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: '{task}' {p} Consider completing it when you have free time.")
