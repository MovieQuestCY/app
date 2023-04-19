// We're using camel_case for types to directly match the JSON response from the python backend or tmdb api.

export interface Movie {
    id: number;
    title: string;
    overview: string;
    release_date: string;
    vote_average: number;
    genres: string;
    popularity: number;
    poster_path: string;
}

export interface User {
    id: number;
    firstname: string;
    lastname: string;
    username?: string;
    email: string;
    profile_picture?: string;
    favorite_genres?: string;
}

export interface UserCreation {
    firstname: string;
    lastname: string;
    username?: string;
    email: string;
    profile_picture?: string;
    favorite_genres?: string;
    password: string;
}

export interface TeamResponse {
    id: number;
    name: string;
}

export interface Team extends TeamResponse {
    members: User[];
}