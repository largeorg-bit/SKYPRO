from typing import Any


def filter_by_state(user_list: list[dict[str,Any]], state: str = "EXECUTED") -> list[dict[str,Any]]:
    """Функция принимает список словарей и выводит список по ключу state (по умолчанию 'EXECUTED')"""
    result = []
    for user in user_list:
        if user["state"] == state:
            result.append(user)
    return result


def sort_by_date(user_list: list[dict[str,Any]], decreasing: bool = True) -> list[dict[str,Any]]:
    """Функция принимает список словарей и сортирует по date(по умолчанию по убыванию)"""
    return sorted(user_list, key=lambda x: x.get("date", 0), reverse=decreasing)


if __name__ == "__main__":
    user_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    print(filter_by_state(user_list))
    print(filter_by_state(user_list, "CANCELED"))
    print(filter_by_state(user_list, "abc"))

    print(sort_by_date(user_list))
    print(sort_by_date(user_list, False))
