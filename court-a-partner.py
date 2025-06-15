def level2_courting():
    global current_state
    
    # Game objects
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 50
    player_speed = 5
    balloons = []
    birds = []
    love_meter = 0
    cupid_boost = 0
    
    # Font for love letters
    font = pygame.font.SysFont(None, 24)
    
    # Main level loop
    while current_state == GAME_STATE_LEVEL2:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Send love letter
                    balloons.append({
                        "x": player_x,
                        "y": player_y,
                        "text": "I ❤️ you",  # In real game, let player input text
                        "speed": 3 + cupid_boost
                    })
                    cupid_boost = 0  # Reset boost after use
        
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 20:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 20:
            player_x += player_speed
        
        # Update game state
        # Update balloons
        for balloon in balloons[:]:
            balloon["y"] -= balloon["speed"]
            if balloon["y"] < 50:  # Reached partner
                love_meter += 10
                balloons.remove(balloon)
            elif balloon["y"] < 0:  # Off screen
                balloons.remove(balloon)
        
        # Check for win condition
        if love_meter >= 100:
            current_state = GAME_STATE_LEVEL3
        
        # Draw everything
        screen.fill((135, 206, 235))  # Sky blue
        
        # Draw partner at top
        pygame.draw.rect(screen, (255, 192, 203), (SCREEN_WIDTH//2-15, 20, 30, 30))
        
        # Draw player (hot air balloon)
        pygame.draw.circle(screen, RED, (player_x, player_y), 20)
        
        # Draw balloons
        for balloon in balloons:
            pygame.draw.circle(screen, (255, 255, 255), (balloon["x"], balloon["y"]), 10)
            text_surface = font.render(balloon["text"], True, BLACK)
            screen.blit(text_surface, (balloon["x"]-15, balloon["y"]-5))
        
        # Draw love meter
        pygame.draw.rect(screen, WHITE, (50, 50, 200, 20), 1)
        pygame.draw.rect(screen, (255, 0, 127), (50, 50, 2*love_meter, 20))
        
        pygame.display.flip()
        clock.tick(FPS)