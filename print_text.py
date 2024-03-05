try:
    width = int(input())
    height = int(input())
    def rectanglePerimeter(width, height):
       return ((width + height)*2)
    print(rectanglePerimeter(width, height))
except EOFError as e:
    print(end="")
