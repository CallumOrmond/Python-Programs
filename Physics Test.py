import pygame, sys, pymunk

#creating body
def create_obj(space):
	body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)#mass inetia, type
	body.position = (400, 0)
	shape = pymunk.Circle(body, 80) 
	space.add(body,shape)
	return shape 

#redering body
def draw_obj(obj):
	for obj in objs:
		pos_x = int(obj.body.position.x)
		pos_y = int(obj.body.position.y)
		pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y),80)
		

#create circle 
#doesnt move
def static_ball(space):
	body = pymunk.Body(body_type=pymunk.Body.STATIC)
	body.position = (500,500)
	shape = pymunk.Circle(body, 50)
	space.add(body,shape)
	return shape 

#render staitc ball
def draw_static_ball(space):
	for ball in balls:
		pos_x = int(ball.body.position.x)
		pos_y = int(ball.body.position.y)
		pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y),50)


pygame.init() #initiating game
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()

#gravity in space 
space.gravity = (0,300) # x and y gravity


objs = []
objs.append(create_obj(space))

balls = []
balls.append(static_ball(space))

#game loop
while True:
	for event in pygame.event.get():
	 	if event.type == pygame.QUIT:
	 		pygame.quit()
	 	# 	sys.exit()


	screen.fill((217,217,217))
	draw_obj(objs)
	draw_static_ball(balls)
	space.step(1/50)
	pygame.display.update() #render the game
	clock.tick(120)         #fps = 120



