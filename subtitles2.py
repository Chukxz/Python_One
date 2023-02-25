data = [{'word': 'average', 'startTime': '5.11s', 'endTime': '5.58s'}, {'word': 'household', 'startTime': '5.59s', 'endTime': '6.04s'}, {'word': 'income', 'startTime': '6.05s', 'endTime': '6.42s'}, {'word': 'is', 'startTime': '6.43s', 'endTime': '6.56s'}, {'word': 'up', 'startTime': '6.57s', 'endTime': '6.76s'}, {'word': 'ten', 'startTime': '6.77s', 'endTime': '6.98s'}, {'word': 'percent', 'startTime': '6.99s', 'endTime': '7.41s'}, {'word': 'from', 'startTime': '7.42s', 'endTime': '7.6s'}, {'word': 'four', 'startTime': '7.61s', 'endTime': '7.86s'}, {'word': 'years', 'startTime': '7.87s', 'endTime': '8.1s'}, {'word': 'ago', 'startTime': '8.11s', 'endTime': '8.52s'}, {'word': 'and', 'startTime': '8.77s', 'endTime': '9.0s'}, {'word': 'our', 'startTime': '9.01s', 'endTime': '9.1s'}, {'word': 'customers', 'startTime': '9.11s', 'endTime': '9.58s'}, {'word': 'are', 'startTime': '9.59s', 'endTime': '9.66s'}, {'word': 'spending', 'startTime': '9.67s', 'endTime': '10.14s'}, {'word': 'twenty', 'startTime': '10.15s', 'endTime': '10.47s'}, {'word': 'percent', 'startTime': '10.48s', 'endTime': '10.88s'}, {'word': 'more', 'startTime': '10.89s', 'endTime': '11.18s'}, {'word': 'per', 'startTime': '11.19s', 'endTime': '11.32s'}, {'word': 'transaction', 'startTime': '11.33s', 'endTime': '12.12s'}, {'word': 'nearly', 'startTime': '12.53s', 'endTime': '13.04s'}, {'word': 'everyone', 'startTime': '13.05s', 'endTime': '13.5s'}, {'word': 'surveyed', 'startTime': '13.51s', 'endTime': '13.96s'}, {'word': 'is', 'startTime': '13.97s', 'endTime': '14.08s'}, {'word': 'employed', 'startTime': '14.09s', 'endTime': '14.56s'}, {'word': 'in', 'startTime': '14.57s', 'endTime': '14.66s'}, {'word': 'a', 'startTime': '14.67s', 'endTime': '14.74s'}, {'word': 'professional', 'startTime': '14.75s', 'endTime': '15.3s'}, {'word': 'or', 'startTime': '15.31s', 'endTime': '15.46s'}, {'word': 'managerial', 'startTime': '15.47s', 'endTime': '16.1s'}, {'word': 'occupation', 'startTime': '16.11s', 'endTime': '16.8s'}]

timestamp = []
transcript = []
tokens = []
start = 0.0
offset_threshold = 0.1
language = 'en-US'

def get_seconds(nanoseconds):
    return round(float(nanoseconds.replace('s','')), 2)


def join_words(words, lang):
    if lang == 'ja-JP' or lang == 'th-TH':
        return ''.join(words)

    return ' '.join(words)

if len(data) == 1:
    timestamp.append({'segment': data[0]['word'], 'start': get_seconds(data[0]['startTime']), 'end': get_seconds(data[0]['endTime'])})
else:
    for i in range(0, len(data) - 1):
        # calculate differences
        difference = round(get_seconds(data[i + 1]['startTime']) - get_seconds(data[i]['endTime']),2)
        print(difference)

        # set start if tokens is empty indicating start of sentence
        if not tokens:
            start = get_seconds(data[i]['startTime'])
        tokens.append(data[i]['word'])

        # build sentence if exceeds threhold, clear tokens and set start to next offset
        if difference >= offset_threshold:
            timestamp.append({'segment': join_words(tokens, language), 'start': start, 'end': get_seconds(data[i]['endTime'])})
            tokens = []
            start = get_seconds(data[i + 1]['startTime'])
        # reached the second last word, add in last word and break out of loop
        # break is not needed here unless you loop using len(data) instead of len(data) - 1
        elif i == len(data) - 2:
            tokens.append(data[i + 1]['word'])
            timestamp.append({'segment': join_words(tokens, language), 'start': start, 'end': get_seconds(data[i + 1]['endTime'])})
            break

print(timestamp)
