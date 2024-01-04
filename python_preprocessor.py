
def python_detector(text_input):
    import re
    specific_words = ["=", "==", "def & :", "()", "if & :", "with & :", "for & :", "while & :", "else & :","break","contineo","return"]

    input_file = text_input
    output_files = ""
    output_file = ""
    # input_file = "text2.txt"

    # output_file = "output2.txt"

    def has_specific_words(line, words):
        for word in words:
            if all(part in line for part in word.split(" & ")):
                return True
        return False

    def is_import_line(line):
        return line.startswith("import") or ("from" in line and "import" in line)

    def has_word_ending_with_parentheses(line):
        return bool(re.search(r'\S+\s*\([^)]*\)', line))

    # with open(input_file, "r") as in_file:
    #     input_text = in_file.read()

    # with open(output_file, "w") as out_file:
    lines = text_input.split('\n')

    for line in lines:
        line = re.sub(r"^\d+", "", line)
        if has_specific_words(line, specific_words):
            output_file = line
        elif is_import_line(line):
            output_file = line
        elif has_word_ending_with_parentheses(line):
            output_file = line
        output_files = f"{output_files}\n{output_file}"
        output_file = ""
        
        
    return output_files
