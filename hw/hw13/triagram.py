import random

f = open('sherlock.txt', 'r')
words = []
triagram = {}
lines = f.readlines()
# Goes through each line and replaces necessary characters with
# blank or space. Then it splits them in to a list.
for l in lines:
    l = l.replace('_', '').replace('"', '')
    l = l.replace(',', '').replace('(', '').replace(')', '')
    l = l.replace('--', ' ').replace(':', '').replace('[', '')
    l = l.replace("'", "").replace(']', '').replace(';', '')
    l = l.replace('-', ' ').replace('\n', '')
    words += l.split()
# Create values as list to hold more than 1 value for keys
for(j, w) in enumerate(words):
    if(j < len(words) - 1):
        triagram[(w, words[j + 1])] = []
# Append values to keys
for(i, word) in enumerate(words):
    if(i < len(words) - 2):
        triagram[(word, words[i + 1])].append(words[i + 2])

# Find starting point of the story
start = random.sample(triagram.items(), 1)
start_1 = start[0][0][0]
start_2 = start[0][0][1]
v = random.choice(triagram[(start_1, start_2)])
pref = ['Jr.', 'Sr.', 'Mr.', 'Mrs.', 'Ms.']
addr = ['St.', 'Ave.', 'Ct.', 'Blvd.', 'U.S.']
# Algorithm that makes the story
# Currently the algorithm uses upto 300 words but will keep going
# until it finds the next stopping point('.', '?', '!') after 300
# words. Otherwise, it will keep adding the next words to the story
index = 0
story = "...%s %s" % (start_1, start_2)
while(True):
    # Checks for conditions for stopping
    if(index > 300 and ("." in v or "!" in v or "?" in v) and
            v not in pref and v not in addr):
        # It will add the last value before breaking out of the loop
        story = " ".join([story, v])
        break
    else:
        # Adds the last value to the story
        # Replaces 1st key with old 2nd key
        # Replaces 2nd key with old value
        # Randomly chooses new value to be added to the story
        story = " ".join([story, v])
        start_1 = start_2
        start_2 = v
        # If the next value is empty which means it reached the end of the
        # story line, it will break out of the loop even if there is not enough
        # for 300 word story
        if (triagram[(start_1, start_2)] == []):
            break
        else:
            v = random.choice(triagram[(start_1, start_2)])
    index += 1

print(story)
