import os
import management as m

io_request = m.IO_Request()
io_algorithm = m.IO_Algorithm(io_request)

if os.name != 'nt':
    io_request.read_input(r"src/input.txt")
else:
    io_request.read_input(r'src\input.txt')


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """
    Displays the Menu
    """
    print('+----------------------------------+')
    print('|--- *IO Management Simulation* ---|')
    print('+----------------------------------+\n')
    print('[1] FCFS - First-Come, First-Served')
    print('[2] SSTF - Shortest Seek Time First')
    print('[3] SCAN - Elevator Scan')
    print('[4] CSCAN - Circular Elevator SCAN')
    print('[5] LOOK - Elevator Modified LOOK')
    print('[6] CLOOK - Circular Elevator Modified LOOK\n')
    print('[0] Exit\n')



def main():
    """
    Main Function
    """
    while True:
        try:
            clear()
            display_menu()
            choice = input('Enter your choice: ')

            if choice == '0':
                print('Exiting...')
                break

            choice = int(choice)
            if 1 <= choice <= 6:
                algorithm_names = {
                    1: 'FCFS', 2: 'SSTF', 3: 'SCAN',
                    4: 'CSCAN', 5: 'LOOK', 6: 'CLOOK'
                }
                algorithm_name = algorithm_names[choice] + ' Algorithm'
                clear()
                print(algorithm_name)
                print('------------------------------------')
                io_algorithm.set_algorithm(algorithm_names[choice])
                io_algorithm.simulate()
                input("Press Enter to continue...")
            else:
                clear()
                print('Invalid Choice! Please choose a number between 0 and 6.')
                input("Press Enter to continue...")
        except ValueError:
            clear()
            print('Invalid input! Please enter a valid number.')
            input("Press Enter to continue...")
        except Exception as e:
            clear()
            print(f'An error occurred: {str(e)}')
            input("Press Enter to continue...")


if __name__ == '__main__':
    main()
