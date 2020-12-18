# 获取md5
def getmd(str):
    # 由于MD5模块在python3中被移除  使用hashlib模块进行md5操作
    import hashlib
    # 创建md5对象
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


if __name__ == '__main__':
    # print("1234\n")
    print("1234")
    print(getmd("1234哈哈哈哈哈哈"))

    # print(getmd("1000003031386950100000196044613903000000005056880彭宇2020-10-01 00:00:15999911232340030222280302220302002020-10-01 00:00:162020-10-01 00:00:161100"))
    # print(getmd("1000003031386976100000196044616500302008100385383宋厂林2020-10-01 00:01:58999911672340030213030302130302002020-10-01 00:02:002020-10-01 00:02:001100"))


    # for line in open("foo.txt"):
    #     print(line)
