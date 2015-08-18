
# coding: utf-8

# In[35]:

import conversation as c
import time

x = c.Conversation()
x.hello()


# In[36]:

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


# In[ ]:

while 1==1:
    for i in range(3):
        k = x.shoot()
        x.send_command(k)
        k = x.rot("RIGHT")
        x.send_command(k)
    time.sleep(0.002)


# In[48]:

PrintPlayer(x.get_players()[0])


# In[10]:




# In[ ]:




# In[ ]:




# In[ ]:



