from object import *
from cmu_graphics import *
import world



def main():
    runApp(app)

def redrawAll(app):
    coin = Coin(app, 5, 6)
    world.drawCollectible(coin.x, coin.y, coin.width, coin.height, coin.color)
main()
