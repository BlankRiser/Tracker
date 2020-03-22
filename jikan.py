from jikanpy import Jikan

obj = Jikan()

schedule = obj.schedule()

# print(type(schedule))
# print(schedule.keys())

sunday = schedule['sunday']

print(sunday[0])