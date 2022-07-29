import textwrap

def wrap(string, max_width):
    s_wrap_list = textwrap.wrap(string, max_width)
    new_string = "\n".join(s_wrap_list)
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)