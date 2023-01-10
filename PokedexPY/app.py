import pygame

pygame.init()

# Define the size of the screen (width, height).
size = (950, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pokedex Pernambucana")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pokedex = pygame.image.load("img/pokedex.png")
    pokedexP = pokedex.get_rect()
    screen.blit(pokedex, pokedexP)

    #bulbasaur = pygame.image.load("img/gifPokemons/bulbasaur.gif")
    #bulbasaurB = bulbasaur.get_rect()
    #screen.blit(bulbasaur, bulbasaurB)

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    #screen.fill((255, 255, 255))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
