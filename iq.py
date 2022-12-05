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
def main():
	isearch(input('movie: '))
	print(s)

if __name__=="__main__":
	main()
