<template>
    <nav class="container flex justify-between items-center pt-5 ">
        <ul class="flex gap-10 justify-center font-medium">
            <li>
                <router-link to="/" class="hover:text-red-500 transition-all duration-300">Home</router-link>
            </li>
            <li>
                <router-link to="/about" class="hover:text-red-500 transition-all duration-300">About</router-link>
            </li>
            <li>
                <router-link to="/register" class="hover:text-red-500 transition-all duration-300">Contact</router-link>
            </li>
        </ul>

        <div class="flex gap-2 items-center">
            <input @keyup.enter="search" v-model="currentSearch" type="text" class="w-full px-2 py-[2px] border-2 border-gray-600 bg-gray-700 rounded-lg focus-visible:outline-none" placeholder="Search for a movie (Ctrl+K)" />
            <button @click="search" class="flex gap-2 px-4 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300">Search</button>
        </div>
    </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const currentSearch = ref('');

const search = () => {
    let encoded = encodeURI(currentSearch.value);
    router.push(`/search/${encoded}`);
}
</script>