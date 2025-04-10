#STRING
"""
= Python offers a variety of built-in string method sfor manipulating strings
"""

message = "Hello, greeting from rift koders, We are busy typing code "
message.lower() # converting all text to lowercase
message.upper() # converting all text to uppercase
message.split() # splits comma seoarated text
# CHECKING CONTENT
print("greeting" in message)
print(message.startswith("Hello"))
#STRIPPING WHITESPACE
msg = "  Hello  "
msg.strip()
#REPLACE
message.replace("Hello", "Yellow")
# COUNT AND FIND 
message.count("are")
message.find ("code")
# STRING FORMATING
name = " Saleh"
print(f"Hello , {name}")