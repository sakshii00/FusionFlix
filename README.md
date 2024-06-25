# Fusionflix

Fusionflix is a movie recommendation system that provides movie recommendations based on the content of movies. It leverages a movie [dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), processes the data to extract meaningful tags, and uses vectorization and the bag-of-words model to generate recommendations. Additionally, Fusionflix integrates with the TMDB API to fetch movie images, and the frontend is built using Streamlit.

## Features

- **Content-Based Recommendations**: Uses movie metadata to provide recommendations based on content similarity.
- **Data Preprocessing**: Preprocesses movie data to extract tags for better recommendation accuracy.
- **Vectorization and Bag-of-Words**: Utilizes vectorization and the bag-of-words technique to compute movie similarities.
- **TMDB API Integration**: Fetches movie images using the TMDB API.
- **Streamlit Frontend**: Interactive user interface built with Streamlit.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/Fusionflix.git
    cd Fusionflix
    ```

2. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory of the project and add your TMDB API key:
    ```env
    API_KEY=your_tmdb_api_key
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Interact with the application**:
    Open your browser and go to `http://localhost:8501` to start using Fusionflix. Enter a movie name to get personalized recommendations and view movie images fetched from the TMDB API.

## Recommendation Engine

The recommendation engine works by:
1. **Calculating Similarities**: Compute cosine similarities between movie vectors.
2. **Generating Recommendations**: Recommend movies based on the highest similarity scores.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
