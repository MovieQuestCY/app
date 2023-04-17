<template>
    <section class="container py-20">
        <h1 class="text-3xl font-bold pb-10">Results for : {{ currentSearch }}</h1>
        <div v-if="searchResults.length > 0" class="flex flex-col gap-10">
            <div v-for="movie in searchResults" :key="movie.id" class="flex gap-10">
                <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="w-[150px] h-[250px] object-cover" />
                <div class="flex flex-col gap-5">
                    <h2 class="text-2xl font-bold">{{ movie.title }}</h2>
                    <p class="text-gray-500">{{ movie.overview }}</p>
                    <div class="flex gap-5">
                        <button class="flex gap-2 px-4 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300">Watch</button>
                        <button class="flex gap-2 px-4 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300">Add to watchlist</button>
                    </div>
                </div>
            </div>            
        </div>
        <div v-else class="text-center">
            <h2 class="text-2xl font-bold">No results found</h2>
            <p class="text-gray-500">Try searching for something else</p>
        </div>
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import MovieService from './../services/MovieService';
import { Movie } from '../models/types';

const movieService = new MovieService();

const router = useRouter();
const currentSearch = ref('');
const searchResults = ref<Movie[]>([]);

const searchMovies = async (movieName: string) => {
    currentSearch.value = decodeURI(movieName);
    searchResults.value = await movieService.searchMovieByName(currentSearch.value, 5)
}

onMounted(async () => {
    let movie = router.currentRoute.value.params.movie as string;
    
    await searchMovies(movie);
});

//watch route change
watch(async () => router.currentRoute.value.params.movie, async (movie) => {
    let movieParam = router.currentRoute.value.params.movie as string;
    currentSearch.value = decodeURI(movieParam);
    await searchMovies(movieParam);
});
</script>