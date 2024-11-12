def longest_line_in_file(filename):
    max_length = 0
    longest_line = ""

    
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            line_length = len(stripped_line)
            
        
            if line_length > max_length:
                max_length = line_length
                longest_line = stripped_line

    return longest_line

filename = "example.txt"

longest_line = longest_line_in_file(filename)
print(f"Η γραμμή με το μεγαλύτερο μήκος είναι: {longest_line}")
