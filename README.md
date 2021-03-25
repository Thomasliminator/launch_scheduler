# Launch Scheduler
### Written by Thomas Lim
NASA Summer Internship Programming Challenge

### Tool Functionality:
The tool displays all of the April 2021 flights as a table. 
There is a search bar where the user can search for flights by date or vehicle name. 
Both the date columns and the vehicle columns are sortable by clicking the column header.
By clicking the vehicle text (e.g. "Bear I") more information is shown about the launch.
- I added some dummy information that I thought might be applicable to a real tool.

### How to Run the Code:
The JSON data can only be read into the tool from a local file if running a local server. To run the program locally, use the alternate URL to get the JSON data from https.
1. Type the following command into the terminal: `$python3 -m http.server 8888`.
2. Go to a web browser and go to `localhost:8888` to launch the webpage.

A version of the tool is also hosted through my github account.
[link](http://thomasliminator.github.io/launch/)

### Assumptions
1. The months of March and May do not have any launches scheduled. (e.g. a Moose-type launch can be scheduled on April 1 or April 30 with no issues)
2. All 10 launches on the original launch schedule must appear in the April launch schedule.
3. Because the delay cost is per vehicle type, there is no cost to switch launches of the same type. (e.g. if a batch of Bumblebee launches are delayed by 1 day, the total delay cost is 0.5 dollars, not 2 dollars.)

### Solution Structure
- launch.py was used to