import imdb

media=[]

def isearch(a):
    iq = imdb.IMDb()
    search = iq.search_movie(a)
    for movies in search:
        print(movies)
        media.append(movies)



def main():
	isearch(input('movie: '))
	print(f'tt{media[0].movieID}')  # how to get TT
	print(media[1])


if __name__=="__main__":
	main()
