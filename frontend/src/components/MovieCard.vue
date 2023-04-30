<template>
        <article class="relative rounded-lg overflow-hidden cursor-pointer"  @mouseenter="showText" @mouseleave="hideText">
            <img :id="'movie-poster-' + props.movie.id"
                class="absolute w-full h-full object-cover transition-all duration-200 ease-in-out transform"
                :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`"
                :alt="props.movie.title + ' poster'" />
            <div v-if="mousehover" class="p-5 relative h-full">
                <h1 v-if="!props.short" class="line-clamp-3 text-xl font-bold">{{ props.movie.title }}</h1>
                <h1 v-else class="text-sm font-medium">{{ props.movie.title }}</h1>
                <div v-if="!props.short">
                    <hr class="my-2 w-[80%] h-[1px] bg-gray-50" />
                    <p class="line-clamp-4 text-sm">{{ props.movie.overview }}</p>
                    <p class="text-red-500 absolute bottom-5 left-0 right-0 mx-auto w-fit underline text-md">
                        <i class="bi bi-cursor"></i> See more
                    </p>
                </div>
            </div>
           
        </article>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Movie } from "../models/types";

const mousehover = ref(false);

const props = defineProps<{
    movie: Movie;
    short?: boolean;
}>();

defineEmits(["close"]);

const showText = () => {
    mousehover.value = true;
    document
        .querySelector(`#movie-poster-${props.movie.id}`)!
        .classList.add("scale-105", "brightness-50", "blur-xl");
};

const hideText = () => {
    mousehover.value = false;
    document
        .querySelector(`#movie-poster-${props.movie.id}`)!
        .classList.remove("scale-105", "brightness-50", "blur-xl");
};
</script>

<style scoped>
article {
    aspect-ratio: 9/16 !important;
}
</style>
