books = [
    {'title': 'Book 1', 'genre': 'Fantasy', 'author': 'Author 1', 'publication_date': '2024-01-01'},
    {'title': 'Book 2', 'genre': 'Science Fiction', 'author': 'Author 2', 'publication_date': '2018-05-15'},
]

users = [
    {'preferences': {'genre': 'Fantasy', 'author': 'Author 1', 'publication_date': '2024-01-01'}},
    {'preferences': {'genre': 'Science Fiction', 'author': 'Author 2', 'publication_date': '2018-05-15'}},
]

def similarity(feature_vector1, feature_vector2):
    return 0.5  # Placeholder similarity score

current_user = {'preferences': {'genre': 'Fantasy', 'author': 'Author 1', 'publication_date': '2024-01-01'}}

book_features = {'genre': [], 'author': [], 'publication_date': []}
for book in books:
    book_features['genre'].append(book['genre'])
    book_features['author'].append(book['author'])
    book_features['publication_date'].append(book['publication_date'])

user_preferences = {'genre': [], 'author': [], 'publication_date': []}
for user in users:
    user_preferences['genre'].append(user['preferences']['genre'])
    user_preferences['author'].append(user['preferences']['author'])
    user_preferences['publication_date'].append(user['preferences']['publication_date'])

def recommend_books(user):
    recommendations = []
    for book in books:
        score = 0
        score += similarity(book_features['genre'], user_preferences['genre'])
        score += similarity(book_features['author'], user_preferences['author'])
        score += similarity(book_features['publication_date'], user_preferences['publication_date'])
        if score > 0.5:
            recommendations.append((book, score))
    return recommendations

recommendations = recommend_books(current_user)
for book, score in recommendations:
    print(f"Title: {book['title']}, Score: {score}")
