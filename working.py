import conversation as c
import settings as s
import time
import math

tracing = True 		#are we tracing our target
aim = True			#are we aiming for our target
shoot = True		#are we shooting
follow = False		#are we following our target
stand = True		#are we trying to stand still
targeting = True	#are we calculating who is our target

spread = True			#do we need to be exact with our aim
spr = 10000/180*math.pi	#the allowed angle spread for shooting
delay = 0.02			#the main loop delay

sprey = 1
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
    
#def ComparePlayers(a, b, numOfPlayers):
#	good = True
#	for i in range(numOfPlayers):
#		if not( b[i].y==a[i].x and b[i].angle==a[i].y and b[i].hp==a[i].hp and b[i].ammo==a[i].ammo and b[i].reloading==a[i].reloading and b[i].alive==a[i].alive and b[i].shot==a[i].shot and b[i].full==a[i].full and b[i].player_nr==a[i].player_nr):
#			good = False
#		PrintPlayer(a[i])
#		print "---"
#		PrintPlayer(b[i])
#		print "\n"
#	print good
#	return good

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
	
	commands = 0
	
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
				#print cur_val
				if cur_val < best_val:
					best_val = cur_val
					best_id = i
		focus = best_id
		#print best_val
		#print focus
	
	enemy = players[focus]
	enemy_vel = velocity[focus]
	
	if stand:
		if bot_vel.dx<0:
			commands |= x.move("RIGHT")
			print "RIGHT"
		if bot_vel.dx>0:
			commands |= x.move("LEFT")
			print "LEFT" 
		
		if bot_vel.dy<0:
			commands |= x.move("DOWN")
			print "DOWN"
		if bot_vel.dy>0:
			commands |= x.move("UP")
			print "UP"
	
	if tracing:
		#enemy.x = 0
		#enemy.y = 0
		dx = enemy.x - bot.x 
		dy = bot.y - enemy.y 
		
		#des_angle1 = math.asin(dy/math.sqrt(dx*dx+dy*dy))
		#des_angle2 = math.acos(dx/math.sqrt(dx*dx+dy*dy))
		
		#if des_angle1 < 0:
		#	des_angle1 = 2*math.pi + des_angle1
		
		#if des_angle2 < 0:
		#	des_angle2 = 2*math.pi + des_angle2
		
		des_angle = math.atan2(dy,dx)
		if des_angle < 0:
			des_angle = 2*math.pi + des_angle
		
		#if des_angle != des_angle1:
		#	des_angle += math.pi
		
		#print des_angle1
		#print des_angle2
		
		#enemy.x = 0
		#enemy_vel.dx = 0
		#enemy_vel.dy = 0
		#enemy.y = 0
		
		#enemy.x -= bot.x
		#enemy.y -= bot.y
		
#		try:
#			des_angle = math.pi+(2*math.atan2(-math.sqrt(enemy.x*enemy.x*s.BULLET_SPEED*s.BULLET_SPEED-enemy.x*enemy.x*enemy_vel.dy*enemy_vel.dy+2*enemy.x*enemy_vel.dx*enemy.y*enemy_vel.dy-enemy_vel.dx*enemy_vel.dx*enemy.y*enemy.y+s.BULLET_SPEED*s.BULLET_SPEED*enemy.y*enemy.y)-enemy.x*s.BULLET_SPEED,-enemy.x*enemy_vel.dy+enemy_vel.dx*enemy.y+s.BULLET_SPEED*enemy.y))
#		except ValueError:
#			print "WTF"
	if aim:
		shoot = False
		
		print "----------"
		print des_angle
		print bot.angle
		print "----------"
		if abs(des_angle-bot.angle)<=spr:
			shoot = True
			
		if des_angle>bot.angle:
			print "ROT-LEFT"
			commands |= x.rot("LEFT")
			
		if des_angle<bot.angle:
			print "ROT-RIGHT"
			commands |= x.rot("RIGHT")
			
		else:
			shoot = True
	
	if follow:
		DX = enemy.x - bot.x
		DY = enemy.y - bot.y
		DV = Velocity()
		DV.dx = enemy_vel.dx - bot_vel.dx
		DV.dy = enemy_vel.dy - bot_vel.dy
	
		r = Decide(DY, DV.dy, agression)
		if r==1:
			commands |= x.move("DOWN")
			#print "DOWN"
		if r==-1:
			commands |= x.move("UP")
			#print "UP"
	
		r = Decide(DX, DV.dx, agression)
		if r==1:
			commands |= x.move("RIGHT")
			#print "RIGHT"
		if r==-1:
			commands |= x.move("LEFT")
			#print "LEFT"
	
	if shoot:
		commands |= x.shoot()
	
	print "\n"
	#print commands
	
	x.send_command(commands)
	
	prev_players = players
	time.sleep(delay)
	
def PickTarget(Players, Velocity, ownPlayerNumber):
    RelativeVelocity = Velocity
    Distance = Velocity
    PlayerToKill = []

    DistanceWeight = -0.8
    RelativeSpeedWeightX =  -0.5
    RelativeSpeedWeightY =  -0.5

    for i in range (len(Velocity)):
        if i != ownPlayerNumber:
            RelativeVelocity[i].dx -= Velocity[ownPlayerNumber].dx
            RelativeVelocity[i].dy -= Velocity[ownPlayerNumber].dy

    for i in range (len(Players)):
        if i != ownPlayerNumber:
            Distance[i] = math.sqrt(sqrtmath.pow(Players[i].x - Players[ownPlayerNumber].x, 2) + math.pow(Players[i].y - Players[ownPlayerNumber].y, 2))

    for i in range(len(Players)):
        if i != ownPlayerNumber:
            PlayerToKill.append([i, Distance[i] * DistanceWeight + RelativeVelocity[i].dx * RelativeSpeedWeightX + RelativeVelocity[i].dy * RelativeSpeedWeightY])

    MaxValue = -10000000.0;
    ChosenPlayer = 0;

    for i in range(len(PlayerToKill)):
        if PlayerToKill[i][1] > MaxValue:
            ChosenPlayer = i
            MaxValue = PlayerToKill[i]

    return ChosenPlayer
