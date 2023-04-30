import {defineStore} from 'pinia';
import { Movie, Team, TeamResponse, User } from '../models/types';
import UserService from '../services/UserService';
import MovieService from '../services/MovieService';
import TeamService from '../services/TeamService';

const userService = new UserService();
const movieService = new MovieService();
const teamService = new TeamService();

export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        movies: [] as Movie[],
        teams: [] as Team[],
    }),
    getters: {
        getMovies: (state) => state.movies,
        getTeams: (state) => state.teams,
    },
    actions: {
        async getUserMovies(user: User) {
            this.movies = await movieService.getWatchedByUser(user.id);
            localStorage.setItem('movies', JSON.stringify(this.movies));
        },
        async getUserTeams(user: User) {
            this.teams = await teamService.getUserTeams(user.id);
            localStorage.setItem('teams', JSON.stringify(this.teams));
        },
        async watchMovie(user: User, movie: Movie) {
            await movieService.userWatchedMovie(user.id, movie.id);
            await this.getUserMovies(user);
        },
        async unwatchMovie(user: User, movie: Movie) {
            await movieService.userUnwatchedMovie(user.id, movie.id);
            await this.getUserMovies(user);
        },
        async joinTeam(user: User, team: TeamResponse) {
            await teamService.addUserToTeam(team.id, user.id);
            await this.getUserTeams(user);
        },
        async leaveTeam(user: User, team: TeamResponse) {
            await teamService.removeUserFromTeam(team.id, user.id);
            await this.getUserTeams(user);
        },
        async createTeam(user: User, name: string) {
            const team = await teamService.createTeam(name, user.id);
            await this.getUserTeams(user);
            return team;
        },
        hasWatchedMovie(movie: Movie) {
            const movies = JSON.parse(localStorage.getItem('movies') || '[]');
            return movies.some((m: Movie) => m.id === movie.id);
        }
    }
});
