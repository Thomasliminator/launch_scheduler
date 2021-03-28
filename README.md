# Launch Scheduler
### Written by Thomas Lim
NASA Summer Internship Programming Challenge

### Table of Contents:
1. [index.html](https://github.com/Thomasliminator/launch_scheduler/blob/master/index.html) (front page)
2. [data.json](https://github.com/Thomasliminator/launch_scheduler/blob/master/data.json) (schedule in JSON format)
3. [main.js](https://github.com/Thomasliminator/launch_scheduler/blob/master/main.js) (scripts for sorting, search)
4. [optimal.py](https://github.com/Thomasliminator/launch_scheduler/blob/master/optimal.py) (algorithm 1 for optimization)
5. [launch.py](https://github.com/Thomasliminator/launch_scheduler/blob/master/launch.py) (algorithm 2 for optimization)


### Tool Functionality:
The tool displays all of the April 2021 launches on the front page.
There is a search bar where the user can search for launches by date or vehicle name. 
The date, vehicle, and delay cost columns are sortable by clicking the column header.
By clicking the vehicle name (e.g. Bear I), additional information is shown about the launch.
- I added some dummy information that I thought might be applicable to a real tool.

### How to Run the Code (3 ways):
#### Option 1: Viewing it on a browser
The tool can be found at the following [link](http://thomasliminator.github.io/launch/).

#### Option 2: Running it locally on a browser through an http-server
The JSON data can only be read into the tool from a **local** file if running a local server. To run the program without runnign a server, see option 3. 
1. In the launch_scheduler directory, type the following command into the terminal: `$python3 -m http.server 8888`.
2. Go to a web browser and go to `localhost:8888` to launch the webpage.

#### Option 3: Running it locally on a browser without a server (change required)
To run the program without launching a local server, use the alternate URL (main.js line 8) instead of line 6 to get the JSON data from a server.

### Assumptions
1. The months of March and May do not have any launches scheduled. (e.g. a Moose-type launch can be scheduled on April 1 or April 30 with no issues)
2. All 11 launches on the original launch schedule must appear in the April launch schedule. (the Bear 3 launch cannot be moved.)
3. There is a cost for every delay; even of the same vehicle type. (e.g. moving a batch of 4 consecutive bumblebee launches costs 2 dollars.)
4. Based on the wording of the question, the Bear I launch must occur on April 2.

### Finding the Minimized Cost
1. The cost of a solution that costs 14 dollars was calculated by hand. This solution was created delaying the launches one day at a time in the original order of the launch dates. (i.e. Orca I is delayed until it meets the constraints, then Moose I, Bear I ...)
2. I wrote a quick algorithm to confirm that 14 dollars is the minimum delay cost. Using `optimal.py` I got the cost to move every launch date to every date in april. Any date that has an associated delay cost of 12 or more dollars is no longer considered since the total cost (including the Bear I delay of 2 dollars) would be greater or equal to 14 dollars (our currently best solution).
3. These dates were tested in `launch.py` to figure out the mimimum delay cost. I split up steps 2 and 3 so that I can greatly reduce the number of (launch, date) tuples to run a combinatorics function on it much more efficiently.
