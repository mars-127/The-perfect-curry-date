def end_screen():
    # Display final scene
    screen.fill((50, 30, 10))  # Dark brown table
    
    # Draw plate of curry
    pygame.draw.circle(screen, WHITE, (400, 300), 100)
    pygame.draw.circle(screen, (200, 100, 50), (400, 300), 90)
    
    # Draw couple
    pygame.draw.circle(screen, (255, 218, 185), (300, 400), 30)  # Player
    pygame.draw.circle(screen, (255, 192, 203), (500, 400), 30)    # Partner
    
    # Draw text
    font = pygame.font.SysFont(None, 48)
    text = font.render("Perfect Curry Date Night Success!", True, WHITE)
    screen.blit(text, (150, 100))
    
    pygame.display.flip()
    
    # Wait before exiting
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()