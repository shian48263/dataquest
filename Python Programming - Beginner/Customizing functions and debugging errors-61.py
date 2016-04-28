## 1. Overview ##

f = open("story.txt", 'r')
story_string = f.read()
vocabulary = open("dictionary.txt", "r").read()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(misspelled_words)

## 3. Optional arguments ##

def tokenize(text_string, special_characters, clean=False):
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    story_tokens = text_string.split(" ")
    return(story_tokens)

tokenized_story = tokenize(story_string, clean_chars, True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
misspelled_words = []

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)

## 4. Named arguments ##

clean_chars = [",", ".", "'", ";", "\n"]

# All different ways to express the same function call.
tokenized_story = tokenize(clean=True, text_string = story_string, special_characters = clean_chars)
# tokenized_story = tokenize(text_string = story_string, clean=True, special_characters = clean_chars)
# tokenized_story = tokenize(special_characters = clean_chars, text_string = story_string, clean=True)

# Both different ways to express the same function call.
tokenized_vocabulary = tokenize(text_string=vocabulary, special_characters=clean_chars)
# tokenized_vocabulary = tokenize(special_characters=clean_chars, text_string=vocabulary)

## 5. Practice: creating a more compact spell checker ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

def spell_check(vocabulary_file, text_file, special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    vocabularies = open(vocabulary_file, 'r').read()
    texts = open(text_file, 'r').read()
    tokenized_vocabulary = tokenize(vocabularies, special_characters)
    tokenized_text = tokenize(texts, special_characters, True)
    for text in tokenized_text:
        if text not in tokenized_vocabulary and text != '':
            misspelled_words.append(text)
    return(misspelled_words)

final_misspelled_words = spell_check('dictionary.txt', 'story.txt')
print(final_misspelled_words)

## 7. Syntax errors ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()
    
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

## 9. TypeError and ValueError ##

forty_two = 42
forty_two = 42

float("7")

## 11. Traceback ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()
    
    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)