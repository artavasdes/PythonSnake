#Snake object
class Snake():

    def __init__(self, color, start_direction):
        #maybe make color customizable by player later
        self.x = 0
        self.y = 0
        #^to do: generate random coords for snake based on grid

        self.positions = [(self.x, self.y), (self.x - 1, self.y - 1), (self.x - 2, self.y - 2)]
        self.direction = start_direction
        self.color = color
        self.head_coords = self.positions[0]

    def move(self, direction):

        if direction == 'UP':
            self.head_coords = (self.head_coords[0], self.head_coords[1] - 1)
        elif direction == "DOWN":
            self.head_coords = (self.head_coords[0], self.head_coords[1] + 1)
        elif direction == "RIGHT":
            self.head_coords = (self.head_coords[0] + 1, self.head_coords[1])
        elif direction == "LEFT":
            self.head_coords = (self.head_coords[0] - 1, self.head_coords[1])
        
        self.positions.insert(0, self.head_coords)



    def controls(self):
        self.left = 
        self.right = 
        


    def movement(self):
        self.speed = 

