import { genres } from "./genres";

export const getGenresFromIds = (genreIds: number[]): string => {
    const genreNames = genreIds.map(id => {
        const genre = genres.find(genre => genre.id === id);
        return genre ? genre.name : "";
    });
    return genreNames.join(",");
}

export const genresToArray = (genres: string): string[] => {
    return genres.split(",");
}
