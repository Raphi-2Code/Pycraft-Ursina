from perlin_noise import PerlinNoise
from ursina import Entity, color, Vec3, destroy
from random import randrange
from ursina import *
Log = 'log.png'
leaves = 'leaves.png'
GrassModel = 'GrassCube.obj'
class Trees:
    def __init__(this):
        this.noise = PerlinNoise(seed=4)

    def checkTree(this, _x,_y,_z):
        freq = 5
        amp = 100
        treeChance = ((this.noise([_x/freq,_z/freq]))*amp)
        if treeChance > 20:
            this.plantTree(_x,_y,_z)

    def plantTree(this,_x,_y,_z):
        tree = Entity(  model = None,
                        position=Vec3(_x,_y,_z))
        global trunk
        trunk = Entity( model=GrassModel,texture=Log,scale_y = randrange(5, 10),collider='mesh')
        crown = Entity( model='cube',scale=8,y=trunk.y+trunk.scale_y,texture=leaves,collider='cube')
        crown.parent=tree
        trunk.parent=tree
        tree.y = 3