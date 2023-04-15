<template>
    <section class="container">
        <div class="pt-20 w-2/3 mx-auto text-center">
            <h2 class="text-2xl text-red-500 uppercase tracking-[1.5rem]">MovieQuest</h2>
            <h1 class="text-6xl font-extrabold">Find the perfect movie to watch together</h1>
        </div>

        <form class="flex w-2/3 mx-auto mt-10 gap-4">
            <input type="text" class="w-full p-2 border-2 border-gray-600 bg-gray-700 rounded-lg focus-visible:outline-none" placeholder="Search for a movie" />
            <button class="flex gap-2 px-4 py-2 bg-red-500 text-white rounded-lg text-lg hover:bg-red-600 transition-all duration-300"><i class="bi bi-magic"></i> Find</button>
        </form>
    </section>

    <section class="container pt-20">
        <div class="flex justify-around w-2/3 mx-auto" >
            <MovieCard v-for="movie in popularMovies" :key="movie.id" :movie="movie" />
        </div>
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { Movie, User } from '../models/types';
import UserService from './../services/UserService'
import MovieService from './../services/MovieService'
import MovieCard from '../components/MovieCard.vue';

const userService = new UserService();
const movieService = new MovieService();

const popularMovies = ref<Movie[]>([]);

onMounted(() => {
    movieService.getPopularMovies(3).then((movies) => {
        popularMovies.value = movies;
    });
});
</script>
