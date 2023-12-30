import tkinter as tk
from tkinter import messagebox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

def close_window(event):
    confirmed = messagebox.askokcancel("Confirm Close", "Do you want to close the game?")
    if confirmed:
        main_window.destroy()
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

def logo():
    def close_window():
        logo_window.destroy()
    logo_path = "FIle--_-/My_Work/Python/Mini-Projects/logo_1071x1080.png"
    logo_window = tk.Tk()
    logo_window.overrideredirect(True)
    center_window(logo_window, 700,600)
    logo_window.configure(bg="white")
    logo = tk.PhotoImage(file=logo_path)

    logo_label = tk.Label(logo_window, image=logo, bg="white")
    logo_label.place(x=-188, y=-220)
    logo_window.after(4000, close_window)
    logo_window.mainloop() 
def reset_window(data):
    for widget in main_window.winfo_children():
        widget.destroy()
    def close_window(event):
        confirmed = messagebox.askokcancel("Confirm Close", "Do you want to close the game?")
        if confirmed:
            main_window.destroy()
    def scores_board(event):
        global scores_window
        if 'scores_window' in globals() and scores_window.winfo_exists():
            scores_window.destroy()
            event.widget["state"] = "normal"
        else:
            event.widget["state"] = "disabled"
            scores_window = tk.Toplevel(main_window)
            scores_window.title("Scores")
            if len(data[0]) >= 7 or len(data[2]) >=7:
                width = 350
                x = 490
                y = 170
            else:
                width = 250
                x = 400 
                y = 150
            height = 300
            screen_width = scores_window.winfo_screenwidth()
            screen_height = scores_window.winfo_screenheight()
            x_coordinate = int((screen_width / 2) - (width / 2) + x)
            y_coordinate = int((screen_height / 2) - (height / 2) - y)
            scores_window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')
            if data[1].lower() == 'x':
                player_x = data[0]
                player_y = data[2]
            else:
                player_x = data[2]
                player_y = data[0]
            x_score_label = tk.Label(
                scores_window,
                text=f"{player_x} (X): {scores['x']}",
                font=("Helvetica", 24)
            )
            o_score_label = tk.Label(
                scores_window,
                text=f"{player_y} (O): {scores['o']}",
                font=("Helvetica", 24)
            )
            tie_score_label = tk.Label(
                scores_window,
                text=f"Tie: {scores['tie']}",
                font=("Helvetica", 24)
            )

            x_score_label.pack(padx=30, pady=30)
            o_score_label.pack(padx=30, pady=30)
            tie_score_label.pack(padx=30, pady=30)
    def on_click(event):
        global main_window, turn, data_board, scores
        def check_chance():
            for i in range(rows):
                if data_board[i][0] == data_board[i][1] == data_board[i][2] != ' ':
                    return data_board[i][0]
            for i in range(columns):
                if data_board[0][i] == data_board[1][i] == data_board[2][i] != ' ':
                    return data_board[0][i]
            if data_board[0][0] == data_board[1][1] == data_board[2][2] != ' ' or data_board[0][2] == data_board[1][1] == data_board[2][0] != ' ':
                return data_board[1][1]
            return " "    
        row, col = event.widget.grid_info()["row"] - 1, event.widget.grid_info()["column"]
        if event.widget["text"] == " ":
            if turn % 2 == 0:
                event.widget.configure(text="X")
            else:
                event.widget.configure(text="O")
            turn += 1
            data_board[row][col] = event.widget["text"]        
            result = check_chance()
            if data[1].lower() == 'x':
                player_x = data[0]
                player_o = data[2]
            else:
                player_x = data[2]
                player_o = data[0]
            if result != " ":
                if data[1].lower() == result.lower() and data[1].lower() == 'x':
                    winner = player_x
                if data[3].lower() == result.lower() and data[3].lower() == 'o':
                    winner = player_o
                if data[1].lower() == result.lower() and data[1].lower() == 'o':
                    winner = player_o
                if data[3].lower() == result.lower() and data[3].lower() == 'x':
                    winner = player_x
                scores[f"{result.lower()}"] += 1
                ans = messagebox.askyesno("Result", f"{winner} ({result}) Won! 🏆, Want to play again?")
                if ans:
                    data_board = [[' ' for _ in range(columns)] for _ in range(rows)]
                    turn = 0
                    reset_window(data)
                else:
                    main_window.destroy()
            
                return
            elif " " not in data_board[0] and " " not in data_board[1] and " " not in data_board[2]:
                scores["tie"] += 1
                ans = messagebox.askyesno("Result", "Its A Tie 🟡, Want to play again?")
                if ans:
                    
                    data_board = [[' ' for _ in range(columns)] for _ in range(rows)]
                    turn = 0
                    reset_window(data)
                else:
                    main_window.destroy()

    main_window.title("Tic Tac Toe")
    center_window(main_window, 625, 635)
    main_window.configure(bg="#212F3D")
    main_window.resizable(False, False)

    header = tk.Label(
        master=main_window,
        text="Tic Tac Toe",
        font=("Helvetica", 34),
        foreground="white",
        background="#212F3D"
    )
    header.grid(row=0, column=0, padx=20, pady=20, sticky="n")
    def GameBoard():
        game_board_frame = tk.Frame(
            master=main_window,
            background="blue"
        )
        for row in range(rows):
            for column in range(columns):
                block = tk.Button(
                    master=game_board_frame,
                    text=" ",
                    font=("Helvetica", 34),
                    borderwidth=3,
                    foreground="#839192",
                    background="#212F3D",
                    relief=tk.RIDGE,
                    width=7,
                    height=3
                    )
                block.grid(row=row + 1, column=column)
                block.bind("<Button-1>", on_click)
        game_board_frame.grid()
        scores_button = tk.Button(
            main_window, 
            text="Scores", 
            state="normal",
            font=("Helvetica", 14),
            width=10,
            height=2
            )
        scores_button.grid(padx=5,pady=5)
        scores_button.bind("<Button-1>", scores_board)

        return game_board_frame

    GameBoard()
    main_window.bind("<Control-z>", close_window)
    main_window.mainloop()
def initial_window():
    def data_from_entry(entry):
        data = entry.get()
        return data

    def validate_name_input(event):
        name = event.widget.get()
        if len(name) < 3 or len(name) > 10:
            event.widget.configure(background='pink')
        else:
            event.widget.configure(background='#A7FA97')    

    def validate_choice_input(event):
        choice = event.widget.get()
        valid_choices = {'x', 'o'}
        if choice not in valid_choices :
            event.widget.configure(background='pink')
        else:
            event.widget.configure(background='#A7FA97')    

    def submit():
        name_1 = data_from_entry(player_1[0]).capitalize()
        name_2 = data_from_entry(player_2[0]).capitalize()
        choice_1 = data_from_entry(player_1[1]).lower()
        choice_2 = data_from_entry(player_2[1]).lower()
        
        checks = []
        errors = []

        def set_background(entry, valid):
            entry.configure(background='#A7FA97' if valid else 'pink')

        def show_error_messages(messages):
            formatted_messages = "\n".join(messages)
            messagebox.showerror("Error", formatted_messages)

        def generate_error_messages(errors):
            error_messages = []
            if "same_names" in errors:
                error_messages.append("Names should not be the same")
            if "player1_long_name" in errors:
                error_messages.append("Player 1: Name should not exceed 10 characters")
            if "player2_long_name" in errors:
                error_messages.append("Player 2: Name should not exceed 10 characters")
            if "player1_short_name" in errors:
                error_messages.append("Player 1: Name should be at least 3 characters")
            if "player2_short_name" in errors:
                error_messages.append("Player 2: Name should be at least 3 characters")
            if "choice_wrong" in errors:
                error_messages.append("Choose 'X' for one player and 'O' for the other")
            return error_messages

        if name_1 and name_2 and choice_1 and choice_2:
            if all(len(name) <= 10 and len(name) >= 3 for name in (name_1, name_2)) and name_1 != name_2:
                set_background(player_1[0], True)
                set_background(player_2[0], True)
                checks.append("names")
            else:
                if name_1 == name_2:
                    errors.append("same_names")
                if len(name_1) > 10:
                    errors.append("player1_long_name")
                if len(name_2) > 10:
                    errors.append("player2_long_name")
                if len(name_1) < 3:
                    errors.append("player1_short_name")
                if len(name_2) < 3:
                    errors.append("player2_short_name")

            valid_choices = {'x', 'o'}
            if choice_1 in valid_choices and choice_2 in valid_choices and choice_1 != choice_2:
                set_background(player_1[1], True)
                set_background(player_2[1], True)
                checks.append("choice")
            else:
                errors.append("choice_wrong")
                if choice_1 in valid_choices and choice_2 in valid_choices and choice_1 == choice_2:
                    set_background(player_1[1], False)
                    set_background(player_2[1], False)
                else:
                    set_background(player_1[1], choice_1 in valid_choices)
                    set_background(player_2[1], choice_2 in valid_choices)

            if errors:
                error_messages = generate_error_messages(errors)
                show_error_messages(error_messages)
                
        else:
            messagebox.showerror("Error", "Fill in all details")
        
        try:
            if checks[0] and checks[1]:
                data = [name_1, choice_1,name_2, choice_2]
                reset_window(data)
        except IndexError:
            pass

    main_window.title("Users Info")
    center_window(main_window, 900, 350)
    main_window.resizable(False, False)

    Wel_Label = tk.Label(
        master=main_window,
        text="Enter The Following Details:",
        font=("Helvetica", 24)
    )
    Wel_Label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    name_Label = tk.Label(
        master=main_window,
        text="Players Names: (Not More Than 10 Letters)",
        font=("Helvetica", 14)
    )
    name_Label.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="w")

    choice_Label = tk.Label(
        master=main_window,
        text="Players Choice: [ X / O ]",
        font=("Helvetica", 14)
    )
    choice_Label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

    def players_frames(num):
        player_frame = tk.Frame()

        player_Label = tk.Label(
            master=player_frame,
            text=f"Player {num}:",
            font=("Arial", 20),
            width=10
        )
        player_Label.grid(row=0, column=0, padx=(20, 5), sticky="w")

        player_arrow = tk.Label(
            master=player_frame,
            text="---->",
            font=("Arial", 20)
        )
        player_arrow.grid(row=0, column=1, padx=(5, 20), pady=10, sticky="w")

        player_entry_name = tk.Entry(
            master=player_frame,
            font=("Arial", 20)
        )
        player_entry_choice = tk.Entry(
            master=player_frame,
            font=("Arial", 20),
            width=2
        )
        player_entry_name.grid(row=0, column=2, padx=(20, 5), pady=10, sticky="w")
        player_entry_choice.grid(row=0, column=3, padx=100, pady=10, sticky="w")
        player_arrow = tk.Label(
            master=player_frame,
            text="---->",
            font=("Arial", 20)
        )
        player_arrow.grid(row=0, column=3, padx=(25, 20), pady=10, sticky="w")
        player_frame.grid()

        return player_entry_name, player_entry_choice

    tk.Frame(
        master=main_window
    )
    player_1 = players_frames(num=1)
    player_2 = players_frames(num=2)

    submit_button = tk.Button(
        text="Submit",
        font=("Arial", 20),
        foreground="#F2F2F2",
        background="#23F92C",
        width=20,
        height=2,
        command=submit,
        relief=tk.RAISED
    )

    submit_button.grid(row=5, column=0, padx=(45, 10), pady=35, sticky="n")
    player_1[0].bind('<KeyRelease>', validate_name_input)
    player_2[0].bind('<KeyRelease>', validate_name_input)
    player_1[1].bind('<KeyRelease>', validate_choice_input)
    player_2[1].bind('<KeyRelease>', validate_choice_input)

    main_window.bind("<Control-z>", close_window)
    main_window.mainloop()
turn = 0
rows = 3
columns = 3
scores = {
    "x": 0,
    "o": 0,
    "tie": 0
}
data_board = [[' ' for _ in range(columns)] for _ in range(rows)]
logo()
main_window = tk.Tk()
data = initial_window()