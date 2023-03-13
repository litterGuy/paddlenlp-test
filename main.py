import datetime

from paddlenlp import Taskflow

def print_hi():
    schema = ['情感倾向[正向，负向]']
    senta = Taskflow("sentiment_analysis", model="uie-senta-base", schema=schema)
    starttime = datetime.datetime.now()
    print(senta('蛋糕味道不错，店家服务也很好'))
    endtime = datetime.datetime.now()
    print(endtime - starttime)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
