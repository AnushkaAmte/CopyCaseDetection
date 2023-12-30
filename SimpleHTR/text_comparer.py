from difflib import SequenceMatcher

with open('correct_text.txt') as file3, open('sample.txt') as file4:
    file3_data = file3.read()
    file4_data = file4.read()
    similarity = SequenceMatcher(None, file3_data, file4_data).ratio()
    print(f"The contents are {similarity*100} common.")
