<template>
    <main class="flex items-center min-h-navbar-dashboard py-10">
        <nav class="px-2 flex flex-col gap-y-5 items-stretch h-navbar-dashboard sticky left-0 top-0 justify-center">
            <router-link to="/dashboard"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard' }">Dashboard</router-link>
            <router-link to="/dashboard/movies"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/movies' }">User movies</router-link>
            <router-link to="/dashboard/teams"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/teams' }">User teams</router-link>
            <router-link to="/dashboard/find"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/find' }">Find movies</router-link>

        </nav>
        <div class="w-[1px] h-navbar-dashboard sticky left-0 top-0  bg-gray-400 mr-2" />
        <div class="flex-1 h-navbar-dashboard overflow-y-auto">
            <h1>Dashboard</h1>
            <p>Here is the dashboard</p>
            <router-view />
        </div>
    </main>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { ref, watch } from 'vue';

const router = useRouter();

const currentRoute = ref<string>(router.currentRoute.value.path);

watch(router.currentRoute, (route) => {
    currentRoute.value = route.path;
});
</script>