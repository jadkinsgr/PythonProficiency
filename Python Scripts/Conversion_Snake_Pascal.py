def stringToPascal(convertString):
    """Accepts a string, and converts it to a PascalCaseString."""
    
    # Replace underscores and hyphens with spaces for uniform splitting
    tempString = convertString.replace("_", " ").replace("-", " ")
    stringParts = tempString.split()
    
    # Capitalize each word
    stringParts = [word.capitalize() for word in stringParts if word.isalpha()]
    
    # Combine into PascalCase
    pascalCaseString = "".join(stringParts)
    
    return pascalCaseString

# Example usage
print(stringToPascal('bronzeTAblE'))          # BronzeTable
print(stringToPascal('bronze_tablE'))         # BronzeTable
print(stringToPascal('bronze-table-123'))     # BronzeTable
print(stringToPascal('bronze---table'))       # BronzeTable


def stringToSnake(convertString):
    """Accepts a string, and converts it to a snake_case_string."""
    
    # Replace underscores and hyphens with spaces for uniform splitting
    tempString = convertString.replace("_", " ").replace("-", " ")
    stringParts = tempString.split()
    
    # Convert each word to lowercase
    stringParts = [word.lower() for word in stringParts if word.isalpha()]
    
    # Combine into snake_case
    snakeCaseString = "_".join(stringParts)
    
    return snakeCaseString

# Example usage
print(stringToSnake('bronzeTAblE'))          # bronze_table
print(stringToSnake('bronze_tablE'))         # bronze_table
print(stringToSnake('bronze-table-123'))     # bronze_table
print(stringToSnake('bronze---table'))       # bronze_table