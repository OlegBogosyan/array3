def list_multiplied_by_average(new_list):
    return [i * (sum(new_list) / len(new_list)) for i in new_list]

