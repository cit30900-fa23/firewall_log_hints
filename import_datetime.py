#import datetime
from datetime import datetime
import pytz

def main():
    # print(datetime.now())

    dt = datetime.now()
    print(dt.hour)
    print(dt.second)
    print(dt.year)
    print(dt.minute)
    print(dt.tzinfo)

    # Create a timezone object
    est_timezone = pytz.timezone("US/Eastern")
    nepal_timezone = pytz.timezone("Asia/Kathmandu")

    # Apply the timezone to our object
    # aware_dt = est_timezone.localize(dt)
    aware_dt = nepal_timezone.localize(dt)
    print(aware_dt)

if __name__ == '__main__':
    main()