# l = [1,2,3,4,5,6]
# print(l[1:5])

# a = [[0,0,0],
# 	 [0,0,0],
# 	 [0,0,0],]

# a[2][2] = 33

# b = print("   a  b  c")
# j = "a"
# for count, x in enumerate(a):
# 	print(count, x)

game = [[0,0,0],
		[0,0,0],
		 [0,0,0],]

def game_board(player=0, row=0, colume=0, justdisplay=False):
	print("   0  1  2")
	if not justdisplay:
		game[row][colume] = player
		for count, row in enumerate(game):
			print(count, row)		 

game_board(0, 0, 0, False)
game_board(player=1, row=2, colume=1)