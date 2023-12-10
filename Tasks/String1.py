#!/usr/bin/python3
sentence = "{0} is dancing like a butterfly"
new_sentence = sentence.format('Kpakpo')
print("{:s} is dancing like a butterfly.".format('Kpakpo'))
print(new_sentence)
print()
sentence = "Dancing like {}"
print(sentence.format("mad"))
print()
# Alignment and width
text = "{:<10} {:^10} {:>10}"
formatted_text = text.format("Left", "Center", "Right")
print(formatted_text)
