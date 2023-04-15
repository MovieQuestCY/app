<template>
    <article class="rounded-lg overflow-hidden">
        <img 
            class="object-cover w-[250px] h-[400px]"
            :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`" 
            :alt="props.movie.title + ' poster'" />
    </article>
</template>

<script setup lang="ts">
import { Movie } from '../models/types';

const props = defineProps<{
    movie: Movie;
}>();
</script>

<style scoped>
article img {
    aspect-ratio: 9/16;
}
</style>