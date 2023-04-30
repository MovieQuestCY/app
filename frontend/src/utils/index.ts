import { genres } from "./genres";

export const getGenresFromIds = async (genreIds: number[]): Promise<string> => {
    let genreNames: string[] = [];
    for await (const genreId of genreIds) {
        let genre = genres.find(genre => genre.id === genreId);
        if(genre) {
            genreNames.push(genre.name);
        }
    }
    return genreNames.join(",");
}

export const getGenreFromObjects = (genres: {id: number, name: string}[]): string => {
    let genreNames: string[] = [];
    genres.forEach(genre => {
        genreNames.push(genre.name);
    });
    return genreNames.join(",");
}

export const genresToArray = (genres: string): string[] => {
    return genres.split(",");
}

// Write a function that takes two lists of film genres ranked according to the users' tastes and returns a list (or hasmap) of an optimised list of film genres liked by both users.
export const getOptimisedGenres = (user1Genres: string, user2Genres: string): string[] => {
    let user1GenresArray = genresToArray(user1Genres);
    let user2GenresArray = genresToArray(user2Genres);
    let optimisedGenres: string[] = [];
    let results = new Map<string,number>();
    for (let i = 0; i < user1GenresArray.length; i++) {
        results.set(user1GenresArray[i], i);
    }
    for (let i = 0; i < user2GenresArray.length; i++) {
        let currentGenre = user2GenresArray[i];
        results.set(currentGenre, results.get(currentGenre)! + i);
    }

    let sortedResults = new Map([...results.entries()].sort((a, b) => a[1] - b[1]));
    sortedResults.forEach((value, key) => {
        optimisedGenres.push(key);
    });
    return optimisedGenres;
}