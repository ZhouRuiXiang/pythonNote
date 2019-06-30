import time, os
#import multiprocessing
from multiprocessing import Process, current_process


# get process id
# print(os.getpid())
 
# 方法current_process用于获得当前进程实例对象（自动创建并启动的进程）
# print(multiprocessing.current_process().pid)

# get parent process id
# print(os.getppid())
def do_sth(arg1, arg2):
	print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
	print(arg1 + arg2)
	print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))


if __name__ == '__main__':

	print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))

	process = Process(target=do_sth, args=(10, 100))
	process.start()

	time.sleep(2)

	print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))

