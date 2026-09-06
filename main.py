import pygame
import sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
from start_screen import StartScreen
from end_screen import EndScreen

def main():

	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	start_screen = StartScreen(screen)
	end_screen = EndScreen(screen)
	started = False
	game_over = False
				
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				log_event("game_exit")
				return
			elif event.type == pygame.KEYDOWN and started == False and game_over == False:
				log_event("game_start")
				for asteroid in asteroids:
					asteroid.kill()
				player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
				player.rotation = 0
				player.cooldown_timer = 0
				started = True
			elif event.type == pygame.KEYDOWN and started == True and game_over == True:
				log_event("game_restart")
				for asteroid in asteroids:
					asteroid.kill()
				game_over = False
				started = False
		
		screen.fill("black")

		if started == False:
			asteroid_field.update(dt)
			for asteroid in asteroids:
				asteroid.update(dt)
			start_screen.draw()
			for asteroid in asteroids:
				asteroid.draw(screen)
		elif game_over == False:
			for obj in updatable:
				obj.update(dt)
			for asteroid in asteroids:
				if player.collides_with(asteroid):
					log_event("player_hit")
					print("Game Over!")
					game_over = True
				else:
					for shot in shots:
						if shot.collides_with(asteroid):
							log_event("asteroid_shot")
							shot.kill()
							asteroid.split()
			for obj in drawable:
				obj.draw(screen)
		else:
			asteroid_field.update(dt)
			for asteroid in asteroids:
				asteroid.update(dt)
			end_screen.draw()
			for asteroid in asteroids:
				asteroid.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
