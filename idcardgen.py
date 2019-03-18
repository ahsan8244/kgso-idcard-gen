from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import glob
import math
import os

imageList = []
cardPath = 'C:/Users/user/Pictures/kgso ids/card.jpg'

for filename in glob.glob('C:/Users/user/Pictures/kgso participants/*'):
    imageList.append(filename)

#for filename in glob.glob('C:/Users/user/Pictures/kgso participants/*.jpeg'):
    #imageList.append(filename)

font = ImageFont.truetype("C:/Users/user/Documents/Raleway-Regular.ttf", 35)
template = Image.open(cardPath)
W,H = (template.width, template.height)
offsetText = 70

imageList.sort()
print(imageList)

n = 0
for imagePaths in imageList:
    details = imageList[n].split('\\')[1]
    name = details.split('-')[0]
    role = details.split('-')[1]
    dept = details.split('-')[2][:-4]
    pic = Image.open(imageList[n])
    resizedPic = pic.resize((293, 422))
    cardCopy = template.copy()
    position = (math.floor((cardCopy.width - resizedPic.width)/2), math.floor((cardCopy.height - resizedPic.height)/2))
    cardCopy.paste(resizedPic, position)
    cardText = ImageDraw.Draw(cardCopy)
    tW = [cardText.textsize(name)[0],cardText.textsize(role)[0],cardText.textsize(dept)[0]]
    cardText.text(( (W-tW[0])/2 - offsetText,750),name,(255,255,255),font=font)
    cardText.text(( (W-tW[1])/2 - offsetText,800),role,(255,255,255),font=font)
    cardText.text(( (W-tW[2])/2 - offsetText,850),dept,(255,255,255),font=font)
    cardCopy.save('C:/Users/user/Pictures/kgso ids/' + str(n) + '.png', dpi=(300,300))
    n = n + 1
