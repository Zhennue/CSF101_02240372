name = "Yeshey Zhennue"
age = 17
height = 1.75
is_student = True

person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person_info)

person_info["favourite_color"] = "black"
print(person_info)

try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")