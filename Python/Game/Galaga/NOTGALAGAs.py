# Game oF NOTGALAGA
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# IMPORTING ALL THE LIBRARIES

import random
import sys
from tkinter import *
import pygame
import pygame.mixer
from os import path

images = path.join(path.dirname(__file__), 'images')
sounds = path.join(path.dirname(__file__), 'sound')

pygame.init()

# Setup The display
DISPLAY_WIDTH, DISPLAY_HEIGHT = 700, 1000
CENTRE_X, CENTRE_Y = DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2
pygame.display.set_caption('NOTGalaga')
clock = pygame.time.Clock()

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
bg_img = pygame.image.load(path.join(images, "bg3.png")).convert()
bg_img = pygame.transform.scale(bg_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
bg_img_w, bgImgH = game_display.get_rect().size
bg_y = 0

SPRING_GREEN = (0, 255, 127)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60
PW_T = 2000

x = DISPLAY_WIDTH / 2
y = DISPLAY_HEIGHT - 75
font = pygame.font.Font('notgalaga.ttf', 25)
score_font = pygame.font.Font('notgalaga.ttf', 25)
big_font = pygame.font.Font('notgalaga.ttf', 105)
lg_font = pygame.font.Font('notgalaga.ttf', 60)

# Importing User Spacecraft
player_img = pygame.image.load(path.join(images, "User1.png"))
player_img = pygame.transform.scale(player_img, (42, 32))
user = player_img.get_rect()

# Importing Enemies
enemy_images = []
enemy_list = ['alien1.png', 'alien2.png', 'alien3.png', 'alien4.png', 'alien5.png'
	, 'alien6.png']
for img in enemy_list:
	enemy_images.append(pygame.image.load(path.join(images, img)))

explosion_list = {}
explosion_list['bg'] = []
explosion_list['sl'] = []
for i in range(9):
	filename = 'regexplosion0{}.png'.format(i)
	img = pygame.image.load(path.join(images, filename))
	img_big = pygame.transform.scale(img, (75, 75))
	explosion_list['bg'].append(img_big)
	img_small = pygame.transform.scale(img, (32, 32))
	explosion_list['sl'].append(img_small)

# Importing Bullets
bullet_img = pygame.image.load(path.join(images, "Bullet2.png"))
bullet_img = pygame.transform.scale(bullet_img, (2, 5))

pw_img = {}
pw_img['health'] = pygame.image.load(path.join(images, 'health.png'))
pw_img['laser'] = pygame.image.load(path.join(images, 'laser.png'))


# Defining Intro Music
def intro_s():
	pygame.mixer.music.load(path.join(sounds, "tgfcoder-FrozenJam-SeamlessLoop.mp3"))
	pygame.mixer.music.play(0, 4.0)


# Defining Bullet Music
pw_s = pygame.mixer.Sound(path.join(sounds, "Powerup.wav"))
laser_s = pygame.mixer.Sound(path.join(sounds, "Laser_Shoot.wav"))
explosion_s = pygame.mixer.Sound(path.join(sounds, "Explosion.wav"))


# Defining Death Music
def new(self):
		# start a new game
	self.score = 0
	self.all_sprites = pygame.sprite.Group()
	self.user = Player(self)
	self.all_sprites.add(self.user)
	self.run()


def death_s():
	pygame.mixer.music.load(path.join(sounds, "Galaga.mp3"))
	pygame.mixer.music.play(0, 140.1)


def start_screen():
	intro = True
	background()
	intro_s()
	while intro:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			big_text = pygame.font.Font('notgalaga.ttf', 62)
			text_surf, text_rect = text_objects("WELCOME TO NOTGALAGA", big_text)
			text_rect.center = (CENTRE_X, CENTRE_Y - 400)
			game_display.blit(text_surf, text_rect)

			small_text = pygame.font.Font('notgalaga.ttf', 39)
			text_surf1, text_rect1 = text_objects("- Press Space to Start -", small_text)
			text_rect1.center = (CENTRE_X, CENTRE_Y - 100)
			game_display.blit(text_surf1, text_rect1)

			big_text = pygame.font.Font('notgalaga.ttf', 50)
			text_surf2, text_rect2 = text_objects("< CONTROLS | INFO >", small_text)
			text_rect2.center = (CENTRE_X, CENTRE_Y + 100)
			game_display.blit(text_surf2, text_rect2)

			small_text = pygame.font.Font('notgalaga.ttf', 20)
			text_surf3, text_rect3 = text_objects("* Press Space to Fire *", small_text)
			text_rect3.center = (CENTRE_X - 200, CENTRE_Y + 200)
			game_display.blit(text_surf3, text_rect3)

			small_text = pygame.font.Font('notgalaga.ttf', 20)
			text_surf3, text_rect3 = text_objects("* Arrow keys to move *", small_text)
			text_rect3.center = (CENTRE_X - 200, CENTRE_Y + 300)
			game_display.blit(text_surf3, text_rect3)

			# text = score_font.render("HighScore: " + str(high_score()), True, WHITE)
			# game_display.blit(text, [250, 0])

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					intro = False
					# game_loop()
				elif (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_x):
					pygame.quit()
					sys.exit()

			pygame.display.update()


def background():
	y_bg = 0
	yloop = y_bg % bgImgH
	game_display.blit(bg_img, (0, yloop - bgImgH))
	if yloop < DISPLAY_HEIGHT:
		game_display.blit(bg_img, (0, yloop))
	y_bg += 4
	pygame.display.update()
	pygame.display.flip()


def message_display():
	game_display.fill(BLACK)
	death = True
	death_s()
	while death:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			big_text = pygame.font.Font('notgalaga.ttf', 105)
			text_surf, text_rect = text_objects('-+ YOU DEAD +-', big_text)
			text_rect.center = (CENTRE_X, CENTRE_Y - 100)
			game_display.blit(text_surf, text_rect)

			small_text = pygame.font.Font('notgalaga.ttf', 39)
			text_surf1, text_rect1 = text_objects("- Press R to Reload -", small_text)
			text_rect1.center = (CENTRE_X, CENTRE_Y + 200)
			game_display.blit(text_surf1, text_rect1)

			# text = lg_font.render("HighScore: " + str(()), True, WHITE)
			# game_display.blit(text, [125, 50])

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					start_screen()
				elif (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_x):
					pygame.quit()
					sys.exit()
			pygame.display.update()


def health_bar(surf, x, y, phb):
	if phb < 0:
		phb = 0
	bar_length = 100
	bar_width = 8
	fill = (phb / 100) * bar_length
	outline_rect = pygame.Rect(x, y, bar_length, bar_width)
	fill_rect = pygame.Rect(x, y, fill, bar_width)
	pygame.draw.rect(surf, GREEN, fill_rect)
	pygame.draw.rect(surf, WHITE, outline_rect, 1)


def score(score):
	text = score_font.render("Score: " + str(score), True, WHITE)
	game_display.blit(text, [300, 0])


# Defining User Spacecraft

def addenemy():
	e = Enemy()
	all_sprites.add(e)
	enemy.add(e)


class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 40))
		self.image = player_img
		self.rect = self.image.get_rect()
		self.radius = 21
		# pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
		self.rect.centerx = DISPLAY_WIDTH / 2
		self.rect.bottom = DISPLAY_HEIGHT - 75
		self.speedx = 0
		self.speedy = 0
		self.fire_delay = 150
		self.last_shot = pygame.time.get_ticks()
		self.health = 100
		self.pw = 1
		self.pw_t = pygame.time.get_ticks()

	def update(self):
		self.speedx = 0
		self.speedy = 0
		keypressed = pygame.key.get_pressed()
		if keypressed[pygame.K_LEFT]:
			self.speedx = -3
		if keypressed[pygame.K_RIGHT]:
			self.speedx = 3
		if keypressed[pygame.K_UP]:
			self.speedy = -3
		if keypressed[pygame.K_DOWN]:
			self.speedy = 3
		if keypressed[pygame.K_SPACE]:
			self.fire()
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.right > DISPLAY_WIDTH:
			self.rect.right = DISPLAY_WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > DISPLAY_HEIGHT:
			self.rect.bottom = DISPLAY_HEIGHT

		if self.pw >= 2 and pygame.time.get_ticks() - self.pw_t > PW_T:
			self.pw -= 1
			self.pw_t = pygame.time.get_ticks()

	def pwup(self):
		self.pw += 1
		self.pw_t = pygame.time.get_ticks()

	def fire(self):
		hold = pygame.time.get_ticks()
		if hold - self.last_shot > self.fire_delay:
			self.last_shot = hold
			if self.pw == 1:
				bullet = Bullet(self.rect.centerx, self.rect.top)
				all_sprites.add(bullet)
				bullets.add(bullet)
				laser_s.play()
			if self.pw >= 2:
				bt0 = Bullet(self.rect.left, self.rect.centery)
				bt1 = Bullet(self.rect.centerx, self.rect.top)
				bt2 = Bullet(self.rect.right, self.rect.centery)
				all_sprites.add(bt0)
				all_sprites.add(bt1)
				all_sprites.add(bt2)
				bullets.add(bt0)
				bullets.add(bt1)
				bullets.add(bt2)
				laser_s.play()


class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image_orig = random.choice(enemy_images)
		self.image = self.image_orig.copy()
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.width * 0.87 / 2)
		# pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
		self.rect.x = random.randrange(DISPLAY_WIDTH - self.rect.width)
		self.rect.y = random.randrange(-300, -100)
		self.speedy = +random.randint(3, 10)
		self.speedx = +random.randint(-2, 2)
		self.health = 50

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > DISPLAY_HEIGHT + 20 or self.rect.left < -35 or self.rect.right > DISPLAY_WIDTH + 30:
			self.rect.x = random.randrange(DISPLAY_WIDTH - self.rect.width)
			self.rect.y = random.randrange(-300, -50)
			self.speedy = random.randrange(1, 6)
			self.blast()
			pygame.display.update()

	def blast(self):
		blasted = Blasts(self.rect.x, self.rect.y)
		all_sprites.add(blasted)
		blasts.add(blasted)
		pygame.display.update()


class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((2, 1))
		# self.image.fill(BLUE)
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		# kill if it moves out of the top frame
		if self.rect.bottom < 0:
			self.kill()


# def username():
# 	def callback(event):
# 		return e1
# 	windows = Tk()
# 	windows.geometry("300x50")
# 	windows.title("Name input")
# 	lb1 = Label(windows, text="Enter Name: ")
# 	lb1.pack(side=TOP)
# 	e1 = Entry(windows, bd=5)
# 	e1.bind("<Return>", callback)
# 	e1.pack(side=TOP)
# 	windows.mainloop()



class Powerup(pygame.sprite.Sprite):
	def __init__(self, center):
		pygame.sprite.Sprite.__init__(self)
		self.type = random.choice(['health', 'laser'])
		self.image = pw_img[self.type]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.speedy = 5

	def update(self):
		self.rect.y += self.speedy
		# kill if it moves out of the top frame
		if self.rect.top > DISPLAY_HEIGHT:
			self.kill()


class Blasts(pygame.sprite.Sprite):
	def __init__(self, xx, yy):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((3, 2))
		self.image.fill(CYAN)
		self.rect = self.image.get_rect()
		self.rect.bottom = yy
		self.rect.centerx = xx
		self.speedy = +8

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom > DISPLAY_HEIGHT:
			self.kill()


class Explosion(pygame.sprite.Sprite):
	def __init__(self, center, size):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.image = explosion_list[self.size][0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 30

	def update(self):
		time = pygame.time.get_ticks()
		if time - self.last_update > self.frame_rate:
			self.last_update = time
			self.frame += 1
			if self.frame == len(explosion_list[self.size]):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_list[self.size][self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center





def text_objects(text, font):
	text_surface = font.render(text, True, WHITE)
	return text_surface, text_surface.get_rect()


def crash_game():
	message_display()


# def game_loop():
game_over = True
working = True
y_bg = 0
current_Score = 0
while working:
	if game_over:
		start_screen()
		game_over = False
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		enemy = pygame.sprite.Group()
		pwup = pygame.sprite.Group()
		blasts = pygame.sprite.Group()
		user = Player()
		all_sprites.add(user)
		for i in range(50):
			addenemy()
		user.health = 100
		current_Score = 0
		enemy.health = 50
		# score = 0
		# y_bg = 0
	clock.tick(FPS)

	# keep loop running at the right speed
	# Process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			working = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

	all_sprites.update()

	collisions = pygame.sprite.groupcollide(enemy, bullets, True, True)
	for collision in collisions:
		enemy.health -= 10
		e = Enemy()
		explosion_s.play()
		expl = Explosion(collision.rect.center, 'bg')
		if random.random() > 0.92:
			pw = Powerup(collision.rect.center)
			all_sprites.add(pw)
			pwup.add(pw)
		all_sprites.add(expl)
		current_Score += 60 - collision.radius
		all_sprites.add(e)
		enemy.add(e)

	collisions = pygame.sprite.spritecollide(user, pwup, True)
	for collision in collisions:
		pw_s.play()
		if collision.type == 'health':
			user.health += random.randrange(5, 50)
			if user.health >= 100:
				user.health = 100
		elif collision.type == 'laser':
			user.pwup()

	collisions = pygame.sprite.spritecollide(user, blasts, True)
	for collision in collisions:
		user.health -= 8
		expl = Explosion(collision.rect.center, 'sl')
		all_sprites.add(expl)
		addenemy()
		if user.health <= 0:
			all_sprites.empty()
			game_over = True
			highscore = 0
			f = open("Scores.txt", 'a')
			#name = input("Input your name: ")
			def username():
				def callback(event):
					return e1

				windows = Tk()
				windows.geometry("300x50")
				windows.title("Name input")
				lb1 = Label(windows, text="Enter Name: ")
				lb1.pack(side=TOP)
				e1 = Entry(windows, bd=5)
				e1.bind("<Return>", callback)
				e1.pack(side=TOP)
				windows.mainloop()
			name = username()
			if current_Score > highscore:
				highscore = current_Score
				f.write(str(name) + " | " + str(highscore))
				f.write("\n")
				f.close()

			# crash_game()

	# check to see if an enemy collides with player
	collisions = pygame.sprite.spritecollide(user, enemy, True, pygame.sprite.collide_circle)
	for collision in collisions:
		user.health -= collision.radius * 1.5
		expl = Explosion(collision.rect.center, 'sl')
		all_sprites.add(expl)
		addenemy()
		if user.health <= 0:
			all_sprites.empty()
			game_over = True
			highscore = 0
			f = open("Scores.txt", 'a')
			#name = input("Input your name: ")
			def username():
				def callback(event):
					return e1

				windows = Tk()
				windows.geometry("300x50")
				windows.title("Name input")
				lb1 = Label(windows, text="Enter Name: ")
				lb1.pack(side=TOP)
				e1 = Entry(windows, bd=5)
				e1.bind("<Return>", callback)
				e1.pack(side=TOP)
				windows.mainloop()
			name = username()
			if current_Score > highscore:
				highscore = current_Score
				f.write(str(name) + " | " + str(highscore))
				f.write("\n")
				f.close()

			# crash_game()

	yloop = y_bg % bgImgH
	game_display.blit(bg_img, (0, yloop - bgImgH))
	if yloop < DISPLAY_HEIGHT:
		game_display.blit(bg_img, (0, yloop))
	y_bg += 4

	all_sprites.draw(game_display)
	score(current_Score)
	health_bar(game_display, 5, 980, user.health)

	pygame.display.update()
	pygame.display.flip()

pygame.quit()
quit()
