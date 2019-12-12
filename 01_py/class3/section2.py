# -*- coding: utf-8 -*-

# f=open("demo.txt","a")
# f.write("aaa bbbb")

# readline= f.readline()
# print(readline)


# 文本
f=open("demo.txt")
iter_file= iter(f)
for l in iter_file:
    print(l)

"""
 写入
write
writelines

"""

fw=open("demo.txt","w")
fw.writelines("dsjflsdf")
fw.flush()
fw.close()



# 文件指针



















