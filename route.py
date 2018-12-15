from point import Point
from sheet import PointsSheet
import math


class Route:
    """
    calculate route
    """

    def __init__(self):
        """initialize route"""

    def make_sheet(self):
        """get x,y value of point"""
        self.x = points_sheet.x
        self.y = points_sheet.y

    def route_formula(self,xa,ya,xb,yb):
        lenth = math.sqrt((point_a.x-point_b.x)**2+(point_a.y-point_b.y)**2)
        route += lenth
        print('lenth ',lenth)
        print('route ',route)
        return route

    def calcutate_formula(self):
        """formula for calculating"""
        route = 0
        # cycle for making
        for i in range(0,len(self.x)):
            if i == 0:
                point_a = Point(0,0)
                point_b = Point(self.x[i],self.y[i])
                route_formula(point_a.x, point_a.y, point_b.x, point_b.y)
            else:
                point_a = Point(self.x[i-1],self.y[i-1])
                point_b = Point(self.x[i],self.y[i])
                route_formula(point_a.x, point_a.y, point_b.x, point_b.y)
        print(route)

    def main(self):
        """calculating process"""
        make_sheet()
        calcutate_formula()



calc_route = Route()
points_sheet = PointsSheet()
calc_route.main()


