<template>
    <h1 class="text-3xl font-bold ">Find a movie</h1>

    <section class="w-full bg-gray-800 rounded-xl p-5 my-5">
        <h1 class="text-center font-bold text-3xl">Choose your partner</h1>

        <form class="flex gap-5 items-center w-fit mx-auto my-5">
            <p>From my team</p>

            <div class="flex flex-col">
                <select name="team" id="team" @change="handleTeamChange" class="bg-gray-700 rounded-lg px-5 py-2 text-white">
                    <option v-for="team in teams" >{{ team.name }}</option>
                </select>
            </div>

            <p> I'll choose </p>

            <div class="flex flex-col">
                <select name="user" id="user" @change="handleMemberChange" class="bg-gray-700 rounded-lg px-5 py-2 text-white">
                    <option v-for="member in currentTeam?.members" :value="member.id">{{ member.username }}</option>
                </select>
            </div>

            <button @click.prevent.stop="handleSubmit" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-all duration-300">Find</button>

        </form>
    </section>

    <h1 class="text-3xl font-bold pb-5">Your results</h1>
    <div v-if="findings.length > 0" class="flex flex-col gap-10">
            <div @click="showDialog(movie)" v-for="movie in findings" :key="movie.id" class="flex gap-10 p-4 hover:bg-gray-800 transition-all duration-300 border-gray-900 hover:border-gray-700 rounded-lg cursor-pointer">
                <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="h-[150px] aspect-[9/16]" />
                <div class="flex flex-col gap-5">
                    <h2 class="text-2xl font-bold">{{ movie.title }}</h2>
                    <p class="text-gray-500 line-clamp-3">{{ movie.overview }}</p>
                </div>
            </div>            
        </div>
        <div v-else class="text-center">
            <h2 class="text-2xl font-bold">No results found</h2>
            <p class="text-gray-500">Try searching for something else</p>
        </div>

        <MovieDialog v-if="showMovieDialog.show" :movie="showMovieDialog.movie" @close="showMovieDialog.show = false" :fromtmbd="false" /> 


</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import {useUserStore} from '../../stores/userStore';
import {useAuthStore} from '../../stores/authStore';
import TeamService from '../../services/TeamService';
import { Movie, Team, User } from '../../models/types';
import {getOptimisedGenres} from '../../utils';
import MovieService from '../../services/MovieService';
import MovieDialog from '../MovieDialog.vue';

const userStore = useUserStore();
const authStore = useAuthStore();
const teamService = new TeamService();
const movieService = new MovieService();
const currentUser = authStore.user;

const teams = ref<Team[]>([]);
const currentTeam = ref<Team>();
const selectedOption = ref<User>();
const findings = ref<Movie[]>([]);
const showMovieDialog = ref({
    show: false,
    movie: {} as Movie
})

const handleTeamChange = (e: any) => {
    currentTeam.value = teams.value.find((team: Team) => team.name === e.target.value);
}

const handleMemberChange = (e: any) => {
    selectedOption.value = currentTeam.value?.members.find((member: User) => member.id === Number(e.target.value));
}

const showDialog = (movie: Movie) => {
    showMovieDialog.value.show = true;
    showMovieDialog.value.movie = movie;
}

onMounted(async () => {
    await userStore.getUserTeams(currentUser);
    let allTeams = JSON.parse(localStorage.getItem('teams') || '[]');
    for await (const team of allTeams) {
        let members = await teamService.getTeamMembers(team.id) as User[];
        members = members.filter((member: User) => member.id !== currentUser.id);
        let newTeam = {
            ...team,
            members
        } as Team;
        if(members.length > 0) teams.value.push(newTeam)
    }
    currentTeam.value = teams.value[0];
    selectedOption.value = currentTeam.value?.members[0];
})

const handleSubmit = async () => {
    let res = new Map<Movie, number>();
    let user1 = currentUser;
    let user2 = selectedOption.value;
    let genres = getOptimisedGenres(user1.favorite_genres!, user2?.favorite_genres!);
    const movies = await movieService.getFindings();
    movies.forEach((movie: Movie) => {
        let score = 0;
        genres.forEach((genre: string) => {
            if(movie.genres?.includes(genre)) score += (19 - genres.indexOf(genre));
        })
        res.set(movie, score);
    })
    let sorted = new Map([...res.entries()].sort((a, b) => b[1] - a[1]));
    let toArray = Array.from(sorted.keys()).slice(0, 10);
    findings.value = toArray;
}
</script>