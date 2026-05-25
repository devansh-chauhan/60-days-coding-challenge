class ThemeParkQueue:
    def __init__(self):
        self.vip_queue = []
        self.normal_queue = []

    def add_visitor(self, name, vip=False):

        if vip:
            self.vip_queue.append(name)
            print(f"{name} joined the VIP queue.")

        else:
            self.normal_queue.append(name)
            print(f"{name} joined the normal queue.")

    def process_visitor(self):

        if len(self.vip_queue) > 0:
            visitor = self.vip_queue.pop(0)
            print(f"Processing VIP visitor: {visitor}")

        elif len(self.normal_queue) > 0:
            visitor = self.normal_queue.pop(0)
            print(f"Processing normal visitor: {visitor}")

        else:
            print("No visitors in queue")

    def display_queues(self):
        print("\nCurrent Queue Status:")
        print("VIP Queue    :", self.vip_queue)
        print("Normal Queue :", self.normal_queue)


park = ThemeParkQueue()

park.add_visitor("Alice")
park.add_visitor("Bob")
park.add_visitor("Charlie", vip=True)
park.add_visitor("David")
park.add_visitor("Eva", vip=True)

park.display_queues()

print("\nProcessing Visitors:\n")

park.process_visitor()
park.process_visitor()
park.process_visitor()

park.display_queues()