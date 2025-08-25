try:
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")
    
    with open(input_file, 'r') as f:
        content = f.read()
    
    with open(output_file, 'w') as f:
        f.write(content.upper())
    
    print("File processed successfully!")
    
except FileNotFoundError:
    print("Error: File not found!")
except:
    print("An error occurred!")
