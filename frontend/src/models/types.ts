export interface Movie {
    id: number;
    title: string;
    description: string;
    year: number;
    rating: number;
    genre: string[];
    image: string;
}

export interface User {
    id: number;
    username: string;
    password: string;
    email: string;
    movie_viewed: Movie[];
}