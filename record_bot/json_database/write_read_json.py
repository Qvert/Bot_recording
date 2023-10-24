import json


def write_json(dict_members: dict, name_file: str) -> None:
    """
    Function write json dict members
    :param dict_members: A dictionary with those who signed up
    :param name_file: File name
    :return: None
    """
    with open(f'json_files/{name_file}.json', mode='w', encoding='utf8') as file_write:
        json.dump(dict_members, file_write, indent=4)
        file_write.close()


def read_json(name_file: str) -> None:
    """
    Function read json file with dict members
    :param name_file: File name
    :return: None
    """
    with open(f'json_files/{name_file}.json', mode='r', encoding='utf8') as file_read:
        return json.load(file_read)
