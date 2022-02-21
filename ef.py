from ursina import *; from ursina.prefabs.first_person_controller import *
from perlin_noise import PerlinNoise
from random import randint,randrange
app=Ursina()
player = FirstPersonController()
Sky(texture='blue_sky')
creeper=Entity(model='cube',collider='box',texture='creeper',scale=(2,4,2),position=(5, 3, 2))
creeper.add_script(SmoothFollow(player, offset=(5,1,5)))
'''for x in range(25):
    for z in range(25):
        y = noise([x * 0.02,z * 0.02])
        y = math.floor(y * 7.5)
        ent = Entity(model='cube', texture='white_cube', color=color.white, collider='box', scale=(1, 1, 1), position=(x, y, z))'''
noise = PerlinNoise(octaves=2,seed=randrange(1, 100000000000000000000000000000000000))
amp = 6
freq = 24

shells = []
shellWidth = 12
def update():
    if player.y < -3:
        player.y = 10
    genTerr()
for i in range(shellWidth*shellWidth):
    ent = Entity(model='cube', texture='grass', collider='box')
    shells.append(ent)
def genTerr():
    global amp, freq
    for i in range(len(shells)):
        x = shells[i].x = floor((i/shellWidth) + player.x - 0.5*shellWidth)
        z = shells[i].z = floor((i%shellWidth) + player.z - 0.5*shellWidth)
        y = shells[i].y = floor(noise([x/freq, z/freq])*amp)
def input(key):
    if key=='right mouse down':
            def xi():
                destroy(e)
            e=Entity(model='cube',texture='grass',color=color.white,collider='box',scale=(1,1,1),position=(round(mouse.world_point.x),round(mouse.world_point.y),round(mouse.world_point.z)),on_click=xi)
app.run()