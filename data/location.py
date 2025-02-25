
class Location:

    def __init__(self, latitude =None,longitude=None, label=""):
        self.latitude = round(latitude, 6)
        self.longitude = round(longitude, 6)
        self.label = label

    def coordinates(self):
        return self.latitude, self.longitude

