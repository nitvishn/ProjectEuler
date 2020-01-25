def getAttempts():
    attempts = []
    for line in open("p079_keylog.txt", 'r'):
        attempts.append(line.replace('\n', ''))
    return attempts


def buildPrecedenceDict(attempts):
    precedence = {}
    for attempt in attempts:
        for i in range(len(attempt)):
            char = attempt[i]
            if precedence.get(char) == None:
                precedence[char] = {'before': set(), 'after': set()}
            if i > 0:
                precedence[char]['before'].add(attempt[i-1])
            if i < len(attempt) - 1:
                precedence[char]['after'].add(attempt[i+1])
    return precedence


def getFirstChar(precedence):
    for char in precedence:
        if len(precedence[char]['before']) == 0:
            return char
    raise ValueError


def removeChar(precedence, bad_char):
    new_precedence = {}
    for char in precedence:
        if char == bad_char:
            continue
        new_precedence[char] = {'before': [], 'after': []}
        if bad_char in precedence[char]['before']:
            new_precedence[char]['before'] = precedence[char]['before'] - {bad_char}
        else:
            new_precedence[char]['before'] = precedence[char]['before']
        new_precedence[char]['after'] = precedence[char]['after']
    return new_precedence


attempts = getAttempts()
precedence = buildPrecedenceDict(attempts)

password = ""
while len(precedence) > 0:
    firstChar = getFirstChar(precedence)
    password += firstChar
    precedence = removeChar(precedence, firstChar)

print(password)
