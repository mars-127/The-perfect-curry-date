def level3_cooking():
    global current_state
    
    # Ingredients from level 1
    ingredients = {
        "rice": 1,
        "rajma": 1,
        "spices": 1,
        "vegetables": 1,
        "salt": 1
    }
    
    # Cooking variables
    heat = 50
    stirring = 0
    cooking_stage = 0  # 0=frying, 1=simmering, 2=serving
    
    # Main level loop
    while current_state == GAME_STATE_LEVEL3:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stirring += 1
        
        # Update game state
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            heat = min(100, heat + 1)
        if keys[pygame.K_DOWN]:
            heat = max(0, heat - 1)
        
        # Progress through cooking stages
        if cooking_stage == 0 and stirring > 30:
            cooking_stage = 1
            stirring = 0
        elif cooking_stage == 1 and 40 < heat < 60 and stirring > 50:
            cooking_stage = 2
        
        # Check for completion
        if cooking_stage == 2:
            current_state = GAME_STATE_END
        
        # Draw everything
        screen.fill((50, 50, 50))
        
        # Draw pot
        pygame.draw.rect(screen, (70, 70, 70), (300, 300, 200, 150))
        
        # Draw contents based on stage
        if cooking_stage == 0:
            pygame.draw.rect(screen, (150, 100, 50), (310, 310, 180, 130))
        elif cooking_stage == 1:
            pygame.draw.rect(screen, (180, 80, 40), (310, 310, 180, 130))
        else:
            pygame.draw.rect(screen, (200, 60, 30), (310, 310, 180, 130))
        
        # Draw UI
        pygame.draw.rect(screen, WHITE, (50, 400, 200, 20), 1)
        pygame.draw.rect(screen, RED, (50, 400, 2*heat, 20))
        
        pygame.display.flip()
        clock.tick(FPS)