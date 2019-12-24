def get_type_of_sentence(sentense):
  last_char = sentense[-1]

  if last_char == "?":
    sentense_type = "question"
  else:
    sentense_type = "normal" 

  return "Sentence is " + sentense_type


print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question

#> Берём 6 символов от начала
print('Winterfell'[:6])  # => 'Winter'

#> Отбрасываем первые 6 символов
print('Winterfell'[6:])  # => 'fell'

def normalize_url_1(url):
    protocol_1 = "https://"
    protocol_2 = "http://"

    if protocol_1 in url: 
        return url

    if protocol_2 in url:
        host = url[len(protocol_2):] # отбрасываем первые символы
        return protocol_1 + host

    return protocol_1 + url

def normalize_url_2(url):
    https = 'https://'
    if url[:8] == https:
        return url
    else:
        if url[:7] == 'http://':
            return https + url[7:]
        else:
            return https + url