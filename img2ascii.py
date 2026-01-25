import sys
from PIL import Image
    
def convert2ASCII(img):
    w,h = img.size
    
    #Fill grid list with image size
    grid = []
    for i in range(h):
        grid.append(["X"]*w)

    #Load pixel data
    pixels = img.load()

    #Match colours to ASCII characters
    for y in range(h):
        for x in range(w):
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



#Argument count
argc = len(sys.argv)

if len(sys.argv) < 2:
    print("Invalid command. At least one argument required.\nUsage: python3 img2ascii <filename>.png")
    sys.exit()
elif argc == 2:
    img = Image.open(sys.argv[1])
elif argc >= 3:
    if not sys.argv[2].isdigit():
        print("Invalid command. Scale must be an integer.\nUsage: python3 img2ascii <filename>.png <scale>")
        sys.exit()
    
    #Open image
    img = Image.open(sys.argv[1]) 
    
    #Set required variables using image data
    w,h = img.size
    type = img.format
    scale = int(sys.argv[2])
    
    #Resize image. Save
    img.resize((w//scale, h//scale)).save("scaled.%s"%type)
    
    #Open resized image
    img = Image.open("scaled.%s"%type)
    
#Write converted ascii characters to text file then close file
txtFile = open("ascii.txt", 'w')
for row in convert2ASCII(img):
    txtFile.write("".join(row)+'\n')
txtFile.close()

#Notify conversion was successful
print("Conversion completed successfully!")
    
    
