#memory
import math, pygame, random, time

# User-defined functions
def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Memory')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 


# User-defined classes
class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.time = 0
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      # create board as an empty list
      self.click = False
      self.board = []
      self.board_size = 4
      self.create_board()
      
      self.tile1 = None
      self.tile2 = None
      self.clicked_image = 0
      self.paired_images = 0
      
      
   def create_board(self):
      #creates the board for the game
      #attributes for image list
      self.image_list_obj = []
      self.image_list_str = ['image' + (str(number)) +'.bmp' for number in range(1,9)] *2
      
      #convert image string list into image object list
      for image_str in self.image_list_str:
         image = pygame.image.load(image_str)
         self.image_list_obj.append(image_str)
         
      #randomizes image order in image_list_obj   
      random.shuffle(self.image_list_obj)
      #attributes for image size (width and height)
      width = image.get_width()
      height = image.get_height()
      default_cover = pygame.image.load('image0.bmp')      
      
      #create board
      for row_index in range(0, self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            x_coord = width * col_index
            y_coord = height * row_index
            image_index = row_index * self.board_size + col_index
            image = self.image_list_obj[image_index]
            tile = Tile(self.surface, x_coord, y_coord, image, default_cover)
            row.append(tile)
         self.board.append(row)
            
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
            if self.clicked_image == 0 or self.clicked_image == 1:
               self.handle_mouse_up(event.pos)

         
   def handle_mouse_up(self, position):
      #checks if the tiles on the board are selected
      #if the tile is clicked, the tile value is assigned to self.selected_tile1 and self.selected_tile2
      for row in self.board:
         for tile in row:
            if tile.select(position):
               self.clicked_image += 1
               tile.reveal_tile()
               
               if self.clicked_image == 1:
                  self.tile1 = tile
               if self.clicked_image == 2:
                  self.tile2 = tile
              
   def check_tile_match(self):
      # evaluates if the two selected tiles are the same
      #if tiles are the same, the tile stays revealed
      #if tiles are not the same, the tile will be hidden
      if self.clicked_image == 2:
         if self.tile1.compare_tiles(self.tile2):
            self.paired_images += 1
            self.tile1.reveal_tile()
            self.tile2.reveal_tile()
            self.tile1 = None
            self.tile2 = None
            self.clicked_image = 0
         else:
            self.tile1.hide_tile()
            self.tile2.hide_tile()
            self.tile1 = None
            self.tile2 = None
            self.clicked_image = 0
            
                     
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw the board and draw the time
      self.draw_tile()
      self.draw_time()
      pygame.display.update() # make the updated surface appear on the display
   
   def draw_tile(self):
      #draws each tile in every row
      for row in self.board:
         for tile in row:
            tile.draw()  
            
   def draw_time(self):
      #displays the score on to screen
      font_size = 70
      fg_color = pygame.Color('white')
      time = str(self.time)
      font = pygame.font.SysFont('Comic Sans', font_size)
      time_str_img = font.render(time, True, fg_color)
      
      pos = (self.surface.get_width() - time_str_img.get_width(), 0)
      self.surface.blit(time_str_img, pos)
      
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.time = pygame.time.get_ticks() // 1000
      self.check_tile_match()
      

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.paired_images == 8:
         self.continue_game = False
         
class Tile:
   # an object of this class represents a Rectangular Tile
   
   def __init__(self, surface, top, left, image, cover):
      #initalizes tile class
      #-top is the int x coord of the upper left corner
      #-left is the int y coord of the upper left corner
      #-image is of type image and is the image file to use
      #-surface is pygame.Surface object on which a Tile object is drawn on
      
      #attributes to initalize objects
      self.surface = surface
      self.top = top
      self.left = left

      self.image = pygame.image.load(image)
      self.image_name = image
      self.cover = cover
      self.hide = True
      
      width = self.image.get_width()
      height = self.image.get_height()
      
      self.rect = pygame.Rect(self.left, self.top, width, height)
      self.surface = surface
      self.selected = False
   
   def draw(self):
      # Draw the Tile
      #- self is the Tile object to draw
      color = pygame.Color('black')
      border_width = 10
      pygame.draw.rect(self.surface, color, self.rect, border_width)
      self.surface.blit(self.image, (self.left, self.top))
      
      if self.hide == False:
         self.surface.blit(self.image, self.rect)
      else:
         self.surface.blit(self.cover, self.rect)
   
   def select(self, pos):
      #returns true if the tile is selected
      #-pos is of type tup and the position of the mouse
      if self.rect.collidepoint(pos) and self.hide:
         self.selected = True
         self.reveal_tile()
      else:
         self.selected = False
         
      return self.selected
            
   def hide_tile(self):
      #set self.hide to false
      time.sleep(0.3)
      self.hide = True

   def reveal_tile(self):
      #set self.hide to true
      self.hide = False

   def compare_tiles(self, other_tile):
      #returns true if the tiles are the same (based on image string)
      return self.image_name == other_tile.image_name   
      
      

main()