
class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Sort jobs based on profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Find the maximum deadline among all jobs to size the slot array
        maxi = max(job.deadline for job in Jobs)
        
        # Initialize an array to track the occupied slots
        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0
        
        # Iterate over all jobs
        for i in range(n):
            # Try to find a slot for this job, starting from its deadline
            for j in range(Jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i  # Assign this slot to the job
                    countJobs += 1  # Increment the job count
                    jobProfit += Jobs[i].profit  # Add the profit
                    break  # Break as the job has been scheduled
        
        return countJobs, jobProfit
