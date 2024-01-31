class CustomOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.log_file = None
        self.counter_file = 'Lesson_21/counter.txt'

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        
        counter = self.get_counter() + 1
        with open(self.counter_file, 'w') as counter_file:
            counter_file.write(str(counter))

    def get_counter(self):
        try:
            with open(self.counter_file, 'r') as counter_file:
                return int(counter_file.read())
        except FileNotFoundError:
            return 0

with CustomOpen('Lesson_21/example.txt', 'w') as file1:
    file1.write("Hello, world!")

counter_value = CustomOpen('Lesson_21/example.txt', 'r').get_counter()
print("Counter value:", counter_value)
