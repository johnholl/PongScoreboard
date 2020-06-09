from tkinter import *


player1 = input("Opponent 1: ")
player2 = input("Opponent 2: ")

score1 = 0
score2 = 0
winner = ""

game_is_over = False

while not game_is_over:
	print("Score is: " + str(score1) + " to " + str(score2))
	point_winner = input("Who won the last point? ")
	if point_winner == "1":
		score1 += 1
	elif point_winner == "2":
		score2 += 1

	if score1 >= 11 and (score1 - score2) > 1:
		game_is_over = True
		winner = player1
	elif score2 >= 11 and (score2 - score1) > 1:
		game_is_over = True
		winner = player2

print("Player " + winner + " won the game!")

