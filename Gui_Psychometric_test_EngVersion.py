import tkinter as tk
import sys

class App:
    def __init__(self, master):
        self.questions = {
            1: {
                "text": "What represents the workspace where you do your best work?",
                "options": {
                    1: "Chaotic Desk",
                    2: "Team Meeting",
                    3: "Cool Cafe",
                    4: "Organized Desk"
                },
                "score": 0,
                "score1": 0
            },
            2: {
                "text": "How would you describe your working hours?",
                "options": {
                    1: "My hours vary, depending on how i feel.",
                    2: "I don't have stable working hours, but I always work.",
                    3: "I work solid, but regular hours.",
                    4: "I always work long hours, especially when there's a deadline."
                },
                "score": 0,
                "score1": 1
            },
            3: {
                "text": "What's your reaction when someone calls a meeting",
                "options": {
                    1:"Doesn't matter as I'm unlikely to go.",
                    2:"I've got too much work to do for meetings.",
                    3:"Great! I'll be able to tell them about my new idea!",
                    4:"What? I probably called the meeting."
                },
                "score": 0,
                "score1": 2     
            },
            4: {
                "text": "How do you react to team-building activities?",
                "options": {
                    1:"Any excuse to avoid them!",
                    2:"I don't really like socializing!",
                    3:"I'm not excited but I usually like them once I get into them.",
                    4:"I love them! They're so important for the team culture."
                },
                "score": 0,
                "score1": 3     
            },
            5: {
                "text": "What would your colleagues say is your biggest strenght?",
                "options": {
                    1:"Solving difficult promblems.",
                    2:"Coming up with good ideas.",
                    3:"Convincing others to support the team.",
                    4:"Keeping the team on track and moving forward."
                },
                "score": 0,
                "score1": 4     
            },
            6: {
                "text": "Your biggest frustration at work is:",
                "options": {
                    1:"People that don't follow the system.",
                    2:"Doing monotonous work.",
                    3:"People thet get too far down the track before getting in.",
                    4:"New things being started when the last ones aren't finished."
                },
                "score": 0,
                "score1": 5     
            },
            7: {
                "text": "When there's an issue in your team, your natural response is:",
                "options": {
                    1:"I'm unlikely to make a fuss.",
                    2:"I get agitated and will argue my point strongly.",
                    3:"I get irritated - I just want to get back to the work.",
                    4:"I'm likely to call a meeting with the relevant parties and sort it out."
                },
                "score": 0,
                "score1": 6     
            },
            8: {
                "text": "What would you do if your team didn't want to implement your idea?",
                "options": {
                    1:"I would do nothing.",
                    2:"I would change the idea or add more.",
                    3:"I would be mad.",
                    4:"I would talk about my idea with the team again"
                },
                "score": 0,
                "score1": 7    
            },
            9: {
                "text": "What are you most passionate about?",
                "options": {
                    1:"Expanding my networks and increasing my influence.",
                    2:"Coming up with innovative new ideas.",
                    3:"Solving difficult problems.",
                    4:"Running an efficient, well-build team."
                },
                "score": 0,
                "score1": 8     
            },
            10: {
                "text": "What would you do if one of your team members doesn't work?",
                "options": {
                    1:"Nothing is not my problem.",
                    2:"Talk to the member.",
                    3:"Ask the member if he/she wants help.",
                    4:"Take his/her work and do it by my self."
                },
                "score": 0,
                "score1": 9     
            },
            # Add more questions as needed
        }

        self.current_question = 1

        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        self.line_label = tk.Label(master, text="______________________")
        self.line_label.pack()

        self.option_labels = {}
        for i in range(1, 5):#den to pirazoume
            self.option_labels[i] = tk.Label(master, text="")
            self.option_labels[i].pack()

        self.answer = tk.Entry(master)
        self.answer.pack()

        self.submit = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.update_question()

    def update_question(self):# Poses epiloges tha dixni
        question_data = self.questions[self.current_question]
        self.question_label.config(text="Question {}: {}".format(self.current_question, question_data["text"]))
        
        for i in range(1, 5):
            self.option_labels[i].config(text="{}. {}".format(i, question_data["options"][i]))

    def submit_answer(self):
        try:
            answer = int(self.answer.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid answer (1-4).")
            return

        if answer < 1 or answer >= 5:
            self.result_label.config(text="Please enter a valid answer (1-4).")
            return

        question_data = self.questions[self.current_question]
        question_data["score"] += answer#To counter gia tous pontous

        question_data = self.questions[self.current_question]
        question_data["score1"] += 1#To counter ton erotiseon pou apantithikan

        self.result_label.config(text="Your score for question {} is: {}".format(self.current_question, question_data["score"]))# Oi sinoliki ponti pou mazepse o xristis
        self.result_label.config(text="You total answers: {}".format( question_data["score1"]))# Oi sinolikes erotisis pou apantithikan

        self.current_question += 1

        if self.current_question > len(self.questions): #elegxei an apomenoun alles ervthseis gia na rvthsei alliws stamataei
            self.show_final_score()
        else:
            self.update_question()

        self.answer.delete(0, tk.END)

    def show_final_score(self):
        # Remove question widgets
        self.question_label.pack_forget()
        self.line_label.pack_forget()
        for i in range(1, 5):
            self.option_labels[i].pack_forget()
        self.answer.pack_forget()
        self.submit.pack_forget()

        ts = sum([question_data["score"] for question_data in self.questions.values()]) #ts = total_score

        global team_role
        team_role = ""

        if 10 <= ts and ts <= 15: #Telling the user what her/his role is.
            self.result_label.config(text="Your total score is: {}\nCongratulations! Your Role is Member!\nA member of the team is intended to do the work given to him/her,\n to attend every meeting and try to finds ideas and solutions to a problem that may exist in his/her work.\n".format(ts))
            team_role = "Member"
        
        elif 15 < ts and ts <= 25:
            self.result_label.config(text="Your total score is: {}\nCongratulations! Your Role is Creative!\nCreative types have a tendency to get caught up in their world of imagination, problem-solving, and conceptualizing.\n They might not always be the clearest communicators, diplomats or deadline-makers,\n but pair them with a savvy planner and you could almost spin gold!\n These creative types don’t just live in the likes of art and copywriting departments—they could be in accounting, sales, you name it.\n Every team benefits from a creative thinker in the group—someone who can deliver fresh ideas and solutions that let the team’s work stand out from the crowd.\nTo spot a creative, look for the original thinker, the person willing to turn the status quo on its head and come up with a new approach to a long-standing goal.\n".format(ts))
            team_role = "Creative"
        
        elif 25 < ts and ts <= 35:
            self.result_label.config(text="Your total score is: {}\nCongratulations! Your Role is Researcher!\nThe researcher types—who show up in sales, IT, support, marketing, content, etc.—are always asking questions and then finding their own answers.\n If you need more information to complete your project, it’s important to have a strong researcher who can get it for you.\n Their special talent: Researchers ask the overlooked questions that can avert a future impediment.\n This natural private eye knows the quickest way to the best resources and is the person everyone goes to with the most puzzling questions.\n".format(ts))
            team_role = "Researcher"
       
        else:
            self.result_label.config(text="Your total score is: {}\nCongratulations! Your Role is Leader!\nCommon wisdom: Before you begin any project, have an established leader. This person is responsible for mediating conflicts,\n facilitating communications between team members, and keeping everyone on course.\n The leader will schedule and guide the course of meetings, but that doesn’t mean being the only speaker, or leading all the meetings.\n A good leader knows how to delegate and let go of the reins.\nYou can recognize leadership qualities in people who have strong communications skills,\n a clear and expansive vision of the project’s end-result, and the ability to motivate others.\n".format(ts))
            team_role = "Leader"

        print(team_role)
        # Schedule the destruction of the window after 5 second
        #root.after(5000, root.destroy)
        # Create a bigger start button
        end_button = tk.Button(root, text="Close", font=("Arial", 12), command=sys.exit)
        end_button.pack(pady=10)
        
root = tk.Tk()
root.title("Psychometric test")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 850
window_height = 200
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}")
app = App(root)
root.mainloop()
