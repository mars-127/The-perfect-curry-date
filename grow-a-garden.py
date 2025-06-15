class Plant:
    def __init__(self, x, y, plant_type):
        self.x = x
        self.y = y
        self.type = plant_type
        self.growth = 0
        self.max_growth = random.randint(100, 150)
        self.water = 50
        self.sunlight = 50
        
    def update(self):
        # Plants grow with adequate water and sunlight
        if self.water > 30 and self.sunlight > 30:
            self.growth += 0.5
        self.water -= 0.2
        self.sunlight -= 0.1
        
    def draw(self, screen):
        # Simple pixel art representation
        if self.growth < self.max_growth / 3:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, 10, 5))
        elif self.growth < 2 * self.max_growth / 3:
            pygame.draw.rect(screen, GREEN, (self.x, self.y-5, 10, 10))
        else:
            if self.type == "rice":
                pygame.draw.rect(screen, (200, 200, 100), (self.x, self.y-10, 10, 15))
            else:
                pygame.draw.rect(screen, (150, 75, 0), (self.x, self.y-10, 10, 15))

def level1_garden():
    global current_state
    
    # Game objects
    plants = []
    inventory = {
        "rice": 0,
        "rajma": 0,
        "spices": 0,
        "vegetables": 0,
        "salt": 0
    }
    
    # Game variables
    water_level = 100
    sunlight_level = 100
    stamina = 100
    
    # Main level loop (simplified)
    while current_state == GAME_STATE_LEVEL1:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Plant new seeds
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.button == 1:  # Left click
                    plants.append(Plant(mouse_x, mouse_y, "rice"))
                elif event.button == 3:  # Right click
                    plants.append(Plant(mouse_x, mouse_y, "rajma"))
        
        # Update game state
        for plant in plants[:]:
            plant.update()
            if plant.growth >= plant.max_growth:
                if plant.type == "rice":
                    inventory["rice"] += 1
                else:
                    inventory["rajma"] += 1
                plants.remove(plant)
        
        # Check if all ingredients are collected
        if all(v > 0 for v in inventory.values()):
            current_state = GAME_STATE_LEVEL2
        
        # Draw everything
        screen.fill((200, 200, 150))  # Light brown dirt
        
        for plant in plants:
            plant.draw(screen)
        
        # Draw UI (inventory, etc.)
        pygame.display.flip()
        clock.tick(FPS)