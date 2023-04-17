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

        <router-link to="/login" class="flex gap-2 px-4 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300">Login</router-link>
    </nav>
</template>