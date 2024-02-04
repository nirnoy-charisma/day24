PLACEHOLDER= "[names]"

with open("./invited_names.txt" ) as names_file:
     names= names_file.readlines()

with open("F:\mail_merger\.venv\starting_letter.docx") as letter_file:
    letter_contents= letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,name)
        print(new_letter)
        with open(f"F:\mail_merger\ReadyToSend\letter_fot_{stripped_name}.docx",mode="w") as finished_letter:
            finished_letter.write(new_letter)
