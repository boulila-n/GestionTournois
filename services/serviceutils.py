import datetime
from re import compile


def is_valid_date(str):
    date_format = compile(r"^(\d?\d)\W(\d?\d)\W(\d{4})$")
    string_match = date_format.match(str)
    if string_match:
        try:
            date = datetime.date(
                int(string_match.group(3)),
                int(string_match.group(2)),
                int(string_match.group(1)))
        except ValueError as exception:
            return False
        return date
    else:
        return False


def datetime_to_str(date):
    if isinstance(date, datetime.date):
        str_date = (
                f"{date.day:0>2d}/"
                + f"{date.month:0>2d}/"
                + str(date.year)
        )
        return str_date
    return False
