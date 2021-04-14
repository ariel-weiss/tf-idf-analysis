# %%
import matplotlib.pyplot as plt
from data import possible_frequencies,possible_rarities
from test_tfidf import TestTFIDF
# %%
testTFIDF = TestTFIDF(possible_frequencies,possible_rarities)
# %% [markdown]
# The frequencies and rarities here are taken from the data.py module.
# <br> To use the TestTFIDF object I sent requests to my TF-IDF node service running locally. 
# %%
plt.rcParams['figure.figsize'] = [12, 5]
testTFIDF.start_test({ "tf_option": 1, "idf_option": 1 })
testTFIDF.start_test({ "tf_option": 2, "idf_option": 1 })
testTFIDF.start_test({ "tf_option": 2, "idf_option": 2 })
# %% [markdown]
# ---
# # TF-IDF Weighting Schemes
# ## **TF options ** 
# 1. **Normal:** ![Normal](https://wikimedia.org/api/rest_v1/media/math/render/svg/91699003abf4fe8bdf861bbce08e73e71acf5fd4) 
# 2. **Log normalization:** ![Log](https://wikimedia.org/api/rest_v1/media/math/render/svg/9c173382612c58c00325c4e9f593739ab3afc324)
# %% [markdown]
# ## **IDF options**
# 1. **Normal:** ![Normal](https://wikimedia.org/api/rest_v1/media/math/render/svg/864fcfdc0c16344c11509f724f1aa7081cf9f657)
# 2. **Probabilistic:** ![Probabilistic](https://wikimedia.org/api/rest_v1/media/math/render/svg/1868194cba8431aa2d556dd1aac90d78833eaaf3)
# %% [markdown]
# ### **Note on word's rarity:**
# I used the term 'rarity' here to describe the document frequency.
# <br>If more then half of the documents contains the given word, I called it a common word.
# <br>If only tenth of the documents contains it, it's a rare word.
#
# %% [markdown]
# In the following graphs, the Y axis describe the TF-IDF score, and the X axis is the weighting schemes combinations (3 lines for 3 combinations).
# %%
testTFIDF.draw_graphs()

# %% [markdown]
# I chose the following tf-idf weighting schemes combinations: (The options are explained above)
# - tf_option: 1, idf_option: 1  (1:1)
# - tf_option: 2, idf_option: 1  (2:1)
# - tf_option: 2, idf_option: 2  (2:2)
# %% [markdown]
# # Conclusions
# 
# We can deduce from the graphs that the third combination gives the common words
# a negative score (a possible usecase is to easily filter out common words, like 'the').
# <br>Also, the log version of the TF is squeezing the tf-idf score to a smaller range,
# as we expect from the log function. This is especially reflected in the high_frequency graph, where the tf
# score is relatively high.
# <br>There is no clear difference between the second and third combination, other then what I've
# mentioned about the negative score.
# 
# %%
