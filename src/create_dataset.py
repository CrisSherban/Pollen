from datetime import datetime as dt
import numpy as np
import pathlib

car_pnts = ['N', 'NE', 'NO', 'E', 'O', 'S', 'SE', 'SO']
wind_dir_to_num = {name: index for index, name in enumerate(car_pnts)}


def insert_to_date_indexed(parent_dict, child_dict):
    one = list(parent_dict.keys())
    two = list(child_dict.keys())
    # attention O(n²) complexity in the following assert
    assert np.sum([i == j for i in one for j in two]) > 0, "Something is wrong with the data, dates don't match"

    for date_key in list(parent_dict.keys()):
        try:
            for feature in child_dict[date_key]:
                parent_dict[date_key].append(wind_dir_to_num[feature] if feature in car_pnts else feature)
        except KeyError:
            [parent_dict[date_key].append(0) for _ in child_dict[list(child_dict.keys())[0]]]


def extract_gramineae(poll):
    grasses = []
    for line in poll:
        if 'Gramineae' in line:
            grasses.append([line[0], line[3]])
    np.savetxt('resources/gram_fi.csv', grasses, delimiter=";", fmt="%s")


def arr_to_dict(arr):
    return {a[0]: list(a[1:]) for a in arr}


def main():
    cwd = pathlib.Path.cwd()
    project_cwd = cwd.parent

    poll = arr_to_dict(np.loadtxt(f"{project_cwd}/resources/poll_fi.csv", delimiter=';', dtype=object)[1:])
    prec = arr_to_dict(np.loadtxt(f"{project_cwd}/resources/prec_fi.csv", delimiter=';', dtype=object)[1:])
    temp = arr_to_dict(np.loadtxt(f"{project_cwd}/resources/temp_fi.csv", delimiter=';', dtype=object)[1:])
    anemo = arr_to_dict(np.loadtxt(f"{project_cwd}/resources/anemo_fi.csv", delimiter=';', dtype=object)[1:])
    gramineae = arr_to_dict(np.loadtxt(f"{project_cwd}/resources/gram_fi.csv", delimiter=';', dtype=object)[1:])

    insert_to_date_indexed(gramineae, prec)
    insert_to_date_indexed(gramineae, temp)
    insert_to_date_indexed(gramineae, anemo)

    full_data = [["INDEX", "CONC", "PREC", "TMAX", "TMIN", "VMIN", "DIR", "VMAX"]]
    for index, el in enumerate(gramineae):
        full_data.append([el] + gramineae[el])
        if index == 50:
            print(full_data)

    # reorder by date
    full_data[1:] = sorted(full_data[1:], key=lambda entry: dt.strptime(entry[0], "%d/%m/%y"))

    np.savetxt('{project_cwd}/resources/grasses_weather.csv', X=full_data, fmt="%s", delimiter=";")


if __name__ == '__main__':
    main()
