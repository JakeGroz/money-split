class NightOut:

    def __init__(self):
        self.entries = []
        self.amount_spent = 0
        self.people = {}

    def read_entries(self, filename):
        file = open(filename)
        contents = file.readlines()

        for i in range(len(contents)):
            self.entries.append(contents[i].strip('\n').strip().split(","))
            self.entries[i][0] = self.entries[i][0].split("/")

        for line in self.entries:
            print(line)

    def total_amount(self):
        for entry in self.entries:
            self.amount_spent += float(entry[2])
        print(round(self.amount_spent, 2))

    def purchase_descriptions(self):
        desc = []
        for entry in self.entries:
            desc.append(entry[2:])

        for line in desc:
            print(line)

    def calculate_owing(self):
        for entry in self.entries:
            payer = entry[-1]
            split = entry[1]
            # populating dictionary
            for person in entry[0]:
                if person != payer:
                    if person not in self.people:
                        # (amount spend, amount owing, amount owed)
                        self.people[person] = [0, 0, 0]

                    if split == "evensplit":
                        _, current_owing, _ = self.people[person]
                        self.people[person][1] += float(entry[2])/len(entry[0])

        print(self.people)

    def calculate_spent_pp(self):
        for entry in self.entries:
            amount, payer = float(entry[2]), entry[-1]
            if payer not in self.people:
                self.people[payer] = [0, 0, 0]
            else:
                balance, _, _ = self.people[payer]
                self.people[payer][0] = balance + amount

        print(self.people)

    def calculate_owed(self):
        for entry in self.entries:
            total_people, split, amount, payer = len(entry[0]), entry[1], float(entry[2]), entry[-1]
            _, _, owed = self.people[payer]
            if split == "evensplit":
                self.people[payer][2] = owed + (amount/total_people)*(total_people-1)

        print(self.people)



if __name__ == "__main__":

    x = NightOut()
    x.read_entries("testEntries.txt")
    x.total_amount()
    x.purchase_descriptions()
    x.calculate_owing()
    x.calculate_spent_pp()
    x.calculate_owed()

    # def print_options():
    #     print("1. Enter file name to read: ")
    #     print("2. Total Balance")
    #     print("3. All purchases")
    #     print("4. Amount Spend per Person")
    #     print("5. Amount Owed per Person")
    #     print("6. Make Payment: ")
    #     print("Q. Quit")
    #
    # quit = False
    #
    # while not quit:
    #     print_options()
    #     action = input("What would you like to do: ")