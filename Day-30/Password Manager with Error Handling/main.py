try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary)

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("This is My File")
except KeyError as error_message:
    print(f"The key {error_message} does not exit.")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("This is an error that I made up.")
