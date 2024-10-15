import sys

def count_words(filename):
    try:
        f = open(filename, 'r')
        text = f.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def count_characters(filename):
    count = 0
    try:
        f = open(filename, 'r')
        text = f.read()
        words = text.split()
        for word in words:
            count = count + len(word)
        return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def count_lines(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2 | len(sys.argv) > 3:
        print("Usage: ccwc [-c | -l | -w | -b] <filename>")
    if len(sys.argv) == 2:
        print("\t" + str(count_characters(sys.argv[1])) + "\t" + str(count_lines(sys.argv[1])) + "\t" + str(count_words(sys.argv[1])) + "\t" + sys.argv[1])
    if len(sys.argv) == 3:
        if(sys.argv[1] == '-c'):
            print("\t" + str(count_characters(sys.argv[2])) + "\t" + sys.argv[2])
        elif(sys.argv[1] == '-l'):
            print("\t" + str(count_lines(sys.argv[2])) + "\t" + sys.argv[2])
        elif(sys.argv[1] == '-b'):
            print("\t" + str(count_characters(sys.argv[2])) + "\t" + sys.argv[2])
        elif(sys.argv[1] == '-w'):
            print("\t" + str(count_words(sys.argv[2])) + "\t" + sys.argv[2])
        else:
            print("Usage: ccwc [-c | -l | -w | -b] <filename>")