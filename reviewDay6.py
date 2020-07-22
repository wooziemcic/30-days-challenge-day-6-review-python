    n = int(input())

    for i in range(n):
        text = input()
        eve = ''
        odd = ''

        for j in range(len(text)):
            if j % 2 == 0:
                eve += text[j]
            else:
                odd += text[j]

        print('{} {}'.format(eve, odd))
