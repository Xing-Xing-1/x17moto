from datetime import datetime
import pytz

TIME_UNIT_TABLE = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
    "weeks": 604800,
    "months": 2592000,
    "years": 31536000,
}

TIMEZONE_TABLE = {
    timezone: int(
        pytz.timezone(timezone).utcoffset(datetime.now()).total_seconds() / 3600
    )
    for timezone in pytz.all_timezones
}
