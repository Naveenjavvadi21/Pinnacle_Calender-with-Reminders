import calendar
from datetime import datetime

# Dictionary to store reminders
reminders = {}

# Display Calendar
def display_calendar():
    year = int(input("Enter Year: "))
    month = int(input("Enter Month (1-12): "))

    print("\n")
    print(calendar.month(year, month))

# Add Reminder
def add_reminder():
    date = input("Enter Date (YYYY-MM-DD): ")
    reminder = input("Enter Reminder: ")

    if date in reminders:
        reminders[date].append(reminder)
    else:
        reminders[date] = [reminder]

    print("Reminder Added Successfully!")

# View Reminders
def view_reminders():
    if not reminders:
        print("No Reminders Found!")
        return

    print("\n===== Reminders =====")

    for date, reminder_list in reminders.items():
        print(f"\nDate: {date}")

        for r in reminder_list:
            print("- " + r)

# Delete Reminder
def delete_reminder():
    date = input("Enter Date (YYYY-MM-DD): ")

    if date in reminders:

        print("\nReminders on", date)

        for i, r in enumerate(reminders[date], start=1):
            print(f"{i}. {r}")

        choice = int(input("Enter Reminder Number to Delete: "))

        if 1 <= choice <= len(reminders[date]):
            removed = reminders[date].pop(choice - 1)

            print("Deleted Reminder:", removed)

            if not reminders[date]:
                del reminders[date]

        else:
            print("Invalid Choice!")

    else:
        print("No Reminders Found for this Date!")

# Main Menu
while True:

    print("\n===== Monthly Calendar Reminder App =====")
    print("1. Display Calendar")
    print("2. Add Reminder")
    print("3. View Reminders")
    print("4. Delete Reminder")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_calendar()

    elif choice == "2":
        add_reminder()

    elif choice == "3":
        view_reminders()

    elif choice == "4":
        delete_reminder()

    elif choice == "5":
        print("Exiting Application...")
        break

    else:
        print("Invalid Choice!")