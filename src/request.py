class IO_Request:
    """
    The Starting Point of the IO Management Simulation
    This is the class that will be used to create the IO Requests,
    to hold necessary information about the IO Requests, and to
    store the user requested IO Requests.
    """

    def __init__(self, ):
        self.request_number = 0  # The number of IO Requests to be simulated
        self.disk_size = 0  # The size of the disk or the maximum track number
        self.requested_tracks = []
        self.current_track = 0  # The current track of the read/write head
        # The total number of head movements or the total distance traveled by the read/write head
        self.total_head_movements = 0
        self.algorithm = None  # The algorithm to be used for the simulation

    def read_input(self, input_file):
        """
        Reads the input file and stores the information in the IO_Request object
        <FORMAT>
        <REQUEST NUMBER>
        <DISK SIZE>
        <REQUESTED TRACKS> (separated by spaces)
        <CURRENT TRACK>
        <ALGORITHM>

        <EXAMPLE>
        10
        200
        98 183 37 122 14 124 65 67
        53
        FCFS

        :param input_file: The input file containing the information about the IO Requests
        :return: None
        """
        with open(input_file, 'r') as f:
            self.request_number = int(f.readline())
            self.disk_size = int(f.readline())
            self.requested_tracks = list(map(int, f.readline().split()))
            self.current_track = int(f.readline())
            self.algorithm = f.readline().strip()

    def take_input(self):
        """
        Takes the input from the user and stores the information in the IO_Request object
        :return: None
        """
        self.request_number = int(
            input('Enter the number of IO Requests to be simulated: '))
        self.disk_size = int(
            input('Enter the size of the disk or the maximum track number: '))
        self.requested_tracks = list(
            map(int, input('Enter the requested tracks (separated by spaces): ').split()))
        self.current_track = int(
            input('Enter the current track of the read/write head: '))
        self.algorithm = input(
            'Enter the algorithm to be used for the simulation: ').strip()

    def print_input(self):
        """
        Prints the information about the IO Requests
        :return: None
        """
        print(f'Request Number: {self.request_number}')
        print(f'Disk Size: {self.disk_size}')
        print(f'Requested Tracks: {self.requested_tracks}')
        print(f'Current Track: {self.current_track}')
        print(f'Algorithm: {self.algorithm}')

    def set_algorithm(self, algorithm):
        """
        Sets the algorithm to be used for the simulation
        :param algorithm: The algorithm to be used for the simulation
        :return: None
        """
        self.algorithm = algorithm
