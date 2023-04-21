import { Movie } from "../models/types";
import {tmdbToken} from "./../secrets"
import { getGenresFromIds } from "../utils";

class MovieService {
    private movieApiUrl = import.meta.env.VITE_APP_MOVIES_API_URL;
    private tmdbApiUrl = "https://api.themoviedb.org/3";
    private static instance: MovieService;

    static getInstance() {
        if (!MovieService.instance) {
            MovieService.instance = new MovieService();
        }
        return MovieService.instance;
    }

    async fetchFromTmdb(endpoint: string, options: any = {}): Promise<any> {
        const url = `${this.tmdbApiUrl}/${endpoint}`;
        const headers = new Headers({
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": `Bearer ${tmdbToken}`
        });
        return fetch(url, { ...options, headers }).then(response => response.json());
    }

    async getMovie(id: number): Promise<Movie | undefined> {
        const dbResponse = await fetch(`${this.movieApiUrl}/${id}`);
        const dbMovie = await dbResponse.json();
        if(dbMovie.id) {
            return dbMovie;
        }

        const tmdbMovie = await this.fetchFromTmdb("movie/" + id);
        const movie = {
            ...tmdbMovie,
            genres: getGenresFromIds(tmdbMovie.genres)
        } as Movie;

        try {
            await fetch(this.movieApiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(movie)
            });
            return movie;
        } catch (error) {
            console.log(error);
        }
    }

    async getAllMovies(): Promise<Movie[]> {
        const response = await fetch(this.movieApiUrl);
        const movies = await response.json() as Movie[];
        return movies;
    }

    async getPopularMovies(number: number): Promise<Movie[]> {
        const response = await this.fetchFromTmdb("movie/popular", {
            method: "GET",
        });
        const movies = await response.results as Movie[];
        return movies.slice(0, number);
    }

    async searchMovieByName(name: string, number: number): Promise<Movie[]> {
        const response = await this.fetchFromTmdb("search/movie?query=" + name, {
            method: "GET",
        });
        const movies = await response.results as Movie[];
        return movies.slice(0, number);
    }
}

export default MovieService;

