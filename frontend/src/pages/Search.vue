<template>
    <section class="container py-20">
        <h1 class="text-3xl font-bold pb-10">Results for : {{ currentSearch }}</h1>
        <div v-if="searchResults.length > 0" class="flex flex-col gap-10">
            <div @click="showDialog(movie)" v-for="movie in searchResults" :key="movie.id" class="flex gap-10 p-4 hover:bg-gray-800 transition-all duration-300 border-gray-900 hover:border-gray-700 rounded-lg cursor-pointer">
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
    </section>

    <MovieDialog v-if="showMovieDialog.show" :movie="showMovieDialog.movie" @close="showMovieDialog.show = false" :fromtmbd="false" /> 
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import MovieService from './../services/MovieService';
import MovieDialog from '../components/MovieDialog.vue';
import { Movie } from '../models/types';

const movieService = new MovieService();

const router = useRouter();
const currentSearch = ref('');
const searchResults = ref<Movie[]>([]);
const showMovieDialog = ref({
    show: false,
    movie: {} as Movie
});

const searchMovies = async (movieName: string) => {
    currentSearch.value = decodeURI(movieName);
    searchResults.value = await movieService.searchMovieByName(currentSearch.value, 30)
}

const showDialog = (movie: Movie) => {
    showMovieDialog.value = {
        show: true,
        movie: movie
    }
}

onMounted(async () => {
    let movie = router.currentRoute.value.params.movie as string;
    await searchMovies(movie);
});

watch(async () => router.currentRoute.value.params.movie, async (movie) => {
    let movieParam = router.currentRoute.value.params.movie as string;
    currentSearch.value = decodeURI(movieParam);
    await searchMovies(movieParam);
});
</script>