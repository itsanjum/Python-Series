# Write a program to fill in a letter template given below with name and date.


letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''


a=letter.replace("<|Name|>","Anjum").replace("<|Date|>","18 May 2025")
print(a)