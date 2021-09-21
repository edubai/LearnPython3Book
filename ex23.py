#https://www.w3schools.com/python/ref_string_encode.asp
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    #if there is line (true) continue to loop, calling itself.
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    #strip() will remove spaces, used here to get rid of /n
    next_lang = line.strip()
    #encode strings
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #decode bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)
