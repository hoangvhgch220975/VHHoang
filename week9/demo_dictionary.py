english_words = {'hello':'xin chao', 'world':'the gioi', 'morning':'buoi sang', 'afternoon':'buoi chieu'}
print(english_words['hello'])

word = input('Enter a english word: ')
if word in english_words:
    print('Vietnamese translation: ', english_words[word])
else:
    print(f'Word {word} is not found in dictionary')
# add new key and value to dictionary
new_word = input('Enter a new word: ')
new_translation = input('Enter a new translation: ')
if new_word not in english_words:
    english_words[new_word] = new_translation   
    print(english_words)
else:
    print(f'{new_word} is already in dictionary')
#edit value of a key in the dictionary
edit_word = input('Enter a word you want to edit: ')
edit_translation = input('Enter a translation: ')
if edit_word in english_words:
    english_words[edit_word] = edit_translation
    print(english_words)
else:
    print(f'{edit_word} is not already in dictionary')
    english_words[edit_word] = edit_translation
    print(english_words)

#delete key and value in dictionary
delete_word = input('Enter word to delete: ')
if delete_word in english_words:
    del english_words[delete_word]  # similar : english_words.pop(delete_word)
    print(english_words)
else:
    print(f'{delete_word} is not in dictionary')

#count the number of occurrences of each word
content = "The highest-ranked of the eight World Cup debutants at 21st on the Fifa list, Portugal have experience at the back and exciting young talent up front. They also possess strength in depth,demonstrated by Neto making seven starting XI changes for Thursday match .While Vietnam were disorganised and open in defence, Portugal were constantly incisive down the flanks and full of creative ideas.They were two up inside 21 minutes and could have scored more as they dominated play all game."
words = content.split()
print(len(words))

word_count = {}
for i in words:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] += 1
print(len(word_count))
for i in word_count:
    print(f'{i}: {word_count[i]}')