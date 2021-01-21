class Solution(object):
    def leastInterval(self, tasks, N):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)