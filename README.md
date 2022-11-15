# MovieRecommendation
A Simple Movie Recommendation Generator using Pandas, Numpy, sklearn with a simple GUI using Tkinter. 
# How it works
We use a .csv dataset containing the top 5000 IMDB movies, and use Pandas and Numpy to manipulate the subset of the dataset 
containing the actor, producer, title and genre. Then we use sklearn to devlop a cosine-similarity model that
takes a soup of information containing keywords describing the actor, producer, title and genre, and on which we produce
the top 10 similar titles to the given movie.
# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pandas, Numpy, sklearn.

```bash
pip install pandas
pip install numpy
pip install sklearn
```

