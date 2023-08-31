import re

def calculate_similarity(query, database):
    # Convert both query and database text to lowercase for case-insensitive comparison
    query = query.lower()
    database = database.lower()

    # Tokenize the text into words using regular expressions
    query_words = re.findall(r'\b\w+\b', query)
    database_words = re.findall(r'\b\w+\b', database)

    # Create a set of unique words from both query and database
    universal_set = set(query_words) | set(database_words)

    # Calculate term frequency (TF) for query and database
    query_tf = [query_words.count(word) for word in universal_set]
    database_tf = [database_words.count(word) for word in universal_set]

    # Calculate dot product and magnitude for both vectors
    dot_product = sum(query_tf[i] * database_tf[i] for i in range(len(universal_set)))
    query_magnitude = sum(tf ** 2 for tf in query_tf) ** 0.5
    database_magnitude = sum(tf ** 2 for tf in database_tf) ** 0.5

    # Calculate cosine similarity
    similarity = dot_product / (query_magnitude * database_magnitude)

    # Convert similarity to percentage
    match_percentage = similarity * 100

    return match_percentage

if __name__ == "__main__":
    print("Plagiarism Checker")
    print("Enter the query text:")
    query_text = input()
    print("Enter the database text:")
    database_text = input()

    similarity_percentage = calculate_similarity(query_text, database_text)

    print(f"Query text matches {similarity_percentage:.2f}% with the database.")
