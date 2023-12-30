import os
from autocorrect import Speller

file1 = open('detected_text.txt','r')
text=file1.read()
file1.close()
spell = Speller()
correct_text = spell(text)
file2 = open('correct_text.txt','w')
file2.write(correct_text)
file2.close()


	
