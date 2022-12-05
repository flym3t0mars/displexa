import imdb

media=[]
s= ""

#for i in range(len(n)):
#...     s+=(f'{i+1} {n[i]}\n')


def isearch(a):
	iq = imdb.IMDb()
	search = iq.search_movie(a)
	for i in range(len(search)):
		#print(movies)
		media.append(search[i])
		global s
		s+=(f'{[i+1]} {media[i]} \n')		
def main():
	isearch(input('movie: '))
	#for i in range(len(media)):
	#	print(f'{i+1} {media[i]}')
	#print('------')
	#print(f'tt{media[0].movieID}')  # how to get TT
	#print(media[1])
	#print('#####')


	# print('\n'.join([str(elem) for elem in media]) + '[1]')
	print(s)

if __name__=="__main__":
	main()
