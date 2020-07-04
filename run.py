from get_bifen import update_result
from get_oupei_game import *
from get_game_id import *
import threading

# while True:
#     time.sleep(1)
# tasks = []
# for i in get_all_game():
#     task = threading.Thread(target=get_oupei_30_data, args=(i,))
#     task1 = threading.Thread(target=get_oupei_60_data, args=(i,))
#     task2 = threading.Thread(target=get_yanzhou_30_game_result, args=(i,))
#     task3 = threading.Thread(target=get_yanzhou_60_game_result, args=(i,))
#     tasks.append(task)
#     tasks.append(task1)
#     tasks.append(task2)
#     tasks.append(task3)
#     task.start()
#     task1.start()
#     task2.start()
#     task3.start()
#     # 等待所有线程完成
# for _ in tasks:
#     _.join()
for i in get_all_game():
    get_yanzhou_30_game_result(i)
    get_yanzhou_60_game_result(i)