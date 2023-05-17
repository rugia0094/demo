from words2numsrus import NumberExtractor


def main():
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()
        print(NumberExtractor().replace_groups(text))


if __name__ == "__main__":
    main()
