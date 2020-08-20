def CheckSpeed(speed):
    if speed < 70:
        raise Exception('速度太慢')
    if speed > 70:
        raise Exception('已經超速')

for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)
    except Exception as e:
        print('現在速度:{},{}'.format(speed,e))
    else:
        print('目前時速:{}'.format(speed))