from PIL import Image
class cap:
    def __init__(self, img):
        self.img = Image.open(img)
        self.bwimg = None

        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.apply_blackwhite_filter()
        self.split()
        self.txt = str(self.get_image_content(self.c1))+str(self.get_image_content(self.c2))+str(self.get_image_content(self.c3))
    def apply_blackwhite_filter(self):
        pixel =self.img.load()
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                if (pixel[i,j][0]+pixel[i,j][1]+pixel[i,j][2])/3<255/2-50:
                   pixel[i,j]=(255,255,255)
                else:
                   pixel[i,j]=(0,0,0)
        self.bwimg = self.img
    def split (self):
        pci=[]

        t=False
        pixel =self.bwimg.load()
        for i in range(self.bwimg.size[0]):
            if t==True and (len(pci)%2)==0:
                pci.append(i-1)
            if t==False and (len(pci)%2)!=0:
                pci.append(i-1)
            t=False
            for j in range(self.bwimg.size[1]):
                if pixel[i,j][0]==0 and pixel[i,j][1]==0 and pixel[i,j][2]==0:
                    t=True
                    break
        box = (pci[0], 0, pci[1], 25)
        c1=self.bwimg.crop(box)
        c1.save('c1.jpg')
        self.c1 = c1
        box = (pci[2], 0, pci[3], 25)
        c2=self.bwimg.crop(box)
        c2.save('c2.jpg')
        self.c2 = c2
        box = (pci[4], 0, pci[5], 25)
        c3=self.bwimg.crop(box)
        c3.save('c3.jpg')
        self.c3 = c3
    def compare(self,src,dst):
        b=True
        if src.size[0]==dst.size[0] and src.size[1]==dst.size[1]:
            pixels =src.load()
            pixeld =dst.load()
            for i in range(src.size[0]):
                for j in range(src.size[1]):
                    if pixels[i,j]!=pixeld[i,j]:
                        b=False
        else:
            b=False
        return(int(b))
    def get_image_content(self,image):
        b=0
        c=[]
        pixeli=image.load()
        im0=Image.open('im0.jpg')
        pixel0=im0.load()
        for i in range(im0.size[0]):
            for j in range(im0.size[1]):
                try:
                    if pixeli[i,j]==pixel0[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im1=Image.open('im1.jpg')
        pixel1=im1.load()
        for i in range(im1.size[0]):
            for j in range(im1.size[1]):
                try:
                    if pixeli[i,j]==pixel1[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im2=Image.open('im2.jpg')
        pixel2=im2.load()
        for i in range(im2.size[0]):
            for j in range(im2.size[1]):
                try:
                    if pixeli[i,j]==pixel2[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im3=Image.open('im3.jpg')
        pixel3=im3.load()
        for i in range(im3.size[0]):
            for j in range(im3.size[1]):
                try:
                    if pixeli[i,j]==pixel3[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im4=Image.open('im4.jpg')
        pixel4=im4.load()
        for i in range(im4.size[0]):
            for j in range(im4.size[1]):
                try:
                    if pixeli[i,j]==pixel4[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im5=Image.open('im5.jpg')
        pixel5=im5.load()
        for i in range(im5.size[0]):
            for j in range(im5.size[1]):
                try:
                    if pixeli[i,j]==pixel5[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im6=Image.open('im6.jpg')
        pixel6=im6.load()
        for i in range(im6.size[0]):
            for j in range(im6.size[1]):
                try:
                    if pixeli[i,j]==pixel6[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im7=Image.open('im7.jpg')
        pixel7=im7.load()
        for i in range(im7.size[0]):
            for j in range(im7.size[1]):
                try:
                    if pixeli[i,j]==pixel7[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im8=Image.open('im8.jpg')
        pixel8=im8.load()
        for i in range(im8.size[0]):
            for j in range(im8.size[1]):
                try:
                    if pixeli[i,j]==pixel8[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        im9=Image.open('im9.jpg')
        pixel9=im9.load()
        for i in range(im9.size[0]):
            for j in range(im9.size[1]):
                try:
                    if pixeli[i,j]==pixel9[i,j]:
                        b+=1
                except:
                    pass
        c.append(b)
        b=0
        d=0
        print(c)
        for i in range(len(c)):
            if c[i]>b:
                b=c[i]
                d=i
        if d==0:
            rgbi = 0
            rgb0 = 0
            rgb9 = 0
            for i in range(image.size[1]):
                rgbi += pixeli[6,i][0]
            print(rgbi)
            for i in range(im0.size[1]):
                rgb0 += pixel0[6,i][0]
            print(rgb0)
            for i in range(im9.size[1]):
                rgb9 += pixel9[6, i][0]
            print(rgb9)
            if (rgbi-rgb0)**2 >= (rgbi - rgb9)**2:
                d = 9
            else:
                pass
        return(d)

