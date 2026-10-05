Function Main
    Declare String Name, Box1, Box2, Box3, currentPlayer, Winner
    Declare Integer moveCount, selectedBox, startChoice
    Declare Boolean gameOver, validMove

    Output "Hello, dear user! I am Flowy, your friendly game master! Today, we'll play a game of Tic-Tac-Toe. Are you ready- oh, what's your name?"
    Input Name
    Output "Wonderful name, " & Name & "! Let's start the game, shall we?"
    Assign Box1 = " "
    Assign Box2 = " "
    Assign Box3 = " "
    Assign moveCount = 0
    Assign gameOver = False
    Assign Winner = " "
    Assign selectedBox = 0
    Assign validMove = False
    Output "To start the game, let the universe decide who goes first!"
    Assign startChoice = Random(2) + 1
    If startChoice == 1
        Assign currentPlayer = "O"
        Output "The universe states that User will go first!"
    Else
        Assign currentPlayer = "X"
        Output "The universe states that Computer will go first!"
    End
    While gameOver == False AND moveCount < 3
        If currentPlayer == "O"
            Assign validMove = False
            While validMove == False
                Output "Enter box number (1, 2, or 3):"
                Input selectedBox
                If selectedBox == 1 AND Box1 == " "
                    Assign Box1 = "O"
                    Assign validMove = True
                Else
                    If selectedBox == 2 AND Box2 == " "
                        Assign Box2 = "O"
                        Assign validMove = True
                    Else
                        If selectedBox == 3 AND Box3 == " "
                            Assign Box3 = "O"
                            Assign validMove = True
                        Else
                            Output "Oh no, your input is invalid or the box is taken. Try again!"
                        End
                    End
                End
            End
        Else
            Assign validMove = False
            While validMove == False
                Assign selectedBox = Random(3) + 1
                If selectedBox == 1 AND Box1 == " "
                    Assign Box1 = "X"
                    Assign validMove = True
                Else
                    If selectedBox == 2 AND Box2 == " "
                        Assign Box2 = "X"
                        Assign validMove = True
                    Else
                        If selectedBox == 3 AND Box3 == " "
                            Assign Box3 = "X"
                            Assign validMove = True
                        End
                    End
                End
            End
            Output "Computer chose Box " & selectedBox & "!"
        End
        Assign moveCount = moveCount + 1
        If (Box1 == Box2) AND (Box2 == Box3) AND (Box1 != " ")
            Output "Players, here is the final board: [" & Box1 & "|" & Box2 & "|" & Box3 & "]"
            Output "GAME OVER! Congratulations to User!"
            Assign gameOver = True
        Else
            If moveCount == 3
                Output "Players, here is the final board: [" & Box1 & "|" & Box2 & "|" & Box3 & "]"
                Output "GAME OVER! It's a tie!"
                Assign gameOver = True
            Else
                If currentPlayer == "O"
                    Assign currentPlayer = "X"
                Else
                    Assign currentPlayer = "O"
                End
            End
        End
    End
End
