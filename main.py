#Goal: Simulate CPU scheduling algorithms and visualize their performance using Gantt charts.

#Import necessary libraries
import matplotlib.pyplot as plt
from tabulate import tabulate
from collections import deque
import copy

#First-Come First-Served Algorithm
def fcfs(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    results = []
    timeline = []

    for p in processes:
        if time < p['arrival']:
            time = p['arrival']
        start = time
        time += p['burst']
        completion = time
        turnaround = completion - p['arrival']
        waiting = turnaround - p['burst']

        results.append({
            'pid': p['pid'],
            'arrival': p['arrival'],
            'burst': p['burst'],
            'completion': completion,
            'turnaround': turnaround,
            'waiting': waiting
        })
        timeline.append((p['pid'], start, completion))

    return results, timeline

#Round Robin Algorithm
def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda x: x['arrival'])
    remaining = {p['pid']: p['burst'] for p in processes}
    time = 0
    queue = deque()
    completed = []
    timeline = []
    i = 0
    n = len(processes)

    while len(completed) < n:
        while i < n and processes[i]['arrival'] <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time = processes[i]['arrival']
            continue

        current = queue.popleft()
        pid = current['pid']
        execute_time = min(quantum, remaining[pid])
        start = time
        time += execute_time
        end = time
        timeline.append((pid, start, end))
        remaining[pid] -= execute_time

        while i < n and processes[i]['arrival'] <= time:
            queue.append(processes[i])
            i += 1

        if remaining[pid] == 0:
            turnaround = time - current['arrival']
            waiting = turnaround - current['burst']
            completed.append({
                'pid': pid,
                'arrival': current['arrival'],
                'burst': current['burst'],
                'completion': time,
                'turnaround': turnaround,
                'waiting': waiting
            })
        else:
            queue.append(current)

    completed.sort(key=lambda x: x['pid'])
    return completed, timeline

#Priority Scheduling Algorithm
def priority_scheduling(processes):
    processes = sorted(processes, key=lambda x: (x['arrival'], x['priority']))
    time = 0
    completed = []
    timeline = []

    while processes:
        available = [p for p in processes if p['arrival'] <= time]
        if not available:
            time = processes[0]['arrival']
            continue
        current = min(available, key=lambda x: x['priority'])
        processes.remove(current)

        start = time
        time += current['burst']
        completion = time
        turnaround = completion - current['arrival']
        waiting = turnaround - current['burst']

        completed.append({
            'pid': current['pid'],
            'arrival': current['arrival'],
            'burst': current['burst'],
            'priority': current['priority'],
            'completion': completion,
            'turnaround': turnaround,
            'waiting': waiting
        })
        timeline.append((current['pid'], start, completion))

    completed.sort(key=lambda x: x['pid'])
    return completed, timeline

#Calculate average waiting and turnaround times
def calculate_averages(results):
    avg_wait = sum(p['waiting'] for p in results) / len(results)
    avg_turn = sum(p['turnaround'] for p in results) / len(results)
    return avg_wait, avg_turn

#Plot Gantt Chart
def plot_gantt_chart(timeline, title):
    fig, gnt = plt.subplots()
    gnt.set_title(title)
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Processes")

    #Unique process IDs
    processes = list(dict.fromkeys([pid for pid, _, _ in timeline]))
    gnt.set_yticks([i*10 for i in range(1, len(processes)+1)])
    gnt.set_yticklabels(processes)

    for idx, pid in enumerate(processes):
        for (p, start, end) in timeline:
            if p == pid:
                gnt.broken_barh([(start, end - start)], (idx*10, 9),
                                facecolors=('tab:blue'))

    plt.grid(True)
    plt.show()

#Main demonstration
#Note: Processes can be modified as needed
if __name__ == "__main__":
    processes = [
        {'pid': 'P1', 'arrival': 0, 'burst': 6, 'priority': 2},
        {'pid': 'P2', 'arrival': 1, 'burst': 2, 'priority': 1},
        {'pid': 'P3', 'arrival': 2, 'burst': 8, 'priority': 3},
        {'pid': 'P4', 'arrival': 3, 'burst': 3, 'priority': 2},
        {'pid': 'P5', 'arrival': 4, 'burst': 4, 'priority': 1}
    ]

    print(" CPU Scheduling Simulation ")

    #FCFS
    fcfs_result, fcfs_timeline = fcfs(copy.deepcopy(processes))
    avg_wait_fcfs, avg_turn_fcfs = calculate_averages(fcfs_result)
    print("\n--- FCFS ---")
    print(tabulate(fcfs_result, headers="keys"))
    print(f"Average Waiting Time: {avg_wait_fcfs:.2f}")
    print(f"Average Turnaround Time: {avg_turn_fcfs:.2f}")
    plot_gantt_chart(fcfs_timeline, "FCFS Gantt Chart")

    #Round Robin
    rr_result, rr_timeline = round_robin(copy.deepcopy(processes), quantum=3)
    avg_wait_rr, avg_turn_rr = calculate_averages(rr_result)
    print("\n--- Round Robin (q=3) ---")
    print(tabulate(rr_result, headers="keys"))
    print(f"Average Waiting Time: {avg_wait_rr:.2f}")
    print(f"Average Turnaround Time: {avg_turn_rr:.2f}")
    plot_gantt_chart(rr_timeline, "Round Robin (q=3) Gantt Chart")

    #Priority Scheduling
    ps_result, ps_timeline = priority_scheduling(copy.deepcopy(processes))
    avg_wait_ps, avg_turn_ps = calculate_averages(ps_result)
    print("\n--- Priority Scheduling ---")
    print(tabulate(ps_result, headers="keys"))
    print(f"Average Waiting Time: {avg_wait_ps:.2f}")
    print(f"Average Turnaround Time: {avg_turn_ps:.2f}")
    plot_gantt_chart(ps_timeline, "Priority Scheduling Gantt Chart")

    print("\n=== Summary ===")
    summary = [
        ["FCFS", avg_wait_fcfs, avg_turn_fcfs],
        ["Round Robin (q=3)", avg_wait_rr, avg_turn_rr],
        ["Priority", avg_wait_ps, avg_turn_ps]
    ]
    print(tabulate(summary, headers=["Algorithm", "Avg Waiting", "Avg Turnaround"], tablefmt="grid"))
