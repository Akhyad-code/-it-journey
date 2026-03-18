def print_line():
    print("-" * 30)

def show_title(title):
    print_line()
    print(title)
    print_line()

def count_chars(text):
    return len(text)

def to_upper_text(text):
    return text.upper()

show_title("МОЙ ТЕСТ")
print(count_chars("hello"))
print(to_upper_text("python for cyber"))