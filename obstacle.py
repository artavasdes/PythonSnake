import random
import pygame
class Obstacles():

    def __init__(self, box_size, gridx, gridy, difficulty, color, snake):

        self.box_size = box_size
        self.gridx = gridx
        self.gridy = gridy
        self.all_obstacles = []
        self.color = color
        self.difficulty = difficulty
        self.snake = snake
    def create_obstacles(self):
        
        if self.difficulty == 1:
            
            # total_grids = (self.gridx // self.box_size) * (self.gridy // self.box_size)
            for i in range(5):

                
                new_obstacle = ([random.randrange(0, (self.gridx - self.box_size) // self.box_size) * self.box_size, 
                random.randrange(0, (self.gridy - self.box_size) // self.box_size) * self.box_size])
                while new_obstacle in self.snake.positions:
                    new_obstacle = ([random.randrange(0, (self.gridx - self.box_size) // self.box_size) * self.box_size, 
                    random.randrange(0, (self.gridy - self.box_size) // self.box_size) * self.box_size])
                self.all_obstacles.append(new_obstacle)
    def check_collision(self, snake):
        for obstacle in self.all_obstacles:
            if obstacle == snake.head_coords:
                return True
        
        return False
    
    def draw_obstacles(self, surface):
        
        for obstacle in self.all_obstacles:
            obstacle_box = pygame.Rect(obstacle[0], obstacle[1], self.box_size, self.box_size)
            pygame.draw.rect(surface, self.color, obstacle_box)

           
 