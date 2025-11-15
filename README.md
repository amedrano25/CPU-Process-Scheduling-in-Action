# CPU-Process-Scheduling-in-Action
Project aimed at showing the trade-offs for specific scheduling algorithms used in CPU scheduling and operating system implementation.

## Storyline
Our scenario takes place on a game server. Our game is capable of hosting several people and each player is able to do actions like firing a weapon, opening chest attack movement messages, etc. In our game every player commands the process. These processes arrive in an unpredictable time so they need the server to decide who's request to process next to the issues we faced is  keeping the experience Fair responds and efficient for everyone regardless of length of the task.

The reason scheduling is important is because if the server focuses too much on long or complex actions the short and frequent past are constantly happening and may experience severe lag. Effective CPU scheduling ensures that gameplay feels smooth and balanced, maintaining fairness without sacrificing speed. The algorithms we will be using are First-Come First-Served (FCFS), Round Robin, Priority Scheduling (Non-preemptive). These ensure fairness and efficiency in our game server.


## Project Overview
This project simulates multiple CPU scheduling algorithms, **First-Come First-Served (FCFS)**, **Round Robin**, and **Priority Scheduling** to analyze their performance under a unified set of process inputs.  

It demonstrates how different scheduling strategies impact **waiting time**, **turnaround time**, and **CPU utilization fairness**.

This second phase allows us to build from our storyline from above by implementing and comparing the algorithms in Python, along with generating **Gantt Charts** and **summary statistics** for each.

---

## Features

- Implementation of three classic CPU scheduling algorithms:
  - **FCFS (First Come, First Served)**
  - **Round Robin (with adjustable time quantum)**
  - **Priority Scheduling (Non-preemptive)**
- **Tabulated results** for each algorithm (via `tabulate` library)
- **Gantt chart visualization** using `matplotlib`
- **Automatic calculation** of average waiting and turnaround times

---

## Algorithms Implemented

### 1. FCFS (First-Come, First-Served)
- Processes are executed in the order of their arrival times.
- **Non-preemptive** scheduling.
- Simple but may cause high waiting time for later processes.

### 2. Round Robin
- Each process is given a fixed **time quantum**.
- **Preemptive**, ensuring fair CPU time distribution.
- Good for **time-sharing systems** like interactive environments.

### 3. Priority Scheduling
- Processes are executed based on their assigned **priority values**.
- Lower priority value = higher importance.
- Non-preemptive version used here.

---

## Data Structure

Each process is represented as a dictionary:

```python
{
    'pid': 'P1',
    'arrival': 0,
    'burst': 6,
    'priority': 2
}
```

## Requirements

Before running, install the following dependencies:

```
pip install matplotlib tabulate pandas
```

## How to Run
### 1. Run the simulation:
```
python main.py
```

### 2. Example output (terminal):
```
--- FCFS ---
  pid    arrival    burst    completion    turnaround    waiting
------  ---------  -------  -------------  ------------  ---------
P1            0        6             6             6          0
P2            1        2             8             7          5
P3            2        8            16            14          6
...

Average Waiting Time: 4.20
Average Turnaround Time: 8.80
```

### 3. Gantt Charts

Each algorithm generates a Gantt chart visualizing CPU execution order that can be downloaded to your local machine.

## Output Summary

At the end, a comparative table and bar chart summarize the results:

| Algorithm         | Avg Waiting | Avg Turnaround |
| ----------------- | ----------- | -------------- |
| FCFS              | 4.20        | 8.80           |
| Round Robin (q=3) | 3.60        | 7.40           |
| Priority          | 3.00        | 6.80           |


## Project Structure
```
CPU_scheduling/
│
├── main.py                    # Main script
├── README.md                  # README file
├── fcfs_chart.png             # Generated Gantt charts
├── rr_chart.png
└──  priority_chart.png
```

## Analysis Summary

FCFS: Simple and predictable but can result in long waiting times for later processes.

Round Robin: Provides fairness, small quantum improves responsiveness but increases context switching overhead.

Priority Scheduling: Ensures urgent tasks execute first, risk of starvation for low-priority processes.

## Team Members
| Member   | Responsibility                      |
| -------- | ----------------------------------- |
| Adam Medrano| Algorithm implementation, assisted in report creation|
| Joshua Kang| Managed the to-do list, hosted meetings, and created the slides|
| Jonathan Quiroz | Algorithm implementation, assisted in report creation |
| Frank Rangel | Worked on storyline, assisted in slide and report creation|
| Chase Sisavath | Algorithm implementation, assisted in report creation|

