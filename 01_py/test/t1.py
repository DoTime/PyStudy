
if __name__ == '__main__':
    from datetime import datetime

    now = datetime.now()
    milliseconds = now.microsecond // 1000

    print(milliseconds)  # 打印当前毫秒值
