<template>
    <section class="container">
        <div class="py-20 w-1/3 mx-auto text-center">
            <h2 class="text-2xl text-red-500 uppercase tracking-[1.5rem]">
                MovieQuest
            </h2>
            <h1 class="text-6xl font-extrabold">Login</h1>
        </div>

        <form class="px-5 md:px-0 md:w-3/4 lg:w-1/3 mx-auto pb-20 opacity-90">
            <div class="flex flex-col gap-5">
                <div class="px-3">
                    <label class="block" for="email">Email</label>
                    <input v-model="formData.email" type="email" id="email" name="email" placeholder="Your email..." class="input" />
                </div>
                <div class="px-3">
                    <label class="block" for="password">Password</label>
                    <input v-model="formData.password" type="password" id="password" name="password" placeholder="Your password..." class="input" />
                </div>
                <button @click="handleSubmit" type="button" id="submit"
                    class="block w-fit mx-auto bg-red-500 px-4 py-2 rounded-md cursor-pointer hover:bg-red-600 transition-all">
                    Login
                </button>
                <p class=" text-center">New to MovieQuest ? <router-link to="/register" class="underline">Register here</router-link>.</p>
                <p class="text-red-500 text-center">{{ errorMessage }}</p>
            </div>
        </form>
    </section>
</template>

<script setup lang="ts">
import { ref } from "vue";

const errorMessage = ref<string>('');
const formData = ref<Record<string, string>>({
    email: "",
    password: "",
});

const handleSubmit = () => {
    if (formData.value.email === "" || formData.value.password === "") {
        errorMessage.value = "Please fill in all fields";
        return;
    }

    errorMessage.value = "";
    console.log(formData.value);
};
</script>