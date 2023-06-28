#i start by creating an Email class
#i set a class variable and default value, "has_been_read" to False.
#i then create a constructor and define the instance variables; 
#email_address, subject_line, email_content
class email:

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

#class method
    def mark_as_read(self):
        self.has_been_read = True

#here I initialize an empty list for the email objects
email_objects = []

#create 3 sample emails and add to inbox list.
#i put in each email an adress, subject and content.
#the append adds the emails to the empty list in "email_objects"
def populate_inbox_list():
    email_1 = email("fred@mail.com", "Shopping list", "Here is the list...")
    email_objects.append(email_1)
    email_2 = email("shania@mail.com", "Birthday invite", "Please RSVP for Friday 9th...")
    email_objects.append(email_2)
    email_3 = email("kate@mail.com", "Cake recipie", "Below is the recipe...")
    email_objects.append(email_3)

#below i set the email_menu. Also below I call the populate_inbox_list()
email_menu = True
populate_inbox_list()

# num with i enumerated so it will print numbers with the options automatically, starting number 1.
#num & enumerate adds numbers automatically to the list when it appears 
def sorting_emails():
    for num, i in enumerate(email_objects, 1):
        print(num, i.subject_line)

#below for unread emails, option 2, i have included a count mechinisum. 
#this counts how many unread emails there are and shows the user the total when propted. #user-friendly
def read_emails():
    count = 0
    for num, i in enumerate(email_objects, 1):
        if i.has_been_read == False:
            print(num, i.subject_line)
            count += 1
    print(f"You have {count} unread emails")

#menu prompt. this will ask the user to input one of the following options. if, elif & else clauses then run.
while True:
    user_input = input("Please choose one of the following options\n"
    "1: Read Email\n"
    "2: View your unread Emails\n"
    "3: Quit\n"
    "Please enter your choice here: ")

    if user_input == "1":
        sorting_emails()
        user_choice = int(input("Which email would you like to access? "))
        print(f'{email_objects[user_choice -1].email_address}\n {email_objects[user_choice -1].subject_line}\n {email_objects[user_choice -1].email_content}')
        email_objects[user_choice -1].mark_as_read()

    elif user_input == "2":
        read_emails()

    else:
        user_input == "3"
        print("Goodbye")
        break

#line 64. this marks the emails as read so it can be used for 
#line 67. accesses the functions on lines 44 to 50.

#for input "3", I have simply put a "break" so the programe will quit the while loop when the user has selected "quit". 
#I have also included a "goodbye" message alongside so the user gets some verification the programme has finished.