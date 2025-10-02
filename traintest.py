import time
import json
from train import Train
from routes import routeA, routeB, routeC

train1 = Train("A1", routeA)
# train2 = Train("A2", routeA)
# train3 = Train("A3", routeA)

# train4 = Train("B1", routeB)
# train5 = Train("B2", routeB)

# train6 = Train("C1", routeC)

train1.start()
# train4.start()
# train6.start()
# time.sleep(20)
# train2.start()
# train5.start()
# time.sleep(20)
# train3.start()
train1.join()
# train2.join()
# train3.join()
# train4.join()
# train5.join()
# train6.join()

