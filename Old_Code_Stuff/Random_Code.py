class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def is_empty(check_function):
        def wrapper():
            if self.size > 0:
                return check_function()
            else:
                print("Stack is empty")
                return True

        return check_function()

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
        self.size += 1

    def pop(self):
        item_to_remove = self.top_item
        self.top_item = item_to_remove
        # Decrement the stack size here:
        self.size -= 1
        return item_to_remove

    def peek(self):
        return self.top_item


class Cell:
    def __init__(self, location, living_status=0):
        self.location = location
        self.living_status = living_status
        self.neighbors = None
        self.total_living_neighbors = None

    def is_alive(self):
        if self.living_status == 0:
            return False
        return True

    def set_living_status(self, living_status):
        self.living_status = living_status

    def get_living_status(self):
        return self.living_status

    def get_location(self):
        return self.location

    def set_neighbors(self, lst_cells):
        self.neighbors = []
        center = self.get_location()
        x = center[0]
        y = center[1]
        left_up = [x - 1, y - 1]
        up = [x, y - 1]
        right_up = [x + 1, y - 1]
        left = [x - 1, y]
        right = [x + 1, y]
        left_down = [x - 1, y + 1]
        down = [x, y + 1]
        right_down = [x + 1, y + 1]
        neighbor_locations = [left_up, up, right_up, left, right, left_down, down, right_down]
        for cell in lst_cells:
            if cell.get_location() in neighbor_locations:
                #print(f"{cell.get_location()}: is in {neighbor_locations}")
                self.neighbors.append(cell)
                neighbor_locations.remove(cell.get_location())
        if neighbor_locations != 0:
            #print("Not all neighbors were found!")
            for i in neighbor_locations:
                self.neighbors.append(Cell(i))
                #print(f"Adding {Cell(i)}")
        #print(f"Neighbors have been set for {self}:\n {self.neighbors}\n")

    def get_neighbors(self):
        if self.neighbors is None:
            self.set_neighbors([])
        return self.neighbors

    def set_living_neighbors(self):
        if self.neighbors is None:
            self.total_living_neighbors = 0
            return
        total_living = 0
        for cell in self.get_neighbors():
            if cell.is_alive():
                total_living += 1
        self.total_living_neighbors = total_living

    def get_living_neighbors(self):
        if self.get_neighbors is None:
            return 0
        return self.total_living_neighbors

    def __repr__(self):
        return f"Cell({self.get_location()} is {self.is_alive()})"


def get_generation(cells, generations):
    #    0  1  2
    # 0 [1, 0, 0]
    # 1 [0, 1, 1]
    # 2 [1, 1, 0]
    if generations <= 0:
        print(cells)
        return cells

    def generate_cells(cells):
        x_cell = len(cells[0])
        y_cell = len(cells)
        lst_cells = []
        for y in range(y_cell):
            for x in range(x_cell):
                new_cell = Cell([x, y])
                if cells[y][x] == 1:
                    new_cell.set_living_status(1)
                lst_cells.append(new_cell)
        for cell in lst_cells:
            cell.set_neighbors(lst_cells)
            cell.set_living_neighbors()
        return list(lst_cells)

    def generation_step(lst_cells):
        for cell in lst_cells:
            total_living = cell.get_living_neighbors()
            if total_living < 2 or total_living > 3:
                cell.set_living_status(0)
            elif total_living == 3:
                cell.set_living_status(1)

    lst_cells = generate_cells(cells)
    for _ in range(generations):
        generation_step(lst_cells)
    lst = []
    for cell in lst_cells:
        lst.append(cell.get_living_status())
    print(lst)
    return cells


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l1_node = l1
    l2_node = l2
    current_node = None
    prev_node = None
    carry = 0

    while l1_node is not None or l2_node is not None:
        if l1_node is None:
            l1_node = ListNode()
        if l2_node is None:
            l2_node = ListNode()
        current_value = l1_node.val + l2_node.val
        if carry > 0:
            current_value += 1
            carry = 0
        if current_value >= 10:
            current_value -= 10
            carry = 1
        l1_node = l1_node.next
        l2_node = l2_node.next
        current_node = ListNode(current_value, current_node)
