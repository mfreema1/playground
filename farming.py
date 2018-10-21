"""
What is the biggest square piece of land that we can divide up our farm with?

This probably isn't obvious why this works, please see Euclid's algorithm to understand why it is so simple.
"""
def land(length, width):

    #if it is already square, then that is the largest piece that will work for the farm
    if length == width:
        return length
    if(length > width):
        return land(length - width, width)
    else:
        return land(length, width - length)

print(land(1680, 640))