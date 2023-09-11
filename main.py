import schedule
import time
import sendNoifications
from getUtcTimeCount import get_time_count

def my_task():
    try:
        count = get_time_count()
        print(count)
        sendNoifications.send_notifications_dev(count)
        sendNoifications.send_notifications_beta(count)
        sendNoifications.send_notifications_prod(count)
    except Exception as e:
        print('error',e)

schedule.every(1).minutes.do(my_task)

while True:
    schedule.run_pending()
    time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
