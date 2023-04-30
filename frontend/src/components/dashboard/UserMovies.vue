<template>
    <h1 class="text-3xl font-bold ">Here are the movies you watched</h1>

    <section class="grid grid-cols-6 gap-5 py-10">
        <MovieCard class="h-[200px] col-span-1" v-for="movie in movies" :key="movie.id" :movie="movie" @click="showDialog(movie)" short  />
    </section>

    <MovieDialog v-if="showMovieDialog.show" :movie="showMovieDialog.movie" @close="showMovieDialog.show = false" :fromtmbd="false" /> 
</template>

<script setup lang="ts">
import { Movie, User } from '../../models/types';
import MovieCard from '../MovieCard.vue';
import MovieDialog from '../MovieDialog.vue';
import { ref, onMounted } from 'vue';
import {useUserStore} from '../../stores/userStore';
import {useAuthStore} from '../../stores/authStore';

const userStore = useUserStore();
const authStore = useAuthStore();
const movies = ref<Movie[]>([]);

const showMovieDialog = ref({
    show: false,
    movie: {} as Movie,
});

const showDialog = (movie: Movie) => {
    showMovieDialog.value.movie = movie;
    showMovieDialog.value.show = true;
};

onMounted(async () => {
    if (localStorage.getItem('movies')) {
        const moviesFromLocalStorage = localStorage.getItem('movies');
        const moviesFromLocalStorageParsed = JSON.parse(moviesFromLocalStorage!);
        movies.value = moviesFromLocalStorageParsed;
    } else {
        let currentUser = authStore.user as User;
        await userStore.getUserMovies(currentUser);
        movies.value = userStore.movies;
    }
});
</script>