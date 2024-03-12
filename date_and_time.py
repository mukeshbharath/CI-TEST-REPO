from datetime import datetime, timedelta

def current_datetime_in_timezone(offset):
    current_time = datetime.utcnow() + timedelta(hours=offset)
    return current_time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    # IST (Indian Standard Time) - UTC+5:30
    ist_time = current_datetime_in_timezone(5.5)
    print("Current IST Date & Time:", ist_time)

    # EST (Eastern Standard Time) - UTC-5:00
    est_time = current_datetime_in_timezone(-5)
    print("Current EST Date & Time:", est_time)

