import re

def tokenize(json_string):
    tokens = []
    pattern = r'\s*(?:(\{|\}|:|,|\[|\])|("([^"\\]*(\\.)?)*"|\d+|true|false|null)?)'
    for match in re.finditer(pattern, json_string):
        token = match.group(0).strip()
        if token:
            tokens.append(token)
    return tokens

def parse_value(tokens, index):
    token = tokens[index]
    if token == '{':
        return parse_object(tokens, index)
    elif token == '[':
        return parse_array(tokens, index)
    elif token[0] == '"': 
        return token[1:-1], index + 1
    elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  
        return float(token), index + 1
    elif token == 'true':
        return True, index + 1
    elif token == 'false':
        return False, index + 1
    elif token == 'null':
        return None, index + 1
    else:
        raise ValueError(f"Unexpected token: {token}")

def parse_object(tokens, index):
    obj = {}
    index += 1  
    while index < len(tokens):
        if tokens[index] == '}':
            return obj, index + 1
        key = tokens[index]
        index += 1
        if tokens[index] != ':':
            raise ValueError("Expected ':' after key")
        index += 1 
        value, index = parse_value(tokens, index)
        obj[key[1:-1]] = value 
        if tokens[index] == '}':
            return obj, index + 1
        if tokens[index] != ',':
            raise ValueError("Expected ',' or '}'")
        index += 1
    raise ValueError("Expected '}'")

def parse_array(tokens, index):
    arr = []
    index += 1 
    while index < len(tokens):
        if tokens[index] == ']':
            return arr, index + 1
        value, index = parse_value(tokens, index)
        arr.append(value)
        if tokens[index] == ']':
            return arr, index + 1
        if tokens[index] != ',':
            raise ValueError("Expected ',' or ']'")
        index += 1  
    raise ValueError("Expected ']'")

def parse(json_string):
    tokens = tokenize(json_string)
    value, index = parse_value(tokens, 0)
    if index != len(tokens):
        raise ValueError("Extra tokens after valid JSON")
    return value

f = open("jsonParser/test.txt", "r")
test_json = f.read()
try:
    result = parse(test_json)
    print("Parsed JSON:", result)
except ValueError as e:
    print("Error:", e)

