#!/usr/bin/env python
# coding: utf-8

# In[62]:


import json
from shutil import move
from matplotlib.pyplot import title
import pandas as pd
path = "C:/Users/Wafik/PycharmProjects/MovieRecommendation/data"
credits_df = pd.read_csv(path + "/tmdb_5000_credits.csv")
movies_df = pd.read_csv(path + "/tmdb_5000_movies.csv")


# In[63]:


#movies_df


# In[64]:


credits_df.columns = ['id','title','cast','crew']
titles = credits_df['title']
titles = [title for title in titles]




# In[65]:


#credits_df


# In[66]:

# In[67]:


import numpy as np
def crew_to_director(crew):
    crew = json.loads(crew)
    for person in crew:
        if person['job'] == 'Director':
            return person['name']
    return np.nan        


# In[68]:


credits_df['director'] = credits_df['crew'].apply(crew_to_director)


# In[70]:


movies_df = movies_df.merge(credits_df,on='id')


# In[79]:


def get_list(x):
    x = json.loads(x)
    if isinstance(x, list):
        names = [i["name"] for i in x]
        if len(names) > 3:
            names = names[:3]
        return names
    return []


# In[80]:


features = ["cast", "keywords", "genres"]
for feature in features:
    movies_df[feature] = movies_df[feature].apply(get_list)


# In[107]:


df = credits_df[['title','id']]


# In[108]:


movies_df = movies_df.merge(df,on='id')


# In[109]:


movies_df


# In[110]:


movies_df[['title', 'cast', 'director', 'keywords', 'genres']].head()


# In[111]:


def clean_data(row):
    if isinstance(row, list):
        return [str.lower(i.replace(" ", "")) for i in row]
    else:
        if isinstance(row, str):
            return str.lower(row.replace(" ", ""))
        else:
            return ""

features = ['cast', 'keywords', 'director', 'genres']
for feature in features:
    movies_df[feature] = movies_df[feature].apply(clean_data)


# In[113]:


def create_soup(features):
    return ' '.join(features['keywords']) + ' ' + ' '.join(features['cast']) + ' ' + features['director'] + ' ' + ' '.join(features['genres'])


movies_df["soup"] = movies_df.apply(create_soup, axis=1)
#print(movies_df["soup"].head())


# In[114]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(movies_df["soup"])
#print(count_matrix.shape)
cosine_sim2 = cosine_similarity(count_matrix, count_matrix) 
#print(cosine_sim2.shape)
movies_df = movies_df.reset_index()
indices = pd.Series(movies_df.index, index=movies_df['title'])


# In[118]:


indices = pd.Series(movies_df.index, index=movies_df["title"]).drop_duplicates()
#indices.head(10)


# In[122]:


def get_recommendations(title, cosine_sim=cosine_sim2):
    idx = indices[title]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores= similarity_scores[1:11]
    # (a, b) where a is id of movie, b is similarity_scores
    movies_indices = [ind[0] for ind in similarity_scores]
    movies = movies_df["title"].iloc[movies_indices]
    titles = [movie for movie in movies]
    return titles


# In[123]:


#print("################ Content Based System #############")
#print("Recommendations for The Dark Knight Rises")
#print(get_recommendations("The Dark Knight Rises", cosine_sim2))
#print()
#print("Recommendations for Avengers")
#print(get_recommendations("The Avengers", cosine_sim2))


# In[124]:


#cosine_sim2.dtype


# In[ ]:




