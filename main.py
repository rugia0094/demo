from words2numsrus import NumberExtractor

def replace(text):
    return NumberExtractor().replace_groups(text)


def main():
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()
        print(replace(text))


if __name__ == "__main__":
    main()
