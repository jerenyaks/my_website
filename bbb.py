while True:
 raw_input = input("Enter a ID number: ")
#whitespacehandling step1 is to remove leading and trailing whitespace
 id_number = raw_input.strip()
#step2 is to remove any internal whitespace
 id_number = id_number.replace(" ", "")

#rule1: ID number must be 8 characters long
 if len(id_number) != 8:
    print("Invalid ID number. ID number must be 8 characters long.")
#rule2: ID number must be digits only
 elif not id_number.isdigit():
    print("Invalid ID number. ID number must contain digits only.")
#rule3: ID number must not start with 0
 elif id_number.startswith("0"):
    print("Invalid ID number. ID number must not start with 0.")

    
 else:
    print("ID number is valid.", id_number)
    masked_id = "****" + id_number[-4:]
    print("Masked ID number:", masked_id)


