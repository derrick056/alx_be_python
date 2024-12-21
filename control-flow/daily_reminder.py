# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-sensitive
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using Match Case for priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task. Please focus on completing it as soon as possible."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task. It’s important to complete it within a reasonable time frame."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please restart the program."

# Modify the reminder for time-sensitive tasks
if time_bound == "yes" and "Reminder:" in reminder:
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)
