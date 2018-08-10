from PIL import Image
import os
import datetime

path = "D:/test/input"
outpath = "D:/test/out"

def cut(filename,folder):
    name = path + "/" + folder + "/" + filename
    img = Image.open(name)
    filename = filename.replace(".png","")
    filename = filename.replace(".jpg","")
    width = img.size[0]
    height = img.size[1]
    
    name1 = outpath + "/" + folder + "/" + filename+"_2.png"
    name2 = outpath + "/" + folder + "/" + filename+"_1.png"
    
    img1 = img.crop((0,0,width/2,height))
    img2 = img.crop((width/2,0,width,height))
    
    img1.save(name1)
    img2.save(name2)


if __name__=="__main__":
    starttime = datetime.datetime.now()
    i = 0
    j = 0
    folders = os.listdir(path)
    for folder in folders:
        os.makedirs(outpath + "/" + folder)
        files = os.listdir(path + "/" + folder)
        i  = i + 1
        for file in files:
            j = j + 1
            nowtime = datetime.datetime.now()
            runtime = (nowtime - starttime).seconds
            m, s = divmod(runtime, 60)
            h, m = divmod(m, 60)
            strruntime = str(h) + ":" + str(m) + ":" + str(s)

            remaintime = int(runtime*((4140-j)/j))
            m, s = divmod(remaintime, 60)
            h, m = divmod(m, 60)
            strremaintime = str(h) + ":" + str(m) + ":" + str(s)
            
            jindu = ('%.4f' % (j/414))
            cut(file,folder)
            print(str(j) + "/4140\t第" + str(i) + "话（34）\t" +  file + "\t" + strruntime + "\t" + strremaintime + "    \t" + jindu + "% ")
