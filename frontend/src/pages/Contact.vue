<template>
    <section class="container">
        <div class="py-20 w-2/3 mx-auto text-center">
            <h2 class="text-2xl text-red-500 uppercase tracking-[1.5rem]">
                MovieQuest
            </h2>
            <h1 class="text-6xl font-extrabold">Contact</h1>
        </div>

        <form class="px-5 md:px-0 md:w-3/4 lg:w-2/3 mx-auto pb-20 opacity-90">
            <div class="grid grid-cols-2">
                <div class="col-span-2 md:col-span-1 px-3 my-2">
                    <label class="block" for="firstname">First Name</label>
                    <input type="text" id="firstname" name="firstname" placeholder="Your first name..." class="input" />
                </div>
                <div class="col-span-2 md:col-span-1 px-3 my-2">
                    <label class="block" for="lastname">Last Name</label>
                    <input type="text" id="lastname" name="lastname" placeholder="Your last name..." class="input" />
                </div>
                <div class="col-span-2 px-3 my-2">
                    <label class="block" for="email">Email</label>
                    <input type="email" id="email" name="email" placeholder="Your email..." class="input" />
                </div>
                <div class="col-span-2 px-3 my-2">
                    <label class="block" for="subject">Subject</label>
                    <input type="text" id="subject" name="subject" placeholder="Subject..." class="input" />
                </div>
                <div class="col-span-2 px-3 my-2">
                    <label class="block" for="message">Message</label>
                    <textarea id="message" name="message" rows="5" placeholder="Your message..." class="input"></textarea>
                    <div class="col-span-2 my-4">
                        <button @click="handleSubmit" type="button" id="submit"
                            class="block w-fit mx-auto bg-red-500 px-4 py-2 rounded-md hover:cursor-pointer hover:bg-red-600 transition-all !opacity-100">
                            Send
                        </button>
                    </div>
                    <p class="text-red-500 text-center">{{ errorMessage }}</p>
                </div>
            </div>
        </form>
    </section>
</template>

<script setup lang="ts">
import { ref } from "vue";

const errorMessage = ref<string>("");
const handleSubmit = () => {
    errorMessage.value = "This is a fake form, please don't try to send anything";
};
</script>
