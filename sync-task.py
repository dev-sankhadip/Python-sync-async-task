import requests
from timeit import default_timer


def request(session):
    url = "https://jsonplaceholder.typicode.com/photos"
    with session.get(url) as response:
        data = response.text
        if response.status_code != 200:
            print("FAILURE::{0}".format(url))
        return data


def start_sync_process():
    with requests.session() as session:
        print("{0:<30} {1:>20}".format("No", "Completed at"))

        start_time = default_timer()

        for i in range(15):
            request(session)
            elapsed_time = default_timer() - start_time
            completed_at = "{:5.2f}s".format(elapsed_time)
            print("{0:<30} {1:>20}".format(i, completed_at))


if __name__ == "__main__":
    start_sync_process()
