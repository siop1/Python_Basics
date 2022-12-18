# WAP to create dictionary having word-meaning and take a user input to
# search in dictionary

_dict={
    'beautiful':'pleasing the senses or mind aesthetically',
    'principle':'rules',
    'deforestation':'cutting down trees'
}

print("######## Dictionary########")
print('Enter word to find its meaning')
while True:
    search=input('word: ').lower()
    try:
        print('meaning: ',_dict[search])
    except:
        print('No results found')