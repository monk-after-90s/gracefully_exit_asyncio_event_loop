import signal
import asyncio

"""
信号值      符号      行为

2          SIGINT    进程终端，CTRL+C

9          SIGKILL   强制终端

15         SIGTEM    请求中断

20         SIGTOP    停止（挂起）进程 CRTL+D
"""
loop = asyncio.get_event_loop()


def safely_exit():
    loop.close()


loop.add_signal_handler(signal.SIGTERM, safely_exit)
loop.add_signal_handler(signal.SIGINT, safely_exit)


async def safely_exit_management():
    print('Safely exit.')


async def loop_task():
    while 1:
        print("ha")  # 任务主体
        await asyncio.sleep(2)


loop.create_task(loop_task())

try:
    loop.run_forever()
except:
    print('Loop detects a error')
finally:
    loop.run_until_complete(safely_exit_management())
# todo 还没有完成
