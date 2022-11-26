def tic_tac_toe(inputs):
	for i in range(3):
		#horz
		if inputs[i][0] == "X" and inputs[i][1] == "X" and inputs[i][2] == "X":
			return "Player 1 wins"
		elif inputs[i][0] == "O" and inputs[i][1] == "O" and inputs[i][2] == "O":
			return "Player 2 wins"
		
		#vert
		if inputs[0][i] == "X" and inputs[1][i] == "X" and inputs[2][i] == "X":
			return "Player 1 wins"
		elif inputs[0][i] == "O" and inputs[1][i] == "O" and inputs[2][i] == "O":
			return "Player 2 wins"
			
	#cross
	x = inputs[0][0] == "X" and inputs[1][1] == "X" and inputs[2][2] == "X"
	y = inputs[0][0] == "O" and inputs[1][1] == "O" and inputs[2][2] == "O"
	if x == True:
		return "Player 1 wins"
	elif y == True:
		return "Player 2 wins"
	else:
		x = inputs[0][2] == "X" and inputs[1][1] == "X" and inputs[2][0] == "X"
		y = inputs[0][2] == "O" and inputs[1][1] == "O" and inputs[2][0] == "O"
		if x == True:
			return "Player 1 wins"
		elif y == True:
			return "Player 2 wins"
		else:
			return "It's a Tie"