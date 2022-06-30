"""
Auther-sumit
Goal-To calculate 24 times faster of any given time
"""


def time_in_days(t):
    day=t 
    hourss=day*24
    minutess=hourss*60



    Speedup_time=minutess/24
    Speedup_time_in_hours= Speedup_time /60
    return print(Speedup_time,"in Minutes", Speedup_time_in_hours,"in Hours")


time_in_days(24)
