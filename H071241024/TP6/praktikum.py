# # Membuat List
# list_example = [1, 2, 3]  
# print(list_example)  # Output: [1, 2, 3]

# # Blank List
# blank_list = []
# print(blank_list)  # Output: []

# # List dengan Duplicate Values
# duplicate_list = [1, 2, 2, 3, 1, 2, 4]
# print(duplicate_list)  # Output: [1, 2, 2, 3, 1, 2, 4]

# # List dengan Mixed Values
# mixed_list = [1, 'Sistem', 'Informasi', 2023]
# print(mixed_list)  # Output: [1, 'Sistem', 'Informasi', 2023]

# # Membuat List dengan Range
# range_list = list(range(1, 5))
# print(range_list)  # Output: [1, 2, 3, 4]

# # Mengakses Data List
# print(list_example[0])  # Elemen pertama -> Output: 1
# print(list_example[-1])  # Elemen terakhir -> Output: 3

# # Mengubah elemen dalam List
# list_example[1] = 10
# print(list_example)  # Output: [1, 10, 3]

# # Slicing pada List
# print(list_example[:2])  # Mengambil elemen hingga indeks 2 -> Output: [1, 10]

# # Multi-Dimensional List (Matriks)
# multi_dim_list = [[1, 2], [2, 3]]
# print(multi_dim_list[0][1])  # Akses elemen 1,1 -> Output: 2

# # Append, Insert, Extend, Remove, dan Pop pada List
# list_example.append(4)
# list_example.insert(1, 2)
# list_example.extend([5, 6, 7])
# list_example.remove(10)
# pop_value = list_example.pop()  # Pop elemen terakhir
# print(list_example)  # Output list terbaru
# print(pop_value)  # Nilai yang di-pop

# # Reverse List
# list_example.reverse()
# print(list_example)  # Output reversed list

# # List Comprehension
# even_square = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(even_square)  # Output: [4, 16, 36, 64, 100]

# # Membuat Tuple
# tuple_example = ("Python", True, 1)
# print(tuple_example)  # Output: ('Python', True, 1)

# # Mengakses Nilai dalam Tuple
# programming_lang = ("Python", "Java", "Kotlin")
# print(programming_lang[0])  # Output: Python

# # Unpacking Tuple
# a, b, c = programming_lang
# print(a, b, c)  # Output: Python Java Kotlin

# # Manipulasi Tuple (Ubah ke List, lalu ubah kembali ke Tuple)
# tuple_to_list = list(tuple_example)
# tuple_to_list[1] = False
# tuple_example = tuple(tuple_to_list)
# print(tuple_example)  # Output: ('Python', False, 1)

# # Menghapus Tuple
# del tuple_example  # Menghapus tuple

# # Membuat Set
# set_example = {"Python", 1, 2, "Java"}
# print(set_example)  # Output: {'Python', 'Java', 1, 2}

# # # Set dengan elemen duplikat
# # duplicate_set = {1, 3, 2, 7, 3, 2, 3, 4}
# # print(duplicate_set)  # Output: {1, 2, 3, 4}

# # Menambah, Menghapus, dan Memodifikasi Set
# set_example.add("Kotlin")
# set_to_list = list(set_example)
# set_to_list[0] = "C++"
# set_example = set(set_to_list)
# print(set_example)  # Output: {'Kotlin', 'Python', 'Java', 'C++'}

# # Mengambil elemen dari Set
# set_example.pop()  # Menghapus elemen acak
# set_example.remove("C++")  # Menghapus elemen tertentu
# set_example.discard("Java")  # Menghapus elemen (tanpa error jika tidak ditemukan)

# # Operasi Set: Union, Intersection, Difference, dan Symmetric Difference
# a = {1, 2, 5}
# b = {3, 4, 1}
# print(a | b)  # Union -> Output: {1, 2, 3, 4, 5}
# print(a & b)  # Intersection -> Output: {1}
# print(a - b)  # Difference -> Output: {2, 5}
# print(a ^ b)  # Symmetric Difference -> Output: {2, 3, 4, 5}


# # Membuat Dictionary
# dict_example = {
#     "name": "Ariel",
#     "age": 21,
#     "hobby": "Playing Genshin"
# }
# print(dict_example)  # Output: {'name': 'Ariel', 'age': 21, 'hobby': 'Playing Genshin'}

# # Mengakses dan Mengupdate Nilai dalam Dictionary
# print(dict_example["name"])  # Output: Ariel
# dict_example["hobby"] = "Playing Minecraft"
# print(dict_example)  # Output: {'name': 'Ariel', 'age': 21, 'hobby': 'Playing Minecraft'}

# # Nested Dictionary
# nested_dict = {
#     "Fakultas": "MIPA",
#     "Program Studi": {
#         1: "Sistem Informasi",
#         2: "Matematika",
#         3: "Aktuaria"
#     }
# }
# print(nested_dict["Program Studi"][1])  # Output: Sistem Informasi

# # Menambahkan Elemen pada Dictionary
# dict_example["graduationYear"] = 2023
# print(dict_example)  # Output: {'name': 'Ariel', 'age': 21, 'hobby': 'Playing Minecraft', 'graduationYear': 2023}

# # Menghapus Elemen pada Dictionary
# dict_example.pop("graduationYear")  # Hapus elemen tertentu
# dict_example.clear()  # Hapus seluruh elemen
# print(dict_example)  # Output: {}