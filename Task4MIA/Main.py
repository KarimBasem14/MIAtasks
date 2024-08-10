
import pygame
from typing import Tuple


# Saw someone on youtube implement that if a piece was lost it would be placed to the right of the board but i probably won't implement it since I am trying to make my own version of this game
""" Things I want to implement but haven't: 
1. Only can move in valid moves and if i click on an invalid move it doesn't waste my turn. DONE 
2. If there is a piece blocking the path of another piece this must be accounted for in valid_moves



"""


pygame.init()
timer = pygame.time.Clock()
fps = 60
# Set display dimensions
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set title
pygame.display.set_caption("Chess Game")

# Colors
WHITE =(255,255,255)
BLACK = (0,0,0)
GOLD= (255,215,0)

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]


black_turn = True # Is it black's turn?
selected = False # Did he select a piece?
selected_piece_coords = ()
selected_piece = ""
turn_text = ["Black's turn: select a piece", "Black's turn: choose a tile to move to", "White's turn: select a piece", "White's turn: choose a tile to move to"]


# Font
font = pygame.font.Font('freesansbold.ttf', 32)

# LOAD GAME IMAGES
# r"" is used to make it a raw string so the \ doesn't give error inside the string
black_queen = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_rook,white_knight,white_bishop,white_king,white_queen,white_bishop,white_knight,white_rook,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn]
black_images = [black_rook,black_knight,black_bishop,black_king,black_queen,black_bishop,black_knight,black_rook,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']



def draw_board(): # Draws the board on the screen
    for x in range(8):
        for y in range(8):
            if (y+x) % 2 ==0: # This (x+y) % 2 == 0 is generally used if you want to generate a grid of any size
                pygame.draw.rect(screen,(0,0,0),( x*100,y*100, 100, 100))
            
    pygame.draw.line(screen, GOLD , (0, 8*100),(8*100,8*100),width=5) # horizontal line under the board
    pygame.draw.line(screen, GOLD ,(8*100,8*100),(8*100,0),width=5)  # Vertical line beside the board
def ingrid_range(x,y): # Returns true if position is inside the grid else returns false
    # Uses x,y insted of pos so i can easily edit them but now you have to unpack the args when you call the function using * 
    return (x<8 and x>=0) and (y<8 and y>=0)

def is_piece(pos): # Returns True if the position given is the position of a piece
    if pos in white_locations or pos in black_locations :
        return True

def highlight_square(square_pos):
    x,y = square_pos
    pygame.draw.rect(screen, (255,0,0), (x*100,y*100,100,100),2 ) # Highlights a square in red when that square is clicked, 2 is the width it makes it so that the rectangle doesn't fill the entire tile
    
def move_to_tile(initial_pos: Tuple[int, int], target: Tuple[int, int]): # The different syntax is used to make the fn only accept 2 tuples
    if black_turn:
        index = black_locations.index(initial_pos)
        black_locations[index] = target
    elif black_turn == False:
        index = white_locations.index(initial_pos)
        white_locations[index] = target

def show_turn_text():
    text = ""
    if black_turn:
        if selected == False:
            text= turn_text[0]
        elif selected == True:
            text = turn_text[1]
    elif black_turn == False:
        if selected == False:
            text= turn_text[2]
        elif selected == True:
            text = turn_text[3]
    
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 850))
    screen.blit(text_surface, text_rect)
    
def remove_piece(piece_type, piece_location): # Removes a piece's image from the board
    if piece_type == "White": 
        index = white_locations.index(piece_location)
        white_locations.pop(index)
        white_images.pop(index)
        white_pieces.pop(index)
    elif piece_type == "Black": 
        index = black_locations.index(piece_location)
        black_locations.pop(index)
        black_images.pop(index)
        black_pieces.pop(index)

def get_diagonal_moves(x, y, own_locations, opponent_locations): # This honestly was generated with chatGPT by I kinda understand how it works
    """
    Returns all diagonal moves for a bishop from the current position (x, y).
    Stops if a piece is encountered in any direction.
    """
    diagonal_moves = []

    # Check top-right diagonal
    for i in range(1, 8):
        new_x, new_y = x + i, y - i
        if not ingrid_range(new_x, new_y):
            break
        diagonal_moves.append((new_x, new_y))
        if (new_x, new_y) in own_locations:
            diagonal_moves.pop()  # Remove move if blocked by own piece
            break
        if (new_x, new_y) in opponent_locations:
            break

    # Check top-left diagonal
    for i in range(1, 8):
        new_x, new_y = x - i, y - i
        if not ingrid_range(new_x, new_y):
            break
        diagonal_moves.append((new_x, new_y))
        if (new_x, new_y) in own_locations:
            diagonal_moves.pop()  # Remove move if blocked by own piece
            break
        if (new_x, new_y) in opponent_locations:
            break

    # Check bottom-right diagonal
    for i in range(1, 8):
        new_x, new_y = x + i, y + i
        if not ingrid_range(new_x, new_y):
            break
        diagonal_moves.append((new_x, new_y))
        if (new_x, new_y) in own_locations:
            diagonal_moves.pop()  # Remove move if blocked by own piece
            break
        if (new_x, new_y) in opponent_locations:
            break

    # Check bottom-left diagonal
    for i in range(1, 8):
        new_x, new_y = x - i, y + i
        if not ingrid_range(new_x, new_y):
            break
        diagonal_moves.append((new_x, new_y))
        if (new_x, new_y) in own_locations:
            diagonal_moves.pop()  # Remove move if blocked by own piece
            break
        if (new_x, new_y) in opponent_locations:
            break

    return diagonal_moves


def get_valid_moves(piece, current_pos) -> list: # Returns a list of tubles of valid positions to move to 
    
    valid_moves = []
    x,y = current_pos
    if black_turn:
        if piece == "pawn":
            valid_moves = [(x, y - n) for n in range(1,3)]
        elif piece == "rook":
            for n in range(0,8):
                valid_moves.append((x, n))
                valid_moves.append((n, y))
            valid_moves.remove(current_pos) # Needs to be removed 2 times as the for loop adds it 2 times
            valid_moves.remove(current_pos) # My current position isn't a valid move
        elif piece == "knight":
            moves = [ (x+2, y+1), (x+2, y-1), (x+1, y-2), (x+1, y+2), (x-2, y+1), (x-2, y-1), (x-1, y-2), (x-1, y+2) ]
            valid_moves = [move for move in moves if ingrid_range(*move) ]
        elif piece == "bishop": # Needs fixing
            valid_moves = get_diagonal_moves(x, y, white_locations if black_turn else black_locations, black_locations if black_turn else white_locations)
        elif piece == "queen":
            valid_moves = get_diagonal_moves(x, y, white_locations if black_turn else black_locations, black_locations if black_turn else white_locations)
            for n in range(0,8):
                valid_moves.append((x, n))
                valid_moves.append((n, y))
            valid_moves.remove(current_pos) # Needs to be removed 2 times as the for loop adds it 2 times
            valid_moves.remove(current_pos) # My current position isn't a valid move
        elif piece == "king":
            # King moves one square in any direction
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if ingrid_range(new_x, new_y) and (new_x, new_y) not in black_locations:
                    valid_moves.append((new_x, new_y))
        for pos in black_locations:
            if pos in valid_moves:
                valid_moves.remove(pos) 
    elif not black_turn:
        if piece == "pawn":
            valid_moves = [(x,y+n) for n in range(1,3)]
        elif piece == "rook":
            for n in range(0,8):
                valid_moves.append((x, n))
                valid_moves.append((n, y))
            valid_moves.remove(current_pos) # Needs to be removed 2 times as the for loop adds it 2 times, can probably be improved
            valid_moves.remove(current_pos) # My current position isn't a valid move
        elif piece == "knight":
            moves = [ (x+2, y+1), (x+2, y-1), (x+1, y-2), (x+1, y+2), (x-2, y+1), (x-2, y-1), (x-1, y-2), (x-1, y+2) ]
            valid_moves = [move for move in moves if ingrid_range(*move) ]
        elif piece == "bishop": # Needs fixing
            valid_moves = get_diagonal_moves(x, y, white_locations if black_turn else black_locations, black_locations if black_turn else white_locations)
        elif piece == "queen":
            valid_moves = get_diagonal_moves(x, y, white_locations if black_turn else black_locations, black_locations if black_turn else white_locations)
            for n in range(0,8):
                valid_moves.append((x, n))
                valid_moves.append((n, y))
            valid_moves.remove(current_pos) # Needs to be removed 2 times as the for loop adds it 2 times
            valid_moves.remove(current_pos) # My current position isn't a valid move
        elif piece == "king":
            # King moves one square in any direction
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if ingrid_range(new_x, new_y) and (new_x, new_y) not in white_locations:
                    valid_moves.append((new_x, new_y))

        for pos in white_locations:
            if pos in valid_moves:
                valid_moves.remove(pos) 
    return valid_moves

def show_valid_moves(piece, current_pos) -> None: # Returns none but displays small bule circles on tiles with valid move positions
    if selected == True:
        valid_moves = get_valid_moves(piece, current_pos)
        
        for x,y in valid_moves:
            pygame.draw.circle(screen, (0,0,234), (x * 100 + 50, y * 100 + 50), 15)
    pygame.display.flip()

def draw_pieces():
    for i,(x,y) in enumerate(white_locations):
        screen.blit(white_images[i], (x*100,y*100))
    for i,(x,y) in enumerate(black_locations):
        screen.blit(black_images[i], (x*100,y*100))
    

    pygame.display.flip()
# Main game loop

running = True
while running:
    timer.tick(fps)
    
    screen.fill('dark gray')
    show_turn_text() # Putting this under draw_pieces() makes it flash from time to time
    draw_board()
    if selected_piece_coords: # Before this the red highlight used to flash
        highlight_square(selected_piece_coords)
    draw_pieces()
    show_valid_moves(selected_piece, selected_piece_coords)


    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if ingrid_range(*click_coords) and is_piece(click_coords) and selected == False: 
                """First condition is to make sure that you clicked somewhere on the board.
                   Second condition is to make sure you clicked on a tile with a piece on it
                   Third condition is to make sure you only select one piece at a time"""
                selected_piece_coords = click_coords
                selected = True 
                # After I click I want to obtain the piece's name to give it to show_valid_moves() later on
                if selected_piece_coords in black_locations:
                    index = black_locations.index(selected_piece_coords)
                    selected_piece = black_pieces[index]
                    if black_turn == False: # This condition makes it so that if i for example select a black piece i can't select a black one right after it
                    # I feel that these is something wrong though or it is a lil bit slow there might be unnoticable bugs but i can ignore them for now ig
                        selected = False
                if selected_piece_coords in white_locations:
                    index = white_locations.index(selected_piece_coords)
                    selected_piece = white_pieces[index]
                    if black_turn == True:
                        selected = False
                print(selected_piece)
            elif selected == True and click_coords in get_valid_moves(selected_piece,selected_piece_coords): # If you have selected a piece
                if click_coords in white_locations: # After selecting a piece, if i want to move that piece on a piece from that opposite team that piece from the opposite team is removed
                    remove_piece("White",click_coords)
                    
                elif click_coords in black_locations:
                    remove_piece("Black",click_coords)
                move_to_tile(selected_piece_coords, click_coords) # Move the piece to whatever place you click on YOU STILL HAVE TO MAKE SURE YOU CAN ONLY PLACE IT IN VALIDMOVES AND INSIDE THE GRID
                selected = False # Return to the nothing selected state
                selected_piece_coords = () 
                black_turn = not black_turn # switches turns
            print(click_coords)
            print(ingrid_range(*click_coords))
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
                
    

    pygame.display.flip()
pygame.quit()