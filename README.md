# PixDB - Database made of pixels
## How it Works
Turns characters into binary and places binary per line on an image, image mode is greyscale, turns pixel intensity of 255 into a bit of 1, 0 into a bit of 0 and 125 to break the bit if the bit is under the width of the image for example the character is 6 bits long but the image width is 8 bits wide it will cut off at 7 and keep the 6 bits together. Feel free to pr have not worked with characters and binary much before, works with JSON too such as this example.
## Todo
- Figure out a way to append more data to the image
## Example Usage
```python
from pixdb import PixDB

db = PixDB(filename="owo") # Saves as owo.png in the current directory
db.write("OwO WHats this >~<") # Write to image 
print(db.read()) # Read binary from the image
```