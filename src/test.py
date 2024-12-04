from Collectible import *
from cmu_graphics import *
import world
import main2



def main():
    runApp(app)

def redrawAll(app):
    coin = Coin(app, 5, 6)
    world.drawCollectible(coin.x, coin.y, coin.width, coin.height, coin.color)

def onKeyPress(app, key):
    if key == 'a':
        for i in range(10):
            main2.updateWorld(app)

main()
