# Musical Recommendation System

A Python project for building a music recommendation dataset from song lyrics and audio features. Lyrics are cleaned and converted into a bag-of-words representation, then an `MLPClassifier` predicts song emotions. A second dataset preparation flow groups songs by genre using Spotify-style audio features.

## Project structure

- `Trabajo_Final_Inteligencia_Articial.ipynb` - main notebook for the project analysis and experiments.
- `creatingBagOfWords/` - creates the lyrics corpus, tokens, stems, and bag-of-words CSV.
- `creatingDataSet/` - trains the emotion classifier and writes `dataSet.csv`.
- `creatingDataSet2/` - prepares the genre-based music dataset.
- `API/` - reserved for the project API.

## Requirements

Python 3 with the following packages:

```bash
pip install beautifulsoup4 nltk numpy pandas scikit-learn jupyter
```

The NLTK tokenizer and stop-word data are also required:

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

## Usage

Run commands from the repository root so the scripts can find their relative paths. Provide the source lyrics dataset as `lyrics.csv` in the root directory, then run the preprocessing scripts in this order:

1. `creatingBagOfWords/creatingCorpus.py`
2. `creatingBagOfWords/creatingTokens1.py` through `creatingTokens4.py`
3. `creatingBagOfWords/doingDerivation.py`
4. `creatingBagOfWords/creatingBagOfWords.py`
5. `creatingDataSet/creatingDataSet.py`
6. `creatingDataSet2/creatingDataSet2.py`

The repository includes intermediate CSV and text files, but the original `lyrics.csv` input is not included. Open the notebook with `jupyter notebook` to review the analysis and experiments.
