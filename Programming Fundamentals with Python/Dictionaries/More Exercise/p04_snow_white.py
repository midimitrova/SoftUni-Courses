dwarfs_data = {}

command = input()
cnt_color_hats = []

while command != 'Once upon a time':
    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(' <:> ')
    dwarf_physics = int(dwarf_physics)

    if dwarf_name not in dwarfs_data.keys():
        dwarfs_data[dwarf_name] = {dwarf_hat_color: dwarf_physics}

    if dwarf_name in dwarfs_data.keys() and dwarf_hat_color not in dwarfs_data[dwarf_name].keys():
        dwarfs_data[dwarf_name][dwarf_hat_color] = dwarf_physics

    if dwarf_name in dwarfs_data.keys() and dwarf_hat_color in dwarfs_data[dwarf_name].keys():
        if dwarfs_data[dwarf_name][dwarf_hat_color] < dwarf_physics:
            dwarfs_data[dwarf_name][dwarf_hat_color] = dwarf_physics
        cnt_color_hats.append(dwarf_hat_color)
    command = input()

result_list = []
hat_len = "hat len"
name_d = "name"
hat_d = "hat"
physic_d = "physic"
for name in dwarfs_data.keys():
    for hat, physic in dwarfs_data[name].items():
        result_list.append({hat_len: cnt_color_hats.count(hat), name_d: name, physic_d: physic, hat_d: hat})
for show in sorted(result_list, key=lambda item: (-item[physic_d], -item[hat_len])):
    print(f"({show[hat_d]}) {show[name_d]} <-> {show[physic_d]}")
