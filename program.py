
flaga=0
x =int(input())
for i in range(2, x):
	if x%i==0:
		print("nie_pietrwsza")
		flaga=1;
		break;
if flaga==0:
	print("pierwsza")

