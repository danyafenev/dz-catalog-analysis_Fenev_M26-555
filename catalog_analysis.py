import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1. Разминка: переменные, числа, math.

def average_rating(movies: list[dict]) -> float:
    """Сделал генераторное выражение, чтобы не захламлять память.
    А float я взял, чтобы обьзапасить себя от того, что он строчный
    """
    
    return round(sum(float(movie["rating"]) for movie in movies) / len(movies), 1)

def catalog_age_stats(movies: list[dict], 
                      curr_year: int = 2026) -> tuple[int, int, int]:
    
    """Функция catalog_age_stats возвращает кортеж 
    (самый старый фильм в годах, самый новый фильм в годах, среднее), 
    где среднее округлено вверх до целого с помощью math.ceil.
    
    Я хотел выдать ответ, через генераторное выражение, но оно очень длинное
    и не удобное для чтения, поэтому сделал создание списка через list comprehension
    """
    a = [curr_year - int(movie["year"]) for movie in movies]
    avg_age = math.ceil(sum(a) / len(movies))
    
    return (max(a), min(a), avg_age)
    
def duration_in_hours(minutes: int) -> str:
     
    """Функция duration_in_hours(minutes) переводит минуты в формат "2ч 35м", 
    используя целочисленное деление и остаток от деления.
    """
     
    duration_hr = f"{minutes // 60}ч {minutes % 60}м"

    return duration_hr   

# Этап 2. Условия и match.

def rating_tier(rating: float) -> str:
    
    if rating >= 9:
        ans = 'шедевр'
    
    elif rating < 9 and rating >= 7:
        ans = "хорошо"
    
    elif rating < 7:
        ans = "средне" if rating >= 5 else "слабо"
    
    return ans

def decade_label(year: int) -> str:
    
    match year:

        case _ if year > 2020:
            
            label = "новые"

        case _ if year >= 2015:
            
            label = "недавние"

        case _ if year < 2015:
            
            label = "старые"
    
    return label

# Этап 3. Циклы

def task_from_stage_3(movies: list[dict]) -> None:
    """
    Эта функция для демонстрации работы циклов и
    вывода и выводов результата отдельно от отчета.
    """
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        else:
            print(movie["title"])

    i = 0

    while i <= len(movies) - 1:
        
        if movies[i]["rating"] > 9.0:
            print(movies[i]["title"])
            break
        
        i += 1
        
    else:
        print("Шедевров не найдено")

def count_long_movies(movies: list[dict], threshold = 120) -> int:
    
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    
    return count

# 4 Этап. Строки

def normalize_title(title: str) -> str:
    
    return " ".join(word[0].upper() + word[1:] for word in title.split())

def make_slug(title: str) -> str:
    
    return title.lower().replace(" ", "-")

def format_report_line(movie: dict) -> str:
    
    return (
        f'"{normalize_title(movie["title"])}"'
        f' ({movie["year"]}) — {movie["rating"]}/10, '
        f'{duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}'
    )

# Этап 5. Списки

def titles_sorted_by_rating(movies: list[dict]) -> list:
    
    movies_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    
    return [movie["title"] for movie in movies_sorted]

def top_n_by_rating(movies: list[dict], n=3) -> list[tuple]:
    
    movies_and_rating = [(movie["title"], movie["rating"]) for movie in movies]
    
    return sorted(movies_and_rating, key=lambda movie: movie[1], reverse=True)[:n]

# Этап 6. Словари

def count_by_genre(movies: list[dict]) -> dict:
    
    counts = {}
    
    for movie in movies:
        for genre in movie["genres"]:
            
            counts[genre] = counts.get(genre, 0) + 1
    
    return counts

def actor_filmography(movies: list[dict]) -> dict:
    
    filmography = {}
    
    for movie in movies:
        for actor in movie["actors"]:
            
            if actor not in filmography:
                filmography[actor] = []
            
            filmography[actor].append(movie["title"])
    
    return filmography

# Словарь со с рейтингом фильмов выше чем среднее.

avg_rating = average_rating(movies)

dict_rating = {movie["title"]: movie["rating"] for movie in movies
               if movie["rating"] > avg_rating}

# Этап 7. Множества

def all_genres(movies: list[dict]) -> set:
    
    genres = set()
    
    for movie in movies:
        
        genres = genres | movie["genres"]
    
    return genres

def common_actors(movie1: dict, movie2: dict) -> set:
    
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    
    return all_genres(movies_a) - all_genres(movies_b)

# Этап 8. Итераторы и генераторы. 

def iter_high_rated(movies: list[dict], min_rating=8.0):
    
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def demonstrate_generator(movies: list[dict]) -> None:
    """
    Эта фукнция для того, чтобы не печатались фильмы в отчет 
    и показать вывод для сумарного кол-ва минут
    """
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    
    total_duration = sum(movie["duration_min"] 
                    for movie in movies if movie["rating"] > 7)
    
    print(total_duration)

# Этап 9. Формирование итогово отчета.

def build_report(movies: list[dict]) -> None:
    
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    
    print("\nТоп-3 фильма:")

    top_titles = titles_sorted_by_rating(movies)[:3]

    for title in top_titles:
        for movie in movies:
            if movie["title"] == title:
                print(f"  {format_report_line(movie)}")
                break
        
    print("\nФильмов по жанрам:")
    
    for genre, count in sorted(
        count_by_genre(movies).items(),
        key=lambda item: item[1],
        reverse=True):
        
        print(f"  {genre} — {count}")
    
    print(f"\nВсе жанры каталога: {", ".join(sorted(all_genres(movies)))}\n")

if __name__ == "__main__":
    build_report(movies)