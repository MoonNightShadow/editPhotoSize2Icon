#coding=utf8
import os,sys
from PIL import Image

image_size=[]
flag="true"
while (flag!="F"):
  flag=raw_input("Input size ,Input F to end : ")
  if flag!="F":
    image_size.append(int(flag))
#image_size = [512,256,144,140,128,120,108,100,88,72,48,32,28]
def create_icon():
  image_name=raw_input("Input image filename : ")
  for size in image_size:

    '''''pri_image = Image.open("icon.png")
    pri_image.thumbnail((size,size))
    image_name = "icon_%d.png"%(size)
    pri_image.save(image_name)'''
    pri_image = Image.open(image_name)
    pri_image.resize((size,size),Image.ANTIALIAS ).save("%s_%d.png"%(image_name,size))
if __name__ == "__main__":
  create_icon()
'''在pillow中图片的缩放有两种方式，1.使用resize函数，2,使用thumbnail函数
resize函数可以缩小，也可以放大
thumbnail只能缩小，不能放大
所以，如果你只打开一次图片，要存出多个尺寸的话，要么，从大到小开始缩放。
要么，使用resize.建议从大到小开始缩放，因为，使用resize放大的话，你可以想象那个马赛克。
当然，你也可以设置缩放图片的质量（ PIL.Image.NEAREST：最低质量， PIL.Image.BILINEAR：双线性，
PIL.Image.BICUBIC：三次样条插值，Image.ANTIALIAS：最高质量）'''
