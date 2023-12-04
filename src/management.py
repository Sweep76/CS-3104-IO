from execution import IO_Execution
from request import IO_Request

import matplotlib.pyplot as plt
# Above line has warning however the program still works

class IO_Algorithm:
    """
    This Class is used to simulate the various IO Algorithms
    """

    def __init__(self, io_request):
        """
        Initializes the IO_Algorithm object
        :param io_request: The IO_Request object containing the information about the IO Requests
        """
        self.io_request = io_request
        self.io_execution = IO_Execution()

    def simulate(self):
        """
        Simulates the IO Algorithm
        :return: None
        """
        self.reset_execution()
        if (self.io_request.algorithm == 'FCFS'):
            self.fcfs()
        elif (self.io_request.algorithm == 'SSTF'):
            self.sstf()
        elif (self.io_request.algorithm == 'SCAN'):
            self.scan()
        elif (self.io_request.algorithm == 'CSCAN'):
            self.cscan()
        elif (self.io_request.algorithm == 'LOOK'):
            self.look()
        elif (self.io_request.algorithm == 'CLOOK'):
            self.clook()
        else:
            print('Invalid Algorithm!')

    def fcfs(self):
        """
        Simulates the FCFS Algorithm
        :return: None
        """

        for track in self.io_request.requested_tracks:
            self.io_execution.add_head_movement(track)

        self.print_graph_gui()

    def sstf(self):
        """
        Simulates the SSTF Algorithm
        :return: None
        """
        self.Queue = self.io_request.requested_tracks.copy()
        while (len(self.Queue) > 0):
            min_distance = self.io_request.disk_size + 1
            min_index = -1
            for i in range(len(self.Queue)):
                if (abs(self.Queue[i] - self.io_execution.head_movement_sequence[-1]) < min_distance):
                    min_distance = abs(
                        self.Queue[i] - self.io_execution.head_movement_sequence[-1])
                    min_index = i
            self.io_execution.add_head_movement(self.Queue.pop(min_index))

        self.print_graph_gui()

    def scan(self):
        """
        Simulates the SCAN Algorithm
        :return: None
        """
        self.Queue = self.io_request.requested_tracks.copy()

        # Check if the queue has any tracks that reaches to the end or max-1
        # If not, then add the max-1 track to the queue
        # This is done to simulate the head movement from the last track to the first track
        if (max(self.Queue) != self.io_request.disk_size - 1):
            self.Queue.append(self.io_request.disk_size - 1)

        # Or you could just add the max track to the queue regardless of whether it is present or not
        # self.Queue.append(self.io_request.disk_size - 1)
        # Though this is usually dependent on how you want to implement SCAN

        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Reverse direction and move towards the lowest track
        current_track = highest_track - 1
        while current_track >= lowest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track -= 1

        self.print_graph_gui()

    def cscan(self):
        """
        Simulates the C-SCAN Algorithm
        :return: None
        """
        self.Queue = self.io_request.requested_tracks.copy()
        # Check if the queue has any tracks that reaches to the end or max-1
        # If not, then add the max-1 track or/and 0 track to the queue
        # This is done to simulate the head movement from the last track to the first track
        if (max(self.Queue) != self.io_request.disk_size - 1):
            self.Queue.append(self.io_request.disk_size - 1)
        if (min(self.Queue) != 0):
            self.Queue.append(0)

        # Or you could just add the max track and 0 track to the queue regardless of whether it is present or not
        # self.Queue.append(self.io_request.disk_size - 1)
        # self.Queue.append(0)
        # Though this is usually dependent on how you want to implement C-SCAN

        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Move towards the lowest track
        current_track = lowest_track
        while current_track < self.io_request.disk_size:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        self.print_graph_gui()

    def look(self):
        """
        Simulates the LOOK Algorithm
        :return: None
        """
        self.Queue = self.io_request.requested_tracks.copy()
        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Reverse direction and move towards the lowest track
        current_track = highest_track - 1
        while current_track >= lowest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track -= 1

        self.print_graph_gui()

    def clook(self):
        """
        Simulates the C-LOOK Algorithm
        :return: None
        """
        self.Queue = self.io_request.requested_tracks.copy()
        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Move towards the lowest track
        current_track = lowest_track
        while current_track < highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        self.print_graph_gui()

    def print_graph_gui(self):
        """
        Prints the graph of the head movement sequence
        :return: None
        """
        self.io_execution.print()
        plt.plot(self.io_execution.head_movement_sequence,
                 marker='o', linestyle='--', color='r')

        plt.ylabel('Track Number', fontweight='bold')
        # plt.xlabel('Time')
        # plt.xlable('Track Number')
        # Up to you which one you want to use but I use the one below
        plt.xlabel(f'Total Head Movement = {self.io_execution.total_head_movements}', fontweight='bold')  # noqa
        plt.title(f'Graph of {self.io_request.algorithm} Algorithm', fontweight='bold', loc='center')  # noqa
        # These 2 can cause errors whenever formatting the code with autopep8
        # Thats why I have # noqa at the end of the line
        plt.grid(True)
        plt.ylim(0, self.io_request.disk_size)
        for i in range(len(self.io_execution.head_movement_sequence)):
            plt.annotate(self.io_execution.head_movement_sequence[i], (
                i, self.io_execution.head_movement_sequence[i]))
        plt.xticks(range(len(self.io_execution.head_movement_sequence)))

        plt.show()

    def set_algorithm(self, algorithm):
        """
        Sets the algorithm to be used for the simulation
        :param algorithm: The algorithm to be used for the simulation
        :return: None
        """
        self.io_request.algorithm = algorithm

    def reset_execution(self):
        """
        Resets the execution
        :return: None
        """
        self.io_execution.head_movement_sequence = []
        self.io_execution.head_movement_sequence.append(
            self.io_request.current_track)
        self.io_execution.total_head_movements = 0
        self.Queue = []
