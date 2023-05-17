from words2numsrus import NumberExtractor

def main():
    extractor = NumberExtractor()

    print(extractor.replace_groups('сто одиннадцать тысяч роз'))


if __name__ == "__main__":
    main()
