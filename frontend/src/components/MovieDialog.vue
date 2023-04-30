<template>
    <section class="fixed top-0 left-0 h-screen w-screen overflow-hidden bg-gray-900/90 z-[998] flex justify-center items-center">
        <div class="p-5 bg-gray-800 rounded-xl flex flex-col w-4/5">
            <div class="w-full clear-both">
                
            </div>
            <div class="p-5 flex gap-5">
                <img class="h-[600px]" :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`" :alt="props.movie.title + ' poster'" />
                <div class="flex flex-col w-full">
                    <div class="flex justify-between items-start">
                        <h1 class="text-3xl font-bold">{{ props.movie.title }}</h1>
                        <i class="bi bi-x text-4xl text-gray-700 cursor-pointer float-right hover:text-red-500 transition-all duration-300" @click="$emit('close')"></i>
                    </div>
                    <p class="text-gray-400 text-sm">Release date: <span class="text-red-500">{{ props.movie.release_date }}</span></p>
                    <hr class="my-2 w-[80%] h-[1px] bg-gray-50" />
                    <p class="text-gray-300 opacity-70">{{ props.movie.overview }}</p>

                    <div class="grid grid-cols-2 gap-5 pt-5">
                        <div class="col-span-1">
                            <p><i class="bi bi-stars opacity-70 text-lg"></i> Vote average : <span class="text-red-500">{{ props.movie.vote_average ?? '-' }}</span> / 10</p>
                        </div>
                        <div class="col-span-1">
                            <p><i class="bi bi-people opacity-70 text-lg"></i> Popularity : <span class="text-red-500">{{ props.movie.popularity ?? '-' }}</span></p>
                        </div>
                    </div>

                    <div v-if="authStore.isAuth" class=" self-end mt-auto">
                        <button v-if="hasWatched" class="bg-red-500 hover:bg-red-600 transition-all duration-300 text-white rounded-lg px-5 py-2 " @click="handleRemoveMovie">Remove from your movies</button>
                        <button v-else class="bg-red-500 hover:bg-red-600 transition-all duration-300 text-white rounded-lg px-5 py-2 " @click="handleAddMovie">Add to your movies</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import { Movie } from '../models/types';
import { useAuthStore } from '../stores/authStore';
import { useUserStore } from '../stores/userStore';

const authStore = useAuthStore();
const userStore = useUserStore();

const user = authStore.user ?? null;

const props = defineProps<{
    movie: Movie;
    fromtmbd: boolean;
}>();

const hasWatched = ref(userStore.hasWatchedMovie(props.movie));

const handleAddMovie = async () => {
    await userStore.watchMovie(user, props.movie);
    hasWatched.value = true;
}

const handleRemoveMovie = async () => {
    await userStore.unwatchMovie(user, props.movie);
    hasWatched.value = false;
}
</script>