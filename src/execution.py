class IO_Execution:
    """
    This Class is used to store the information about the execution of the IO Requests
    This Class is also used for useful calculations about the execution of the IO Requests
    """

    def __init__(self):
        self.head_movement_sequence = []  # The sequence of the head movements
        self.total_head_movements = 0  # The total number of head movements

    def add_head_movement(self, head_movement):
        """
        Adds a head movement to the head_movement_sequence
        This will systematically update the total_head_movements
        :param head_movement: The head movement to be added
        :return: None
        """
        if (head_movement > self.head_movement_sequence[-1]):
            self.total_head_movements += head_movement - \
                self.head_movement_sequence[-1]
        else:
            self.total_head_movements += self.head_movement_sequence[-1] - \
                head_movement
        self.head_movement_sequence.append(head_movement)

    def get_head_movement_sequence(self):
        """
        Returns the head movement sequence
        :return: The head movement sequence
        """
        return self.head_movement_sequence

    def get_total_head_movements(self):
        """
        Returns the total number of head movements
        :return: The total number of head movements
        """
        return self.total_head_movements

    def print(self):
        """
        Prints the graph of the head movement sequence
        :return: None
        """
        print('Head Movement Sequence Graph')
        print('------------------------------------')
        for i in range(len(self.head_movement_sequence)):
            print('Track', i, ':', self.head_movement_sequence[i])
        print('------------------------------------')
        self.print_calculation()

    def print_calculation(self):
        """
        Prints the calculation of the head movement sequence
        Basing from the ppt format
        """

        print('Head Movement Sequence Calculation')
        print('------------------------------------')
        print('The Following are the number of tracks traversed by the read/write head:')
        print()

        list_of_calculation = []
        i = 1
        while i < len(self.head_movement_sequence):
            diff = abs(
                self.head_movement_sequence[i] - self.head_movement_sequence[i - 1])
            list_of_calculation.append(diff)
            # Fixed width for alignment
            from_track = f"Track {self.head_movement_sequence[i - 1]:<4}"
            # Fixed width for alignment
            to_track = f"Track {self.head_movement_sequence[i]:<4}"

            if (self.head_movement_sequence[i - 1] > self.head_movement_sequence[i]):
                minuend = self.head_movement_sequence[i - 1]
                subtrahend = self.head_movement_sequence[i]
                print(f"From {Colors.RED}{from_track}{Colors.RESET} "
                      f"to {Colors.GREEN}{to_track}{Colors.RESET} "
                      f"= {Colors.RED}{minuend:<3} {Colors.RESET} - {Colors.GREEN}{subtrahend:<3} {Colors.RESET} = {Colors.BLUE}{list_of_calculation[i - 1]} tracks{Colors.RESET}")
            else:
                minuend = self.head_movement_sequence[i]
                subtrahend = self.head_movement_sequence[i - 1]
                print(f"From {Colors.RED}{from_track}{Colors.RESET} "
                      f"to {Colors.GREEN}{to_track}{Colors.RESET} "
                      f"= {Colors.GREEN}{minuend:<3} {Colors.RESET} - {Colors.RED}{subtrahend:<3} {Colors.RESET} = {Colors.BLUE}{list_of_calculation[i - 1]} tracks{Colors.RESET}")

            i += 1

        print()
        print('The total number of tracks traversed by the read/write head:')
        blue_calculations = [f'{Colors.BLUE}{calc}{Colors.RESET}' for calc in list_of_calculation] #noqa
        print(' + '.join(blue_calculations), end='')
        print(f' = {Colors.BLUE}{self.total_head_movements} tracks{Colors.RESET}') #noqa
        # The two lines above have noqa because whenever formatting is applied
        # it will cause an error
        print('------------------------------------')


class Colors:
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
