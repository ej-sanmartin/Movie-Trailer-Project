import fresh_tomatoes
import MovieClass

'''instances of Movies being created, including information on title,
summary, movie poster, and their youtube trailer's url'''
toy_story = MovieClass.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_room = MovieClass.Movie(
    "The Room",
    "A love triangle of epic proportions",
    "https://upload.wikimedia.org/wikipedia/en/e/e1/TheRoomMovie.jpg",
    "https://www.youtube.com/watch?v=tfMTHIwTUXA")

train_to_busan = MovieClass.Movie(
    "Train to Busan",
    "Father and daughter trapped on train during a zombie outbreak",
    "https://upload.wikimedia.org/wikipedia/en/9/95/Train_to_Busan.jpg",
    "https://www.youtube.com/watch?v=pyWuHv2-Abk")

lilo_and_stitch = MovieClass.Movie(
    "Lilo & Stitch",
    "The galaxy's most wanted and a hawaiian girl learn the meaning of ohana",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/LiloandStitchmovieposter.jpg",
    "https://www.youtube.com/watch?v=wAtaSKQ4-T0")

dunkirk = MovieClass.Movie(
    "Dunkirk",
    "Allied soldiers try to survive a fierce WWII battle",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
    "https://www.youtube.com/watch?v=F-eMt3SrfFU")

beauty_and_the_beast = MovieClass.Movie(
    "Beauty and the Beast",
    "A tale as old as time",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
    "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

spiderman_homecoming = MovieClass.Movie(
    "Spiderman: Homecoming",
    "Spiderman tries to prove himself while also balancing high school",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
    "https://www.youtube.com/watch?v=oNE0zRNyXuc")

heathers = MovieClass.Movie(
    "Heathers",
    "This teenage angst has a body count",
    "https://upload.wikimedia.org/wikipedia/en/7/77/Heathersposter89.jpg",
    "https://www.youtube.com/watch?v=v5gHF3FNr78")

hellboy = MovieClass.Movie(
    "Hellboy",
    "The son of the devil saves the world",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Hellboy_poster.jpg",
    "https://www.youtube.com/watch?v=VTZB7u3iFaA")

movies = [toy_story, the_room,
          train_to_busan, lilo_and_stitch,
          dunkirk, beauty_and_the_beast,
          spiderman_homecoming, heathers]

#Generates the web page
fresh_tomatoes.open_movies_page(movies)
