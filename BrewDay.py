import pygame

# Define Variables

hop1 = "Centennial"
hop2 = "Amarillo"
hop3 = "Simcoe"

pretimer = 1
brewLength = 3600
addition1 = 3530
addition2 = 1800
addition3 = 1800
addition4 = 600
addition5 = 600

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Brew Day")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60

def BrewClock():
    total_seconds = frame_count // frame_rate
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [25, 30]) 
    
def CountDown():
    total_seconds = brewLength - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Brew Time left: {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, BLACK)
 
    screen.blit(text, [25, 60])
  
def TimeUntilAddition(hop, hopTime, addition):
    font_color = BLACK
    total_seconds = brewLength - hopTime - (frame_count // frame_rate)
    if total_seconds < 0:
       total_seconds = 0
       font_color = RED
       
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
   # Use python string formatting to format in leading zeros
    output_string = "Time until " + hop + ": {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, font_color)
    if total_seconds == 15:
       pygame.mixer.music.load('audio/Course.mp3')
       pygame.mixer.music.play(0)

 
    screen.blit(text, [25, addition*30+60])
  
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(WHITE)
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    BrewClock() 
    CountDown()
    TimeUntilAddition(hop1, addition1, 1)
    TimeUntilAddition(hop2, addition2, 2)
    TimeUntilAddition(hop3, addition3, 3)
    TimeUntilAddition(hop2, addition4, 4)
    TimeUntilAddition(hop3, addition5, 5)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    frame_count += 1
 
    # Limit frames per second
    clock.tick(frame_rate)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
