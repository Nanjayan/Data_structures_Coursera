# python3

from collections import namedtuple

import math
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    """Worker class.
    The workers are sorted by release time. If the release time is the same for
    both of them, workers are sorted by their thread_id.
    """

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    
    result = []
    next_free_time = [Worker(i) for i in range(n_workers)]
    for job in jobs:
        next_worker = heapq.heappop(next_free_time)
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
        heapq.heappush(next_free_time,next_worker)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
