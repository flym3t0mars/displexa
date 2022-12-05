import imdb

media=[]
s= ""

def isearch(a):
	iq = imdb.IMDb()
	search = iq.search_movie(a)
	for i in range(len(search)):
		media.append(search[i])
		global s
		s+=(f'{[i+1]} {media[i]} \n')
	print(s)
	print('pick a number between 1-20')
	t=int(input('Number: '))
	print(f'you picked: {media[t-1]}')
	# how to get tt3778644
	print(f'tt{media[t-1].movieID}')
		
def main():
	isearch(input('movie: '))
	# print(s)

if __name__=="__main__":
	main()
