import { Movie, User } from "../models/types";
import {tmdbToken} from "./../secrets"
import { getGenresFromIds, getGenreFromObjects } from "../utils";

class MovieService {
    private movieApiUrl = import.meta.env.VITE_APP_MOVIES_API_URL;
    private tmdbApiUrl = "https://api.themoviedb.org/3";
    private dbToken = localStorage.getItem("token");
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
        const dbResponse = await fetch(`${this.movieApiUrl}${id}?authToken=${this.dbToken}`);
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
            await fetch(this.movieApiUrl + `?authToken=${this.dbToken}`, {
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
        const response = await fetch(this.movieApiUrl + `?authToken=${this.dbToken}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${this.dbToken}`
            },
        });
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
        const response = await fetch(`${this.movieApiUrl}${userId}/watched?authToken=${this.dbToken}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${this.dbToken}`
            },
            });
        const movies = await response.json() as Movie[];
        return movies;
    }

    async isWatchedByUser(userId: number, movieId: number): Promise<boolean> {
        const response = await fetch(`${this.movieApiUrl}${movieId}/watchedby?authToken=${this.dbToken}`);
        const users = await response.json() as User[];
        const user = users.some(user => user.id === userId);
        return user;
    }

    async userWatchedMovie(userId: number, movieId: number): Promise<void> {
        await this.findOrCreate(movieId);
        await fetch(`${this.movieApiUrl}${userId}/watched/${movieId}?authToken=${this.dbToken}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${this.dbToken}`
            },
            body: JSON.stringify({userId, movieId})
        });
    }

    async userUnwatchedMovie(userId: number, movieId: number): Promise<void> {
        await fetch(`${this.movieApiUrl}${userId}/unwatched/${movieId}?authToken=${this.dbToken}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${this.dbToken}`
            },
            body: JSON.stringify({userId, movieId})
        });
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

