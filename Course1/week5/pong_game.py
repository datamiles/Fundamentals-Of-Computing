# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [0,0]
paddle1_vel = 0
paddle2_pos = [WIDTH-PAD_WIDTH, 0]
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    #print ball_pos
    if (direction == "right"):
        
        h = (random.randrange(120, 240))/60.0
        v = (random.randrange(60, 180))/60.0
        v = -v
        ball_vel = [h, v]
        #print h,v

    if (direction == "left"):
        h = (random.randrange(120, 240))/60.0
        v = (random.randrange(60, 180))/60.0
        h = -h
        v = -v
        ball_vel = [h, v]
        #print h,v
    #print direction

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    score1 = 0
    score2 = 0
    d = ['right', 'left']
    direction = random.choice(d)
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    #print "paddle 1 pos " + str(paddle1_pos[0]) + " " + str(paddle1_pos[1])
    #midofpaddle1 = paddle1_pos[1] + HALF_PAD_HEIGHT
    #print "mid of paddle1" +str(midofpaddle1)
    
    # bounce off left
    if(ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        topOfPedal1 = paddle1_pos[1]
        bottomOfPedal1 = paddle1_pos[1] + PAD_HEIGHT
        if (topOfPedal1 <= ball_pos[1] <= bottomOfPedal1): 
            ball_vel[0] = - ball_vel[0]
        else:
            score2 += 1
            spawn_ball('right')
    
    # bounce off right
    if (ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH):
        topOfPedal2 = paddle2_pos[1]
        bottomOfPedal2 = paddle2_pos[1] + PAD_HEIGHT
        if (topOfPedal2 <= ball_pos[1] <= bottomOfPedal2): 
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball('left')
    
    # bounce off top
    if (ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # bounce off bottom
    if (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen

    #print paddle1_pos[1]
    #print "vel is " + str(paddle1_vel)
    
    if (paddle1_vel > 0):
        if (paddle1_pos[1] <= HEIGHT - PAD_HEIGHT):
            paddle1_pos[1] += paddle1_vel
    if (paddle1_vel < 0):
        if (paddle1_pos[1] >= 1):
            paddle1_pos[1] += paddle1_vel
            
    if (paddle2_vel > 0):
        if (paddle2_pos[1] <= HEIGHT - PAD_HEIGHT):
            paddle2_pos[1] += paddle2_vel
    if (paddle2_vel < 0):
        if (paddle2_pos[1] >= 1):
            paddle2_pos[1] += paddle2_vel

        
    
    # draw paddles
    a = paddle1_pos[0]
    b = paddle1_pos[1]
    c = paddle2_pos[0]
    d = paddle2_pos[1]
    canvas.draw_polygon([(a, b), (a, b + PAD_HEIGHT), (a + PAD_WIDTH, b + PAD_HEIGHT), (a + PAD_WIDTH, b)], 2, "Red","Fuchsia")
    canvas.draw_polygon([(c, d), (c, d + PAD_HEIGHT), (c + PAD_WIDTH, d + PAD_HEIGHT), (c + PAD_WIDTH, d)], 2, "Red","Fuchsia")
        
    # determine whether paddle and ball collide    


    
    # draw scores
    canvas.draw_text(str(score1), (150, 50), 40, 'Yellow')
    canvas.draw_text(str(score2), (425, 50), 40, 'Yellow')
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 2
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", button_handler, 80)


# start frame
new_game()
frame.start()
