"""
Given an array of meeting time intervals return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""
"""
- first index shows start time as 0 and end time as 30 = 1 conference room

- second index shows start time as 5 and end time as 10 -- so we see that this
 needs to be in another conference room b/c 5 & 10 fall in the range of 0, 30
 ** book a second room -- b/c 5 fall in between 0,30's meeting = 2 conference rooms

- but the third index shows start time as 15 and end time as 20 and the start
time number is greater than index 2's end time
** no need to add any new conference rooms
"""

"""
initial loop
i = [0,30]
i = [5,10]
i = [15,20]

j = 0, 30
"""


def meetingRoom(meetingTimes):
    meetingRooms = 0
    for i, time in enumerate(meetingTimes):
        print('what is this', meetingTimes[i-1][1])
        # TODO: review to make more dynamic
        start_time = time[0]
        if i == 0:
            meetingRooms += 1
        elif meetingTimes[i-1][1] > start_time:

            # When less than or equal to -> are values are the same?
            meetingRooms += 1
            # Previous value at end_time > next start_time? if so, meetingRooms += 1

    return meetingRooms


print(meetingRoom([[1, 30], [5, 10], [15, 20]]))
"""
for(let i = 0; i > meetingTimes.length; i++){
    start_time = meetingTimes[i][0]
    end_time = meetingTimes[i][1]
    if start_time == 0{
        meetingRooms++
    } else if{
        meetingTimes[i-1]
    }
}


{
    1: [1,30],
    2: [5,10], [15,20]
}
"""
