class Collection:
    def __init__(self, movielist, gamelist):
        self.movielist = movielist
        self.gamelist = gamelist
        self.favgame = ""
        self.favmovie = ""
    def display_movies(self):
        print("Movies in your collection:")
        for movie in self.movielist:
            print("- " + movie)
        if not self.movielist:
            print("No movies in your list.")
    def display_games(self):
        print("Games in your collection:")
        for game in self.gamelist:
            print("- " + game)
        if not self.gamelist:
            print("No games in your list.")
    def add_movie(self, movie):
        self.movielist.append(movie)
        print(f"Added movie: {movie}")
    def add_game(self, game):
        self.gamelist.append(game)
        print(f"Added game: {game}")
    def remove_movie(self, movie):
        if movie in self.movielist:
            self.movielist.remove(movie)
            print(f"Removed movie: {movie}")
        else:
            print(f"{movie} not found in movie list.")
    def remove_game(self, game):
        if game in self.gamelist:
            self.gamelist.remove(game)
            print(f"Removed game: {game}")
        else:
            print(f"{game} not found in game list.")
    def set_favorite_movie(self, movie):
        if movie in self.movielist:
            self.favmovie = movie
            print(f"Favorite movie set to: {movie}")
        else:
            print(f"{movie} is not in your movie list.")
    def set_favorite_game(self, game):
        if game in self.gamelist:
            self.favgame = game
            print(f"Favorite game set to: {game}")
        else:
            print(f"{game} is not in your game list.")
        





             

    def DisplayFavGame(self):
        print(self.favgame)

    def DisplayFavMovie(self):
        print(f'Fav Movie:{self.favmovie}')