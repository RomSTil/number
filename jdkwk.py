def generate():
    for i in range(3**8):
        combination = ""
        for j in range(8):
            operators = ('+', '-', ' ')
            operator = operators[i // (3**j) % 3]
            combination += str(j+1) + operator

        combination += "9"
        
        print(combination)
    
generate()

