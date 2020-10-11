# IMPORTING ALL THE LIBRARIES
import random
import sys
import time

import pygame
import pygame.mixer
from pygame.locals import *


# EXITING THE GAME


def events():
	for event in pygame.event.get():
		if event.type == QUIT(event.type == KEYDOWN and event.key == K_x):
			pygame.quit()
			sys.exit()


def __init__(self):
	self.rect = pygame.Rect(32, 32, 16, 16)


pygame.init()

# Setup The display
DISPLAY_WIDTH, DISPLAY_HEIGHT = 700, 1000
CENTRE_X, CENTRE_Y = DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2

clock = pygame.time.Clock()
pygame.display.set_caption('NOTGalaga')

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
bg_img = pygame.image.load("bg1.png").convert()
bg_img = pygame.transform.scale(bg_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
bg_img_w, bgImgH = bg_img.get_rect().size
bg_y = 0

black = (0, 0, 0)
white = (255, 255, 255)

PLAYER_WIDTH = 51
PLAYER_HEIGHT = 51
ENEMY_HEIGHT = 16
ENEMY_WIDTH = 16
ENEMY_AREA = ENEMY_HEIGHT * ENEMY_WIDTH
destroyed = False

font = pygame.font.Font('notgalaga.ttf', 25)

# Importing User Spacecraft
player_img = pygame.image.load('User1.png')
player_img = pygame.transform.scale(player_img, (65, 65))
player = player_img.get_rect()

# Importing Enemies
raw_enemy_img = pygame.image.load('alien1.png')
enemy_img = pygame.transform.scale(raw_enemy_img, (32, 32))
enemy = enemy_img.get_rect()
NEW_ENEMY = 10
enemies = []
for i in range(6):
	enemies.append(enemy)


# bullet_img = pygame.image.load('Bullet1.png')
# bullet_img = pygame.transform.scale(bullet_img, (15, 15))
# bullet_sound = pygame.mixer.Sound('Laser.wav')
# bullet = bullet_img.get_rect()



# Defining Intro Music


# def intro_s():
# 	pygame.mixer.music.load('Intro.mp3')
# 	pygame.mixer.music.play(0, 4.0)
#
#
# def bullet_s():
# 	pygame.mixer.music.load('Laser.mp3')
# 	pygame.mixer.music.play()
#
# # Defining Death Music
#
#
# def death_s():
# 	pygame.mixer.music.load('Death.mp3')
# 	pygame.mixer.music.play(-1, 320.40)

# Defining User Spacecraft


def draw_user(x, y):
	game_display.blit(player_img, (x, y))


# def draw_background():
# 	yloop = y_bg % bgImgH
# 	game_display.blit(bg_img, (0, yloop - bgImgH))
# 	if yloop < DISPLAY_HEIGHT:
# 		game_display.blit(bg_img, (0, yloop))
# 	y_bg += 4
# Defining Enemies
def draw_enemy(enemyx, enemyy):
	game_display.blit(enemy_img, (enemyx, enemyy))


def draw_bullet(bulletx, bullety):

	pygame.Surface(player_img, (bulletx, bullety))
	game_display.blit(bullet_img, (bulletx, bullety))


def text_objects(text, font):
	text_surface = font.render(text, True, white)
	return text_surface, text_surface.get_rect()


def message_display():
	#death_s()
	big_text = pygame.font.Font('notgalaga.ttf', 105)
	text_surf, text_rect = text_objects('-+ YOU DEAD +-', big_text)
	text_rect.center = (CENTRE_X, CENTRE_Y - 100)
	game_display.blit(text_surf, text_rect)

	small_text = pygame.font.Font('notgalaga.ttf', 39)
	text_surf1, text_rect1 = text_objects("- Press Space to Start -", small_text)
	text_rect1.center = (CENTRE_X, CENTRE_Y + 200)
	game_display.blit(text_surf1, text_rect1)

	pygame.display.update()
	time.sleep(2)

	game_loop()


def crash_game():
	message_display()


def intro_game():

	intro = True
	#intro_s()
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			big_text = pygame.font.Font('notgalaga.ttf', 62)
			text_surf, text_rect = text_objects("WELCOME TO NOTGALAGA", big_text)
			text_rect.center = (CENTRE_X, CENTRE_Y)
			game_display.blit(text_surf, text_rect)

			small_text = pygame.font.Font('notgalaga.ttf', 39)
			text_surf1, text_rect1 = text_objects("- Press Space to Start -", small_text)
			text_rect1.center = (CENTRE_X, CENTRE_Y + 200)
			game_display.blit(text_surf1, text_rect1)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_loop()
				elif (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_x):
					pygame.quit()
					sys.exit()

			pygame.display.update()
			clock.tick(15)


def game_loop():
	x = (DISPLAY_WIDTH * 0.45)
	y = (DISPLAY_HEIGHT * 0.8)
	x_change = 0
	y_change = 0
	y_bg = 0
	enemy_start_x = random.randrange(0, DISPLAY_WIDTH)
	enemy_start_y = -600
	enemy_speed = 5
	bullet_y = y
	bullet_x = x
	bullet_speed = 5
	game_exit = False
	enemy_count = 3

	# Defining Movement functions
	while not game_exit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_LEFT) or (event.key == K_a):
					x_change = -3
				elif (event.key == pygame.K_RIGHT) or (event.key == K_d):
					x_change = 3
				elif (event.key == pygame.K_UP) or (event.key == K_w):
					y_change = -3
				elif (event.key == pygame.K_DOWN) or (event.key == K_s):
					y_change = 3
				elif (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_x):
					pygame.quit()
					sys.exit()
				elif (event.key == pygame.K_LEFT) and pygame.K_RIGHT:
					x_change = 0
				elif event.key == pygame.K_SPACE:
					bullet_s()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == K_a or event.key == K_d:
					x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == K_w or event.key == K_s:
					y_change = 0

		x += x_change
		y += y_change

		draw_enemy(enemy_start_x, enemy_start_y)
		enemy_start_y += enemy_speed
		draw_user(x, y)

		bullet_y += bullet_speed

		# if y > DISPLAY_HEIGHT:
		# 	y = 0 + PLAYER_HEIGHT
		# elif y < 0:
		# 	y = 0 - PLAYER_HEIGHT
		# if x > DISPLAY_WIDTH:
		# 	x = 0 + PLAYER_WIDTH
		# elif x < 0:
		# 	x = 0 - PLAYER_WIDTH

		if enemy_start_y > DISPLAY_HEIGHT:
			enemy_start_y = 0 - ENEMY_HEIGHT
			enemy_start_x = random.randrange(0, DISPLAY_WIDTH)

		enemy_count += 1
		if enemy_count < 10:
			enemy_count = 0
			enemies.append(pygame.Rect(enemy_start_x, enemy_start_y, 32, 32))

		if x > enemy_start_x and x < enemy_start_x + ENEMY_WIDTH or x + PLAYER_WIDTH > enemy_start_x and x + PLAYER_WIDTH < enemy_start_x + ENEMY_WIDTH:
			#print('collision x')
			if y > enemy_start_y and y < enemy_start_y + ENEMY_HEIGHT:
				#print('collision y/x')
				crash_game()

			elif y + PLAYER_HEIGHT > enemy_start_y and y + PLAYER_HEIGHT < enemy_start_y + ENEMY_HEIGHT:
			#	print('x and y collision')
				crash_game()

			elif x + PLAYER_WIDTH > enemy_start_x and x + PLAYER_WIDTH < enemy_start_x + ENEMY_WIDTH:
				crash_game()
		# Collision Detection

		#for enemy in enemies:
			#if player.colliderect(enemy):
			#	print('crossover x')

		#		crash_game()

		# Scrolling Background

		yloop = y_bg % bgImgH
		game_display.blit(bg_img, (0, yloop - bgImgH))
		if yloop < DISPLAY_HEIGHT:
			game_display.blit(bg_img, (0, yloop))
		y_bg += 4

		# pygame.Surface(Bullet, (x, y))
		game_display.blit(player_img, (x, y))

		game_display.blit(enemy_img, (enemy_start_x, enemy_start_y))

		pygame.display.update()
		pygame.display.flip()
		clock.tick(60)


intro_game()
game_loop()
pygame.quit()
quit()