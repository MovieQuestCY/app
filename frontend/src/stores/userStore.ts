import {defineStore} from 'pinia';
import { Movie, Team } from '../models/types';
import UserService from '../services/UserService';

const userService = new UserService();

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
    }
});
