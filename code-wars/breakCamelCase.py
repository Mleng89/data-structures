def breakCamelCase(str)->str:
    result = ''
    for letter in str:
        if letter.isupper():
            result += " " + letter
        else:
            result += letter
    return result

print(breakCamelCase('camelCase')) # 'camel Case'
print(breakCamelCase('camelCaseTesting')) # 'camel Case Testing'