class Node:

    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find(self.data, '_')

        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]

        children = []

        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])

            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)

        return children

    def shuffle(self, puz, x1, y1, x2, y2):

        if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3:

            temp_puz = [row[:] for row in puz]

            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp

            return temp_puz
        else:
            return None

    def find(self, puz, x):

        for i in range(3):
            for j in range(3):
                if puz[i][j] == x:
                    return i, j


class Puzzle:

    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):

        puz = []

        for i in range(self.n):
            temp = input().split()
            puz.append(temp)

        return puz

    def h(self, start, goal):

        temp = 0

        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1

        return temp

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def process(self):

        print("Enter Start State Matrix:")
        start = self.accept()

        print("Enter Goal State Matrix:")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        self.open.append(start)

        while True:

            cur = self.open[0]

            print("\nCurrent State:\n")

            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print()

            if self.h(cur.data, goal) == 0:
                print("\nGoal State Reached!")
                break

            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            self.closed.append(cur)
            del self.open[0]

            self.open.sort(key=lambda x: x.fval)


puz = Puzzle(3)
puz.process()

#input
#1 2 3
#5 6 _
#7 8 4

#goal
#1 2 3
#5 8 6
#7 _ 4
