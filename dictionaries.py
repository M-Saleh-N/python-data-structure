# DICTIONARIES
"""
= Dictionaries store data in the key-value pairs
Properties:-
    * Ket -value pairs
    *  Unordered (but insertation is ordered in pythjon 3.7+)
    *  Mutable
"""
student_name = {
    "name": "Tilak",
    "age": 18,
    "city": "Mumbai"
}
#ACCESSING
student_name["name"]
#ADDING/UPDATING
student_name["city"] = "Nakuru"
#DELETING
del student_name["age"]
#LOOPing
for key, value in student_name.items():
    print(key,value)
#KEYS AND VALUES
student_name.keys()
student_name.values()
#NESTING
student_name = {
    "student_1": {
        "name": "Vansh",
        "city": "Nakuru",
        "age": 17
    },
    "student_2": {
        "name": "Ansh",
        "city": "Nairobi",
        "age": 20
    }
}