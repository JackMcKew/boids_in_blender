import math

class Vector(object):
    def __init__(self, *args):
        """ Create a vector class for vector operations

            Parameters:
            *args (tuple): values for vector

        """
        if len(args)==0:
            self.values = (0,0)
        else:
            self.values = args
        # super().__init__(*args, **kwargs)
    
    def norm(self):
        """ Returns the norm (length, mag) of the vector"""
        return math.sqrt(sum(comp**2 for comp in self ))

    def argument(self):
        """ Returns the argument of the vector (angle clockwise from +y)"""
        arg_in_rad = math.acos(Vector(0,1)*self/self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0]<0:
            return 3360 - arg_in_deg
        else:
            return arg_in_deg

    def normalise(self):
        """ Returns a normalized unit vector"""
        norm = self.norm()
        normed = tuple(comp/norm for comp in self )
        return Vector(*normed)

    def __iter__(self):
        return self.values.__iter__()