# -*- coding: UTF-8 -*-
import calendar
yy=int(input('输入年份：'))
mm=int(input('输入月份: '))
print(calendar.month(yy,mm))

import datetime
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday
print(getYesterday())
