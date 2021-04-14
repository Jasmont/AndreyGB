import time


class TrafficLight:
    __color = None

    def __init__(self):
        print('Traffic light deploy!')

    def running(self):
        while True:
            print(f'Traffic light is red!')
            time.sleep(7)
            print('Traffic light is yellow!')
            time.sleep(2)
            print('Traffic light is green!')
            time.sleep(12)


if __name__ == '__main__':
    tl = TrafficLight()

    tl.running()
