def screening(number: int) -> str:
    result_string = str(number) + "."
    if number % 3 == 0:
        result_string = result_string + " foo"
    if number % 5 == 0:
        result_string = result_string + " bar"
    if number % 7 == 0:
        result_string = result_string + " baz"
    return result_string

if __name__ == '__main__':
    i = 0
    for i in range(1, 51):
        print(screening(i))
    print("конец")