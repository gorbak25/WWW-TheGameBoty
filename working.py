import conversation as c
import settings as s
import time
import math

tracing = True 		#are we tracing our target
aim = True			#are we aiming for our target
shoot = False		#are we shooting
follow = False		#are we following our target
stand = True		#are we trying to stand still
targeting = True	#are we calculating who is our target

spread = True	#do we need to be exact with our aim
spr = 10		#the allowed angle spread for shooting
delay = 0.01	#the main loop delay

des_angle = 0	#the desired angle to aim
agression = 10	#the aggresion of chasing our oponent
focus = 0		#what we are focusing

#maxVel = 10

x = c.Conversation()
x.hello()

class Velocity(object):
    dx = None
    dy = None

def PrintPlayer(p):
    print p.x
    print p.y
    print p.angle 
    print p.hp
    print p.ammo
    print p.reloading
    print p.alive
    print p.shot
    print p.full
    print p.player_nr

def Decide(X,V,D):
    if X>=0:
        if V<=0:
            if V==(-D):
                if X<=D*D:
                    return -1
                else:
                    return 1
            if V>-D:
                if X<D*D:
                    return -1
                else:
                    return 1
            else:
                return -1
        else:
            return 1
    else:
        if V>=0:
            if V==D:
                if (-X)<=D*D:
                    return 1
                else:
                    return -1
            if V<D:
                if (-X)<=D*D:
                    return 1
                else:
                    return -1
            else:
                return 1
        else:
            return -1

while 1==1:
    prev_players = x.get_players()
    if prev_players!=None:
        break
    
numOfPlayers = len(prev_players)

velocity = range(numOfPlayers);

for i in range(numOfPlayers):
    velocity[i] = Velocity()

while 1==1:
	players = None
	
	while players==None:
		players = x.get_players()
	
	for i in range(numOfPlayers):
		velocity[i].dx = (players[i].x - prev_players[i].x)#*s.FPS
		velocity[i].dy = (players[i].y - prev_players[i].y)#*s.FPS
	
	bot = players[s.MY_NR]
	bot_vel = velocity[s.MY_NR]
		
	if targeting:
		best_id = 0
		best_val = 4*s.MAP_SIZE*s.MAP_SIZE
		for i in range(numOfPlayers):
			if i!=s.MY_NR:
				pla = players[i]
				cur_val = (pla.x-bot.x)*(pla.x-bot.x) + (pla.y-bot.y)*(pla.y-bot.y)
				if cur_val < best_val:
					best_val = cur_val
					best_id = i
		focus = best_id
	
	enemy = players[focus]
	enemy_vel = velocity[focus]
	
	if stand:
		if bot_vel.dx>0:
			k = x.move("LEFT")
			print "LEFT"
			x.send_command(k)
		if bot_vel.dx<0:
			k = x.move("RIGHT")
			print "RIGHT"
			x.send_command(k)
		else:
			print "NONE"
		
		if bot_vel.dy>0:
			k = x.move("UP")
			print "UP"
			x.send_command(k)
		if bot_vel.dy<0:
			k = x.move("DOWN")
			print "DOWN"
			x.send_command(k)
		else:
			print "NONE"
	
	if tracing:
		#des_angle = math.atan2(enemy.y-bot.y, enemy.x-bot.x)
		
		des_angle = 2*math.atan2(-math.sqrt(enemy.x*enemy.x*s.BULLET_SPEED*s.BULLET_SPEED-enemy.x*enemy.x*enemy_vel.dy*enemy_vel.dy+2*enemy.x*enemy_vel.dx*enemy.y*enemy_vel.dy-enemy_vel.dx*enemy_vel.dx*enemy.y*enemy.y+s.BULLET_SPEED*s.BULLET_SPEED*enemy.y*enemy.y)-enemy.x*s.BULLET_SPEED,-enemy.x*enemy_vel.dy+enemy_vel.dx*enemy.y+s.BULLET_SPEED*D)
		
	if aim:
		shoot = false
		if math.abs(des_angle-bot.angle)<=spr:
			shoot = true
			
		if des_angle>bot.angle:
			k = x.rot("LEFT")
			print "ROT-LEFT"
			x.send_command(k)
			
		if des_angle<bot.angle:
			k = x.rot("RIGHT")
			print "ROT-RIGHT"
			x.send_command(k)
			
		else:
			shoot = true
	
	if follow:
		DX = enemy.x - bot.x
		DY = enemy.y - bot.y
		DV = Velocity()
		DV.dx = enemy_vel.dx - bot_vel.dx
		DV.dy = enemy_vel.dy - bot_vel.dy
	
		r = Decide(DY, DV.dy, agression)
		if r==1:
			k = x.move("DOWN")
			print "DOWN"
			x.send_command(k)
		if r==-1:
			k = x.move("UP")
			print "UP"
			x.send_command(k)
	
		r = Decide(DX, DV.dx, agression)
		if r==1:
			k = x.move("RIGHT")
			print "RIGHT"
			x.send_command(k)
		if r==-1:
			k = x.move("LEFT")
			print "LEFT"
			x.send_command(k)
	
	print "\n"
	
	if shoot:
		k = x.shoot()
		x.send_command(k)
	
	prev_players = players
	time.sleep(delay)
	

