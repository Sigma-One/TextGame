import sys
import os

sys.stdout = open(os.devnull, 'w')

import levels.spawnArea
spawn = levels.spawnArea.main()
import levels.backYard
backyard = levels.backYard.main()
import levels.livingRoom
livingroom = levels.livingRoom.main()

sys.stdout = sys.__stdout__
