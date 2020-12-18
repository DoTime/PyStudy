import subprocess as sub

if __name__ == '__main__':
    sub.run("hadoop fs -ls ", shell=True)
    sub.run("ll ", shell=True)