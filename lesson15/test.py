from datetime import datetime, timedelta


delta = timedelta(
    days=50,
    seconds=27,
    milliseconds=29000,
    microseconds=10,
    minutes=5,
    hours=8,
    weeks=28
)
print(delta)


seventh_day_2020 = datetime(year=2023, month=4, day=9, hour=19)
ts = seventh_day_2020.timestamp()
print(ts)

ts += 100_000_000
print(datetime.fromtimestamp(ts))

result_day_2020 = seventh_day_2020.strftime('%A %d %B %Y')
print(result_day_2020)

datetime_result = datetime.strptime(result_day_2020, '%A %d %B %Y')
print(datetime_result)

result2 = datetime_result.strftime("%Y-%m-%d")
print(result2)