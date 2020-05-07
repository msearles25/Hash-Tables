def word_count(s):
    # Implement me.
    d = {}
    ignoreThese = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', 
    '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    splitString = s.split(' ')

    for word in splitString:
        word = word.lower()

        for c in word:
            if c in ignoreThese:
                word = word.replace(c, '')
        if word == '':
            return d
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    # print(splitString)

    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))