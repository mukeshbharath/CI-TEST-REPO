from datetime import datetime
import pytz

def current_datetime_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

if __name__ == "__main__":
    # IST (Indian Standard Time)
    ist_time = current_datetime_in_timezone('Asia/Kolkata')
    print("Current IST Date & Time:", ist_time)

    # EST (Eastern Standard Time)
    est_time = current_datetime_in_timezone('America/New_York')
    print("Current EST Date & Time:", est_time)

