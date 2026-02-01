import sys, os
from PIL import Image

def convert2ASCII(img):
    """Convert image to grid of ASCII characters"""
    width,height = img.size
    
    #Fill grid list with image size
    grid = []
    for i in range(height):
        grid.append(["X"]*width)

    #Load pixel data
    pixels = img.load()

    #Match colours to ASCII characters
    for y in range(height):
        for x in range(width):
            if sum(pixels[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pixels[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pixels[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pixels[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pixels[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pixels[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pixels[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pixels[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pixels[x,y]) in range(700,750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
                    
    return grid


if __name__ == "__main__":
    #Argument count
    argc = len(sys.argv)
    img = Image.open(sys.argv[1])
    
    if len(sys.argv) < 2:
        print("Invalid command. At least one argument required.\nUsage: python3 img2ascii <filename>")
        sys.exit()
    elif argc >= 3:
        if not sys.argv[2].isdigit():
            print("Invalid command. Scale must be an integer.\nUsage: python3 img2ascii <filename> <scale>")
            sys.exit()
               
        #Set required variables using image data
        width,height = img.size
        type = img.format
        scale = int(sys.argv[2])
        
        #Resize image. Save
        img.resize((width//scale, height//scale)).save("scaled.%s"%type)
        
        #Open resized image
        img = Image.open("scaled.%s"%type)
        
    #Write converted ascii characters to text file then close file
    file = open("ascii.txt", 'w')
    for row in convert2ASCII(img):
        file.write("".join(row)+'\n')
    file.close()
    
    img.close()
    
    try:
        os.remove("scaled.%s"%type)
    except:
        pass
    
    #Notify conversion was successful
    print("Conversion completed successfully!")

    
    
    
