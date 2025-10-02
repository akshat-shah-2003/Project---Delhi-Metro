import time
import threading
import numpy as np

class Train(threading.Thread):
    def __init__(self, train_id, route):
        super().__init__()
        self.train_id = train_id
        self.route = route
        self.current_idx = 0
        self.position = route[0]['coords']
        self.active = True

    def interpolate_points(self, start, end, steps):
        lat = np.linspace(start[0], end[0], steps)
        lon = np.linspace(start[1], end[1], steps)
        return list(zip(lat, lon))
    
    def run(self):
        for i in range(len(self.route) - 1):
            print(f"Train {self.train_id} has departed from {self.route[i]['name']} to {self.route[i+1]['name']}.")
            start = self.route[i]['coords']
            end = self.route[i+1]['coords']
            duration = self.route[i]['duration_to_next']

            steps = duration//20
            points = self.interpolate_points(start, end, steps)

            for point in points:
                if not self.active:
                    break
                #self.position = point
                self.position = float(point[0]), float(point[1])
                print(f"Train {self.train_id} is at position {self.position}.")
                time.sleep(1)

            if self.active:
                print(f"Train {self.train_id} arrived/waiting at {self.route[i+1]['name']}.")
                time.sleep(5)
        
        self.active = False
        print(f"Train {self.train_id} has completed its route.")



