import time
import threading
import numpy as np

def interpolate_points(start, end, steps):
    lat = np.linspace(start[0], end[0], steps)
    lon = np.linspace(start[1], end[1], steps)
    return list(zip(lat, lon))

class Train(threading.Thread):
    def __init__(self, train_id, route):
        super().__init__()
        self.train_id = train_id
        self.route = route
        self.current_idx = 0
        self.position = route[0]['coords']
        self.active = True
    
    def run(self):
        for i in range(len(self.route) - 1):
            start = self.route[i]['coords']
            end = self.route[i+1]['coords']
            duration = self.route[i]['duration_to_next']

            steps = duration
            points = interpolate_points(start, end, steps)

            for point in points:
                if not self.active:
                    break
                self.position = point
                time.sleep(1)
        
        self.active = False
        print(f"Train {self.train_id} has completed its route.")



