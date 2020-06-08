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


def safely_exit(signo, sigframe):
    asyncio.create_task(safely_exit_management())


signal.signal(signal.SIGTERM, safely_exit)
signal.signal(signal.SIGINT, safely_exit)


async def safely_exit_management():
    print('Safely exit.')
    loop.stop()


async def loop_task():
    while 1:
        print("ha")  # 任务主体
        await asyncio.sleep(2)


loop.create_task(loop_task())
try:
    loop.run_forever()
finally:
    loop.close()
exit()
