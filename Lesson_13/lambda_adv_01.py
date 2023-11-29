# Lesson 13 Classwork; Task 7
# Створіть програму для обробки даних про рейтинг фільмів. Кожен фільм має назву та рейтинг.
# Напишіть функцію, яка приймає список фільмів та функцію для визначення середнього рейтингу.
# Використайте цю функцію в лямбді, яка має повертати список фільмів з рейтингом вище середнього.

movie_lib = {
    "Avatar": 9.0,
    "Terminator 9": 4.6,
    "Charlie's Angels": 5.7,
    "Hangover": 6.2,
    "The Shining": 7.5,
    "Fast & Furious 10": 3.4,
    "Warheads": 1.2
}

def movie_list(x, func):
    movies = ", ".join([x for x in x.keys()])
    ave_rating = func(x)
    high_rating_movies_list = []
    for key, value in x.items():
        if value >= ave_rating:
            high_rating_movies_list.append(key)
    high_rating_movies = ", ".join([el for el in high_rating_movies_list])
    print("Your current movie library contains next movies:", movies,"\n")
    print("Average movie rating is", round(ave_rating,1), "\n")
    print(f'Here is a list of movies with rating higher than average: {high_rating_movies}.', "\n")

def rating_calc(x):
    y = sum(x.values()) / len(x)
    return y

lambda_func = lambda x, func: movie_list(x, func)
lambda_func(x = movie_lib, func = rating_calc)
