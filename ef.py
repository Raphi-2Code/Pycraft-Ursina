from ursina import *; from ursina.prefabs.first_person_controller import *
from perlin_noise import PerlinNoise
from random import randint,randrange
window.show_ursina_splash = True
app=Ursina()
player = FirstPersonController()
indra=Sky(texture='blue_sky')
abc=3
def destroy_creeper():
    global abc, lives
    abc=abc-1
    if abc==0:
        creeper.color=color.clear
        creeper.collider=None
        #lives=20
        creeper.add_script(SmoothFollow(player,offset=[10,10000000,10]))
        Text('Tasty creeper:)')
creeper=Entity(model='cube',collider='box',texture='creeper',scale=(2,4,2),position=(3, 1, 3),rotation_y=45,on_click=destroy_creeper)
creeper.add_script(SmoothFollow(player, offset=(1, 1, 1), speed=1))


'''for x in range(25):
    for z in range(25):
        y = noise([x * 0.02,z * 0.02])
        y = math.floor(y * 7.5)
        ent = Entity(model='cube', texture='white_cube', color=color.white, collider='box', scale=(1, 1, 1), position=(x, y, z))'''
noise = PerlinNoise(octaves=2,seed=randrange(1, 100000000000000000000000000000000000))
amp = 6
freq = 24
lives=20
shells = []
shellWidth = 12
heartlives=1
def update():
    global heartlives
    global lives
    heartlives=lives/2
    if player.y < -3:
        player.y = 10
    genTerr()
    if distance(creeper, player) < 7:
        lives = lives - 1
        print('lives-1')
        if lives == 0:
            Text('You died!!!', background=True)
            creeper.color=color.clear
            creeper.collider=None
            player.speed=0
            player.gravity=0
            mouse.enabled = False
            mouse.locked = False
            indra.texture="red_sky"
            indra.color=color.red
        creeper.z-=7
    textf=str("♥")*int(round(heartlives))
    texti=Text(text=textf,x=.11,y=-.11)
    texti.font="SegoeUI.ttf"
    if int(round(heartlives))==10:
        texti.text=dedent("<red>♥♥♥♥♥♥♥♥♥♥<default><orange>/<default>")
    if int(round(heartlives))==9:
        texti.text=dedent("<red>♥♥♥♥♥♥♥♥♥<default><orange>/<default>    ")
    if int(round(heartlives))==8:
        texti.text=dedent("<red>♥♥♥♥♥♥♥♥<default><orange>/<default>     ")
    if int(round(heartlives))==7:
        texti.text=dedent("<red>♥♥♥♥♥♥♥<default><orange>/<default>      ")
    if int(round(heartlives))==6:
        texti.text=dedent("<red>♥♥♥♥♥♥<default><orange>/<default>           ")
    if int(round(heartlives))==5:
        texti.text=dedent("<red>♥♥♥♥♥<default><orange>/<default>             ")
    if int(round(heartlives))==4:
        texti.text=dedent("<red>♥♥♥♥<default><orange>/<default>               ")
    if int(round(heartlives))==3:
        texti.text=dedent("<red>♥♥♥<default><orange>/<default>                 ")
    if int(round(heartlives))==2:
        texti.text=dedent("<red>♥♥<default><orange>/<default>                   ")
    if int(round(heartlives))==1:
        texti.text=dedent("<red>♥<default><orange>/<default>                     ")
    if int(round(heartlives))==0:
        texti.text=dedent("<orange>/<default>\n♡♡♡♡♡♡♡♡♡♡")
        texti.background=True
    '''
    if int(round(heartlives))==10:
        Text("♥♥♥♥♥♥♥♥♥♥",x=.11)
    if int(round(heartlives))==9:
        Text("♥♥♥♥♥♥♥♥♥♡",x=.11, y=.13)
    if int(round(heartlives))==8:
        Text("♥♥♥♥♥♥♥♥♡♡",x=.11, y=.26)
    if int(round(heartlives))==7:
        Text("♥♥♥♥♥♥♥♡♡♡",x=.11, y=.52)
    if int(round(heartlives))==6:
        Text("♥♥♥♥♥♥♡♡♡♡",x=.11, y=.104)
    if int(round(heartlives))==5:
        Text("♥♥♥♥♥♡♡♡♡♡",x=.11, y=.208)
    if int(round(heartlives))==4:
        Text("♥♥♥♥♡♡♡♡♡♡",x=.26)
    if int(round(heartlives))==3:
        Text("♥♥♥♡♡♡♡♡♡♡",x=.52)
    if int(round(heartlives))==2:
        Text("♥♥♡♡♡♡♡♡♡♡",x=.104)
    if int(round(heartlives))==1:
        Text("♥♡♡♡♡♡♡♡♡♡",x=.208)
    if int(round(heartlives))==0:
        Text("♡♡♡♡♡♡♡♡♡♡",x=.416)'''

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
            e=Entity(model='cube',texture='grass',color=color.white,collider='box',scale=(1,1,1),position=(round(mouse.world_point.x),round(1+floor(mouse.world_point.y)),round(mouse.world_point.z)),on_click=xi)
app.run()
