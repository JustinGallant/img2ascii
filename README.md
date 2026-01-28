# img2ascii
img2ascii is an image conversion tool to convert any still image to ascii characters.
## How to install
- Install Python3:
  - Linux: `apt install python3`
  - Windows: Install manually via https://www.python.org/downloads/ or through the Microsoft Store.
- Download dependancies: `pip install pillow` (Fork of PIL [Python Image Library])

## How to use
`python3 img2ascii.py <ImageFile> <Scale>`\
Output is stored as text file, ascii.txt. Scaled images are generated then removed upon completion. Scale is an optional argument.

## Example:
`python3 img2ascii.py example.jpg 3`

### Input Example:
![exampleInput](https://github.com/user-attachments/assets/64b305b5-7062-4574-a7d3-4938139d632c)
### Output Example:
<img width="1000" height="1332" alt="Screenshot" src="https://github.com/user-attachments/assets/e9c04932-b076-4b76-a039-d3b7a5063a48" />
