import { Movie, User } from "../models/types";
import {tmdbToken} from "./../secrets"
import { getGenresFromIds, getGenreFromObjects } from "../utils";

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

    async findOrCreate(id: number): Promise<Movie | undefined> {
        const dbResponse = await fetch(`${this.movieApiUrl}${id}`);
        const dbMovie = await dbResponse.json();
        if(dbMovie.id) {
            return dbMovie;
        }

        const tmdbMovie = await this.fetchFromTmdb("movie/" + id);
        const movie = {
            ...tmdbMovie,
            genres: getGenreFromObjects(tmdbMovie.genres)
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
        const response = await this.fetchFromTmdb(`movie/popular`, {
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

    async getWatchedByUser(userId: number): Promise<Movie[]> {
        const response = await fetch(`${this.movieApiUrl}${userId}/watched`);
        const movies = await response.json() as Movie[];
        return movies;
    }

    async isWatchedByUser(userId: number, movieId: number): Promise<boolean> {
        const response = await fetch(`${this.movieApiUrl}${movieId}/watchedby`);
        const users = await response.json() as User[];
        const user = users.some(user => user.id === userId);
        return user;
    }

    async userWatchedMovie(userId: number, movieId: number): Promise<void> {
        await this.findOrCreate(movieId);
        await fetch(`${this.movieApiUrl}${userId}/watched/${movieId}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({userId, movieId})
        });
    }

    async userUnwatchedMovie(userId: number, movieId: number): Promise<void> {
        await fetch(`${this.movieApiUrl}${userId}/unwatched/${movieId}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({userId, movieId})
        });
    }

    async createMovie(movie: Movie): Promise<Movie> {
        const isImageExisting = await fetch(movie.poster_path);
        if(!isImageExisting.ok) {
            movie.poster_path = "";
        }
        const response = await fetch(this.movieApiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(movie)
        });
        const newMovie = await response.json() as Movie;
        return newMovie;
    }

    async getFindings(): Promise<Movie[]> {
        let movies: Array<Movie[]> = [];
        for(let i = 1; i <= 5; i++) {
            const response = await this.fetchFromTmdb(`movie/popular?page=${i}`, {
                method: "GET",
            });
            let res = await response.results;
            res.forEach(async (movie: any) => {
                movie.genres = await getGenresFromIds(movie.genre_ids);
            });
            movies.push(res as Movie[]);
        }
        return movies.flat();
    }
}

export default MovieService;

