import os
class Player:
    quality = 'extra choice'
    q1= '360p'
    q2 = '480p'
    q3 = '720p'
    q4 = '1080p'
    playing = True

    def play(self):
        print('Write address')
        address = input()
        if os.path.exists(address):
            self.playing = True
        else:
            self.playing = False
        return self.playing
    @property
    def change_quality(self):
        print('Choose number of quality \n1.360p \n2.480p \n3.720p \n4.1080p')
        q = int(input())
        if q == 1:
            self.quality = self.q1
        if q == 2:
            self.quality = self.q2
        if q == 3:
            self.quality = self.q3
        if q == 4:
            self.quality = self.q4
        return self.quality