<template>
    <main class="flex items-center min-h-navbar-dashboard py-10">
        <nav class="px-2 flex flex-col gap-y-5 items-stretch h-navbar-dashboard sticky left-0 top-0 justify-center">
            <router-link to="/dashboard/profile"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/profile' }">Profile</router-link>
            <router-link to="/dashboard/movies"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/movies' }">Your movies</router-link>
            <router-link to="/dashboard/teams"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/teams' }">Your teams</router-link>
            <router-link to="/dashboard/find"
                class="hover:bg-gray-700 hover:text-gray-200 rounded-lg transition-all duration-300 px-10 py-2 w-full self-stretch border-2 border-gray-900"
                :class="{ 'bg-gray-700 !border-gray-600': currentRoute === '/dashboard/find' }">Find movies</router-link>
            <p class="text-red-500 hover:text-red-700 transition-all duration-300 px-10 py-2 w-full self-stretch cursor-pointer" @click="handleLogout">Logout</p>

        </nav>
        <div class="w-[1px] h-navbar-dashboard sticky left-0 top-0  bg-gray-400 mr-2" />
        <div class="flex-1 h-navbar-dashboard overflow-y-auto p-8">
            <router-view />
        </div>
    </main>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { ref, watch } from 'vue';
import { useAuthStore } from '../stores/authStore';

const router = useRouter();
const authStore = useAuthStore();

const currentRoute = ref<string>(router.currentRoute.value.path);

const handleLogout = async () => {
    await authStore.logout();
    router.push('/');
}

watch(router.currentRoute, (route) => {
    currentRoute.value = route.path;
});
</script>