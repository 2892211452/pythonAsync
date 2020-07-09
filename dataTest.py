import pickle
from path  import *
#设置递归深度，为了解决数据存储问题
import sys
sys.setrecursionlimit(10000)


if __name__=="__main__":
    output = open(FileDir+'/dmList/data4.pkl', 'rb')


    data=pickle.load(output)

    print(len(data))
    print(data[0])



    output.close()
