<template>
    <section class="container">
        <div class="pt-20 w-2/3 mx-auto text-center">
            <h2 class="text-2xl text-red-500 uppercase tracking-[1.5rem]">MovieQuest</h2>
            <h1 class="text-6xl font-extrabold">Find the perfect movie to watch together</h1>
        </div>

        
    </section>

    <section class="container pt-20">
        <div class="w-2/3 mx-auto grid grid-cols-3 gap-10" >
            <MovieCard class="moviecard w-full col-span-1" v-for="movie in popularMovies" :key="movie.id" :movie="movie" @click="showDialog(movie)" />
        </div>
    </section>

    <MovieDialog v-if="showMovieDialog.show" :movie="showMovieDialog.movie" @close="showMovieDialog.show = false" fromtmbd /> 
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { Movie } from '../models/types';
import MovieService from './../services/MovieService'
import MovieCard from '../components/MovieCard.vue';
import MovieDialog from '../components/MovieDialog.vue';

const movieService = new MovieService();

const popularMovies = ref<Movie[]>([]);
const showMovieDialog = ref({
    show: false,
    movie: {} as Movie,
});

const showDialog = (movie: Movie) => {
    showMovieDialog.value.movie = movie;
    showMovieDialog.value.show = true;
};

onMounted(() => {
    movieService.getPopularMovies(3).then((movies) => {
        popularMovies.value = movies;
    });
});
</script>

<style scoped>
.moviecard:first-child {
    transform: skewY(-12deg);
    margin-top: 40px;
}
.moviecard:last-child {
    transform: skewY(12deg);
    margin-top: 40px;
}
</style>
