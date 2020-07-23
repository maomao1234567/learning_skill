import threading
import requests
import time
from datetime import datetime
import asyncio
import threading


def foo():
    for i in range(100000):
        print(i)
        yield
        time.sleep(1)


async def print_string(interval):
    for _ in range(10):
        print(f'{datetime.now()} 做{interval}秒的任务!')
        now_time = time.time()
        end_time = now_time + interval
        while True:
            await asyncio.sleep(1)
            new_time = time.time()
            if new_time >= end_time:
                break


class Task:
    next_task_id = 0

    def __init__(self, corounte):
        self.id = self.next_task_id
        self.next_task_id += 1
        self.corounte = corounte


class Scheduler:
    def __init__(self):
        self.runnable_tasks = []
        self.task_result = []
        self.error_tasks = []

    def add_task(self, corounte):
        task = Task(corounte)
        self.runnable_tasks.append(task)

    def run_tasks_until_all_completion(self):
        while len(self.runnable_tasks) != 0:
            task = self.runnable_tasks.pop(0)
            try:
                yield_result = next(task.corounte)
            except StopIteration as stop:
                self.task_result.append(task)
            except Exception as error:
                self.task_result.append(task)
            else:
                if yield_result is None:
                    self.runnable_tasks.append(task)


async def main():
    pass

if __name__ == '__main__':
    pass
