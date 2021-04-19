from datetime import datetime


def what_date_is_it():
    """
    get the current date
    :return: string
    """
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


if __name__ == "__main__":
    print("can't be run")
