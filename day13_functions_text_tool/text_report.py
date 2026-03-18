def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def count_lines(text):
    lines = text.splitlines()
    return len(lines)

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    return len(text)

def create_report(text):
    lines_count = count_lines(text)
    words_count = count_words(text)
    chars_count = count_chars(text)

    report = ""
    report += "TEXT REPORT\n"
    report += "===========\n"
    report += f"Lines: {lines_count}\n"
    report += f"Words: {words_count}\n"
    report += f"Characters: {chars_count}\n"

    return report

def save_report(filename, report_text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report_text)

def main():
    input_file = "sample.txt"
    output_file = "report.txt"

    text = read_file(input_file)
    report = create_report(text)

    print(report)
    save_report(output_file, report)

main()

def create_report(text, source_name):
    lines_count = count_lines(text)
    words_count = count_words(text)
    chars_count = count_chars(text)

    report = ""
    report += "TEXT REPORT\n"
    report += "===========\n"
    report += f"Source file: {source_name}\n"
    report += f"Lines: {lines_count}\n"
    report += f"Words: {words_count}\n"
    report += f"Characters: {chars_count}\n"

    return report

def count_letter_a(text):
    return text.lower().count("a")