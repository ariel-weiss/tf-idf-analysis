
n_words = 200
possible_frequencies = {
'low_frequency' : {
            'word_count': int(0.005*n_words),
            'n_words': n_words,
         },
'mid_frequency' : {
            'word_count': int(0.03*n_words),
            'n_words': n_words,
         },
'high_frequency' : {
            'word_count': int(0.06*n_words),
            'n_words': n_words,
         }
}

n_documents = 1000000
possible_rarities = {
'common_word' : {
            'n_documents': n_documents,
            'relevant_documents': int(n_documents*0.7)
            },
'mid_rarity' : {
            'n_documents': n_documents,
            'relevant_documents': int(n_documents*0.3)
            },
'rare_word' : {
            'n_documents': n_documents,
            'relevant_documents': int(n_documents*0.1)
            },
}

