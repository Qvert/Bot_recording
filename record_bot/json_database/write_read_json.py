import json


def write_json(dict_members: dict, name_file: str) -> None:
    """
    Function write json dict members
    :param dict_members: A dictionary with those who signed up
    :param name_file: File name
    :return: None
    """
    with open(f'json_files/{name_file}.json', mode='w') as file:
        json.dump(dict_members, file, indent=4)
        file.close()
