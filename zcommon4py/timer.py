from datetime import datetime


FORMAT_PATH_MONTH = "%Y-%m" 
FORMAT_PATH_DATE = FORMAT_PATH_MONTH + "-%d"
FORMAT_TIME = "%H:%M:%S" 

SEC_MIN = 60
SEC_HR = 60 * SEC_MIN
SEC_DAY = 24 * SEC_HR
SEC_WEEK = 7 * SEC_DAY
SEC_MONTH = 30 * SEC_DAY 

MS_SEC = 1000
MS_MIN = 60 * MS_SEC
MS_HR = 60 * MS_MIN
MS_DAY = 24 * MS_HR
MS_WEEK = 7 * MS_DAY
MS_MONTH = 30 * MS_DAY

US_SEC = 1000000
US_MIN = 60 * US_SEC
US_HR = 60 * MS_MIN
US_DAY = 24 * US_HR
US_WEEK = 7 * US_DAY
US_MONTH = 30 * US_DAY

NS_US = 1000
NS_MS = 1000 * NS_US
NS_SEC = 1000 * NS_MS
NS_MIN = 60 * NS_SEC
NS_HR = 60 * NS_MIN
NS_DAY = 24 * NS_HR
NS_WEEK = 7 * NS_DAY
NS_MONTH = 30 * NS_DAY
        

def truncate(timestamp, timestamp_ref):
    return int(timestamp/timestamp_ref)


def round(timestamp, timestamp_ref):
    return int(truncate(timestamp, timestamp_ref) * timestamp_ref)


def get_current_time_sec():
    return int(datetime.timestamp(datetime.now()))


def to_unix_timestamp_sec(time_str, format_time):
    try:
        return int(datetime.timestamp(datetime.strptime(time_str, format_time)))
    except:
        return None


def to_time_str(timestamp_ms, format_time):
    try:
        return datetime.strftime(datetime.fromtimestamp(timestamp_ms), format_time)
    except:
        return None

        