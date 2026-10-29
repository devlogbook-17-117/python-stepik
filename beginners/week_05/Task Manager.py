
# Print two blank lines to separate sections of the interface.
def print_spacing():
    print()
    print()


# Display the application header.
print('=' * 50)
print('TASK MANAGER'.center(50))
print('=' * 50)

print_spacing()

# Store all tasks in a list.
tasks = []

# Define the actions available in the main menu.
menu = '''Menu:

1. View tasks
2. Add tasks
3. Delete tasks
4. Exit'''

# Keep displaying the menu until the user chooses to exit.
while True:
    print(menu)
    print()

    # Ask the user to select an action.
    act = input('Choose an option: ')

    # Option 1: Display the current task list.
    if act.strip() == '1':
        if len(tasks) == 0:
            print("Your task list is empty.")
            print_spacing()
        else:
            # Display each task with its current number.
            for i in range(len(tasks)):
                print(f'{i + 1}. {tasks[i]}')
            print()

    # Option 2: Add new tasks to the list.
    elif act.strip() == '2':
        quantity = input('How many tasks would you like to add? ')
        quantity = quantity.strip()

        # Make sure the quantity contains only digits.
        if not quantity.isdigit():
            print('Invalid input.')
            print_spacing()

        # Return to the menu if the requested quantity is zero.
        elif int(quantity) == 0:
            print()
            continue

        else:
            # Count only tasks that contain non-whitespace characters.
            k = 0

            while k != int(quantity):
                new_task = input('Enter task: ')

                if new_task.strip():
                    # Remove surrounding whitespace before saving the task.
                    k += 1
                    tasks.append(new_task.strip())
                else:
                    print('Invalid input.')

            print_spacing()

    # Option 3: Delete tasks by their current numbers.
    elif act.strip() == '3':
        if len(tasks) == 0:
            print("Your task list is empty.")
            print_spacing()
        else:
            # Display the tasks before asking which ones to delete.
            fl = False

            for i in range(len(tasks)):
                print(f'{i + 1}. {tasks[i]}')

            # Allow multiple task numbers separated by spaces.
            delete = input(
                'Enter the task number(s) to delete, separated by spaces: '
            ).strip().split(' ')

            # Combine the entered values for the input validation below.
            str_delete = ''
            for f in delete:
                str_delete += f

            # Check whether the input contains at least one numeric value.
            for check in delete:
                if check.isdigit():
                    fl = True
                    break

            if fl:
                for i in range(len(delete)):

                    # Delete a single task if its number is valid.
                    if (
                        delete[i].isdigit()
                        and len(delete) == 1
                        and 1 <= int(delete[i]) <= len(tasks)
                    ):
                        del tasks[int(delete[i]) - 1]
                        print('Task deleted successfully.')
                        print_spacing()

                    # Process multiple task numbers.
                    elif delete[i].isdigit() and len(delete) > 1:
                        flag = False

                        # Mark valid tasks before removing them.
                        # This prevents earlier deletions from shifting
                        # the positions of tasks that are still to be checked.
                        for j in range(len(delete)):
                            if (
                                delete[j].isdigit()
                                and 1 <= int(delete[j]) <= len(tasks)
                            ):
                                flag = True
                                tasks[int(delete[j]) - 1] = ' '

                        # Remove all marked tasks from the list.
                        ind = 0
                        count = 0

                        while ' ' in tasks:
                            if tasks[ind] == ' ':
                                count += 1
                                del tasks[ind]
                            else:
                                ind += 1

                        # Display the appropriate success message.
                        if flag:
                            if count == 1:
                                print('Task deleted successfully.')
                                print_spacing()
                                break
                            elif count > 1:
                                print('Tasks deleted successfully.')
                                print_spacing()
                                break
                        else:
                            print('Invalid input.')
                            print_spacing()
                            break

                    # Ignore non-numeric entries.
                    elif not delete[i].isdigit():
                        continue

                    # Report invalid numeric input when no valid deletion
                    # can be processed through the preceding conditions.
                    elif (
                        delete[i].isdigit()
                        and not (1 <= int(delete[i]) <= len(tasks))
                    ) or not str_delete.isspace():
                        print('Invalid input.')
                        print_spacing()
                        break

            else:
                # Display an error if the input contains no numeric values.
                print('Invalid input.')
                print_spacing()

    # Option 4: Exit the application.
    elif act.strip() == '4':
        print('Goodbye!')
        break

    # Handle choices that do not match any menu option.
    else:
        print('Invalid option.')
        print_spacing()
