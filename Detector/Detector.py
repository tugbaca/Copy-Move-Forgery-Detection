from Detector.MatchFeature.Match import MatchFeatures
from DrawFunctions.Rectangle import DrawRectangle

class AbsDetector:
    key_points = None
    descriptors = None
    color = None
    image = None
    distance = None

    def __init__(self, image, key_points, descriptors, distance, color):
        self.image = image
        self.key_points = key_points
        self.descriptors = descriptors
        self.distance = distance
        self.color = color
        self.detector()

    def detector(self):
        match = MatchFeatures(self.key_points, self.descriptors, self.distance)  # match points
        draw = DrawRectangle(self.image, match.gPoint1, match.gPoint2, self.color, match.cRectangle)  # draw matches
    #   draw = DrawLine(self.image,keypoints1 = points1, keypoints2 = points2,color=self.color)
        self.image = draw.image