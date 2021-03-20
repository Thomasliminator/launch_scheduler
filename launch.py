schedule = [
    {
        "type": "bear",
        "flight": "1",
        "day": "1"
    },
    {
        "type": None,
        "flight": None,
        "day": "2"
    },
    {
        "type": "orca",
        "flight": "1",
        "day": "3"
    },
    {
        "type": None,
        "flight": None,
        "day": "4"
    },
    {
        "type": "moose",
        "flight": "1",
        "day": "5"
    },
    {
        "type": None,
        "flight": None,
        "day": "6"
    },
    {
        "type": None,
        "flight": None,
        "day": "7"
    },
    {
        "type": None,
        "flight": None,
        "day": "8"
    },
    {
        "type": None,
        "flight": None,
        "day": "9"
    },
    {
        "type": "bear",
        "flight": "2",
        "day": "10"
    },
    {
        "type": None,
        "flight": None,
        "day": "11"
    },
    {
        "type": "bee",
        "flight": "1",
        "day": "12"
    },
    {
        "type": "bee",
        "flight": "2",        
        "day": "13"
    },
    {
        "type": "bee",
        "flight": "3",
        "day": "14"
    },
    {
        "type": "bee",
        "flight": "4",
        "day": "15"
    },
    {
        "type": None,
        "flight": None,
        "day": "16"
    },
    {
        "type": None,
        "flight": None,
        "day": "17"
    },
    {
        "type": None,
        "flight": None,
        "day": "18"
    },
    {
        "type": None,
        "flight": None,
        "day": "19"
    },
    {
        "type": "orca",
        "flight": "2",
        "day": "20"
    },
    {
        "type": None,
        "flight": None,
        "day": "21"
    },
    {
        "type": None,
        "flight": None,
        "day": "22"
    },
    {
        "type": "moose",
        "flight": "2",
        "day": "23"
    },
    {
        "type": None,
        "flight": None,
        "day": "24"
    },
    {
        "type": None,
        "flight": None,
        "day": "25"
    },
    {
        "type": None,
        "flight": None,
        "day": "26"
    },
    {
        "type": None,
        "flight": None,
        "day": "27"
    },
    {
        "type": None,
        "flight": None,
        "day": "28"
    },
    {
        "type": None,
        "flight": None,
        "day": "29"
    },
    {
        "type": "bear",
        "flight": "3",
        "day": "30"
    }
]

def isValidSchedule(schedule):
    for day in range(len(schedule)):
        if schedule[day]["type"] == "bear" and day+1 < len(schedule) and schedule[day+1]["type"] != None:
            return False
        if schedule[day]["type"] == "orca":
            if day+1 < len(schedule) and day-1 > -1 and schedule[day+1]["type"] != None and schedule[day-1]["type"] != None:
                return False
            elif day+1 < len(schedule) and day-1 < 0 and schedule[day+1]["type"] != None:
                return False
            elif day+1 > len(schedule)-1 and day-1 > -1 and schedule[day-1]["type"] != None:
                return False
        if schedule[day]["type"] == "bee" and day-1 > -1:
            if schedule[day-1]["type"] != "None" or schedule[day-1]["type"] != "bee":
                return False
        if schedule[day]["type"] == "moose":
            if day-1 > -1 and schedule[day-1]["type"] != None:
                return False
            if day+4 < 
    return True
        

print(isValidSchedule(schedule))
