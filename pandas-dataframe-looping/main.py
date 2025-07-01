student_dict = {
    "student": ["Nabeel", "Azeem", "Salah", "Zaid"],
    "score": [74, 85, 95, 65]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(row.student)  # if statement maybe used to
