data = [{"Word":"average","Offset":51100000,"Duration":4700000},{"Word":"household","Offset":55900000,"Duration":4500000},{"Word":"income","Offset":60500000,"Duration":3700000},{"Word":"is","Offset":64300000,"Duration":1300000},{"Word":"up","Offset":65700000,"Duration":1900000},{"Word":"ten","Offset":67700000,"Duration":2100000},{"Word":"percent","Offset":69900000,"Duration":4200000},{"Word":"from","Offset":74200000,"Duration":1800000},{"Word":"four","Offset":76100000,"Duration":2500000},{"Word":"years","Offset":78700000,"Duration":2300000},{"Word":"ago","Offset":81100000,"Duration":4100000},{"Word":"and","Offset":87700000,"Duration":2300000},{"Word":"our","Offset":90100000,"Duration":900000},{"Word":"customers","Offset":91100000,"Duration":4700000},{"Word":"are","Offset":95900000,"Duration":700000},{"Word":"spending","Offset":96700000,"Duration":4700000},{"Word":"twenty","Offset":101500000,"Duration":3200000},{"Word":"percent","Offset":104800000,"Duration":4000000},{"Word":"more","Offset":108900000,"Duration":2900000},{"Word":"per","Offset":111900000,"Duration":1300000},{"Word":"transaction","Offset":113300000,"Duration":7900000},{"Word":"nearly","Offset":125300000,"Duration":5100000},{"Word":"everyone","Offset":130500000,"Duration":4500000},{"Word":"surveyed","Offset":135100000,"Duration":4500000},{"Word":"is","Offset":139700000,"Duration":1100000},{"Word":"employed","Offset":140900000,"Duration":4700000},{"Word":"in","Offset":145700000,"Duration":900000},{"Word":"a","Offset":146700000,"Duration":700000},{"Word":"professional","Offset":147500000,"Duration":5500000},{"Word":"or","Offset":153100000,"Duration":1500000},{"Word":"managerial","Offset":154700000,"Duration":6300000},{"Word":"occupation","Offset":161100000,"Duration":6900000}]

timestamp = []
transcript = []
tokens = []
start = 0.0
offset_threshold = 0.1
language = 'en-US'


def get_seconds(nanoseconds):
    return round(nanoseconds / 10000000, 2)


def join_words(words, lang):
    if lang == 'ja-JP' or lang == 'th-TH':
        return ''.join(words)

    return ' '.join(words)


if len(data) == 1:
    timestamp.append({'segment': data[0]['Word'], 'start': get_seconds(data[0]['Offset']), 'end': get_seconds(data[0]['Offset'] + data[0]['Duration'])})
else:
    for i in range(0, len(data) - 1):
        # calculate differences
        difference = get_seconds(data[i + 1]['Offset'] - (data[i]['Offset'] + data[i]['Duration']))
        # print(difference)

        # set start if tokens is empty indicating start of sentence
        if not tokens:
            start = get_seconds(data[i]['Offset'])
        tokens.append(data[i]['Word'])

        # build sentence if exceeds threhold, clear tokens and set start to next offset
        if difference >= offset_threshold:
            timestamp.append({'segment': join_words(tokens, language), 'start': start, 'end': get_seconds(data[i]['Offset'] + data[i]['Duration'])})
            tokens = []
            start = get_seconds(data[i + 1]['Offset'])
        # reached the second last word, add in last word and break out of loop
        # break is not needed here unless you loop using len(data) instead of len(data) - 1
        elif i == len(data) - 2:
            tokens.append(data[i + 1]['Word'])
            timestamp.append({'segment': join_words(tokens, language), 'start': start, 'end': get_seconds(data[i + 1]['Offset'] + data[i + 1]['Duration'])})
            break

print(timestamp)