from datetime import datetime, timedelta

GREEN_TIME = 60  # in seconds
YELLOW_TIME = 5  # in seconds
RED_TIME = 30  # in seconds

start_time = datetime.strptime("00:00:00", "%H:%M:%S")
end_time = start_time + timedelta(seconds=GREEN_TIME + YELLOW_TIME + RED_TIME)

input_time = datetime.strptime("11:42:06", "%H:%M:%S") #change the time from here

elapsed_time = input_time - start_time
complete_cycles = int(elapsed_time.total_seconds() / (GREEN_TIME + YELLOW_TIME + RED_TIME))

cycle_start_time = start_time + timedelta(seconds=complete_cycles * (GREEN_TIME + YELLOW_TIME + RED_TIME))
cycle_end_time = cycle_start_time + timedelta(seconds=GREEN_TIME + YELLOW_TIME + RED_TIME)

time_within_cycle = (input_time - cycle_start_time).total_seconds()
if time_within_cycle < GREEN_TIME:
    print("Traffic light is green at", input_time)
elif time_within_cycle < GREEN_TIME + YELLOW_TIME:
    print("Traffic light is yellow at", input_time)
else:
    print("Traffic light is red at", input_time)
