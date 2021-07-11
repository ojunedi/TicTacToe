from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TicTacToe")
root.iconbitmap("images/uzumaki_naruto.ico")

const = True
move_counter = 0
game_won = False


# defining the buttons
button1 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(0, 0, button1))
button2 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(0, 1, button2))
button3 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(0, 2, button3))

button4 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(1, 0, button4))
button5 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(1, 1, button5))
button6 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(1, 2, button6))

button7 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(2, 0, button7))
button8 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(2, 1, button8))
button9 = Button(root, text=" ", padx=25, pady=25, bg="white", command=lambda: my_click(2, 2, button9))

# printing out buttons
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

# determines if there is a winner
def who_won(game):
    global game_won
    global move_counter
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] != " ":  # row win condition
            print(f'player {game[i][0]} won')
            Button(root, text=game[i][0], bg="#66ff00").grid(row=i, column=0) # Turn winning squares #66ff00
            Button(root, text=game[i][1], bg="#66ff00").grid(row=i, column=1)
            Button(root, text=game[i][2], bg="#66ff00").grid(row=i, column=2)
            Label(root, text=f'player {game[i][0]} won', pady=10).grid(row=3, column=1) # Congrats statement
            game_won = True
            break
        elif game[0][i] == game[1][i] == game[2][i] and game[0][i] != " ":  # column win condition
            print(f'player {game[0][i]} won')
            Button(root, text=game[0][i], bg="#66ff00").grid(row=0, column=i)
            Button(root, text=game[1][i], bg="#66ff00").grid(row=1, column=i)
            Button(root, text=game[2][i], bg="#66ff00").grid(row=2, column=i)
            Label(root, text=f'player {game[0][i]} won', pady=10).grid(row=3, column=1)
            game_won = True
            break
        elif game[0][0] == game[1][1] == game[2][2] and game[1][1] != " ":  # diagonal \ win condition
            print(f'player {game[1][1]} won')
            for i in range(3):
                Button(root, text=game[i][i], bg="#66ff00").grid(row=i, column=i)
            Label(root, text=f'player {game[1][1]} won', pady=10).grid(row=3, column=1)
            game_won = True
            break
        elif game[0][2] == game[1][1] == game[2][0] and game[1][1] != " ":  # diagonal / win condition
            print(f'player {game[1][1]} Won')
            for i in range(3):
                for j in range(3):
                    if i + j == 2:
                        Button(root, text=game[i][j], bg="#66ff00").grid(row=i, column=j)
            Label(root, text=f'player {game[1][1]} won', pady=10).grid(row=3, column=1)
            game_won = True
            break
    if move_counter == 9 and not game_won: # tie statement
        Label(root, text=f'TIE GAME!', pady=10, bg="yellow").grid(row=3, column=1)


def my_click(x, y, buttonx): # updates buttons when clicked
    global const
    global move_counter
    if const and not game_won:
        buttonx = Button(root, text="X", padx=25, pady=25, bg="white")
        buttonx.grid(row=x, column=y)
        const = False
        game[x][y] = buttonx.cget("text")
        move_counter += 1
        who_won(game)
        return
    if not const and not game_won:
        buttonx = Button(root, text="O", padx=25, pady=25, bg="white")
        buttonx.grid(row=x, column=y)
        game[x][y] = buttonx.cget("text")
        move_counter += 1
        who_won(game)
        const = True
        return

# list of lists which is used to determine if there is a winner
game = [[button1.cget("text"), button2.cget("text"), button3.cget("text")],
        [button4.cget("text"), button5.cget("text"), button6.cget("text")],
        [button7.cget("text"), button8.cget("text"), button9.cget("text")]
        ]

root.mainloop()