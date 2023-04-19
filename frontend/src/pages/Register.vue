<template>
    <section class="container">
        <div class="pt-20 w-1/3 mx-auto text-center">
            <h2 class="text-2xl text-red-500 uppercase tracking-[1.5rem]">
                MovieQuest
            </h2>
            <h1 class="text-6xl font-extrabold">Register</h1>
        </div>

        <Steppy v-model:step="step" v-model:tabs="tabs" v-model:nextText="nextLabel" v-model:primaryColor1="primaryColor1"
            v-model:primaryColor2="primaryColor2" v-model:doneText="doneLabel" class="md:w-3/4 lg:w-1/2 mx-auto">
            <template #1>
                <form class="px-5 md:px-0 opacity-90">
                    <div class="flex flex-col gap-5">
                        <div class="px-3">
                            <label class="block" for="email">Email</label>
                            <input v-model="formData.email" type="email" id="email" name="email" placeholder="Your email..."
                                class="input" />
                        </div>
                        <div class="px-3">
                            <label class="block" for="password">Password</label>
                            <input v-model="formData.password" type="password" id="password" name="password"
                                placeholder="Your password..." class="input" />
                        </div>
                        <p class="text-red-500 text-center">{{ errorMessage }}</p>
                    </div>
                </form>
            </template>
            <template #2>
                <div class="flex justify-center gap-3">
                    <ul>
                        <li class="text-xl" v-for="(element, index) in genres" :key="element.id">{{ index + 1 }}.<br /></li>
                    </ul>
                    <draggable class="cursor-pointer" v-model="genresList" group="people" @change="onGenreChange($event)"
                        item-key="id">
                        <template #item="{ element }">
                            <div class="flex items-center gap-2">
                                <i class="bi bi-grip-vertical text-gray-500 text-xl"></i>
                                <div>{{ element.name }}</div>
                            </div>
                        </template>
                    </draggable>
                </div>
            </template>
            <template #3><!-- Step 3 Content --></template>
        </Steppy>

    </section>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Steppy } from 'vue3-steppy';
import draggable from 'vuedraggable';
import { genres } from "../utils/genres";

const step = ref<number>(1);
const drag = ref<boolean>(false);
const nextLabel = ref<string>("Continue");
const doneLabel = ref<string>("Register");
const primaryColor1 = ref<string>("#ef4444");
const primaryColor2 = ref<string>("#111827");
const tabs = ref<any>([
    { title: "Informations", isValid: true },
    { title: "Your favorite genres", isValid: true },
    { title: "Join a team", isValid: true },
]);
const errorMessage = ref<string>('');
const formData = ref<Record<string, string>>({
    email: "",
    password: "",
});
const genresList = ref<any>(genres);

const handleSubmit = () => {
    if (formData.value.email === "" || formData.value.password === "") {
        errorMessage.value = "Please fill in all fields";
        return;
    }

    errorMessage.value = "";
    console.log(formData.value);
};

const onGenreChange = (event: any) => {
    console.log(genresList.value);
};
</script>

<style>
.steppy-pane {
    background-color: transparent !important;
    box-shadow: none !important;
    color: #f9fafb !important;
}

.steppy-item-title {
    white-space: nowrap !important;
}
</style>