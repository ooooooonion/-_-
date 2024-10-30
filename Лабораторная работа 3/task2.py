def find_common_participants(first_group, second_group, inter=','):
    set_first_group = set(first_group.split(inter))
    set_second_group = set(second_group.split(inter))

    common_participants = set_first_group.intersection(set_second_group)
    common_participants = list(common_participants)

    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, inter = '|'))