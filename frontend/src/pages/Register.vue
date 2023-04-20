<template>
    <section class="container">
        <div class="pt-20 w-1/3 mx-auto text-center">
            <h2 class="text-2xl text-red-500 uppercase tracking-[1.5rem]">
                MovieQuest
            </h2>
            <h1 class="text-6xl font-extrabold">Register</h1>
        </div>

        <Steppy v-model:step="step" v-model:tabs="tabs" v-model:nextText="nextLabel" v-model:primaryColor1="primaryColor1"
            v-model:primaryColor2="primaryColor2" v-model:doneText="doneLabel" v-model:finalize="handleSubmit" class="md:w-3/4 lg:w-3/4 mx-auto">
            <template #1>
                <form class="px-5 md:px-0 opacity-90" @input="handleChangeForm">
                    <div class="flex flex-col gap-5">
                        <div class="flex gap-3 items-center ">
                            <div class=" w-full">
                                <label class="block" for="firstname">Firstname</label>
                                <input v-model="formData.firstname" type="text" id="firstname" name="firstname"
                                    placeholder="Your firstname..." class="input"  />
                            </div>
                            <div class=" w-full">
                                <label class="block" for="lastname">Lastname</label>
                                <input v-model="formData.lastname" type="text" id="lastname" name="lastname"
                                    placeholder="Your lastname..." class="input"  />
                            </div>
                        </div>
                        <div>
                            <label class="block" for="username">Username</label>
                            <input v-model="formData.username" type="text" id="username" name="username"
                                placeholder="Your username..." class="input"  />
                        </div>
                        <div>
                            <label class="block" for="email">Email</label>
                            <input v-model="formData.email" type="email" id="email" name="email" placeholder="Your email..."
                                class="input"  />
                        </div>
                        <div class="flex gap-3 items-center">
                            <div class=" w-full">
                                <label class="block" for="password">Password</label>
                                <input v-model="formData.password" type="password" id="password" name="password"
                                    placeholder="Your password..." class="input"  />
                            </div>
                            <div class=" w-full">
                                <label class="block" for="password">Confirm password</label>
                                <input v-model="formData.confirmPassword" type="password" id="confirmPassword" name="password" placeholder="Your password..."
                                    class="input"  />
                            </div>
                        </div>
                        <p class=" text-center">Already user ? <router-link to="/login" class="underline">Login here</router-link>.</p>
                        <p class="text-red-500 text-center">{{ errorMessage }}</p>
                    </div>
                </form>
            </template>
            <template #2>
                <div class="flex justify-center gap-3">
                    <ul>
                        <li class="text-xl" v-for="(element, index) in genres" :key="element.id">{{ index + 1 }}.<br /></li>
                    </ul>
                    <draggable class="cursor-pointer" v-model="genresList" group="people"
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
            <template #3>
                <h1 class="text-xl font-medium">Here are some existing Teams. Join some to meet people with the same interests!</h1>
                <ul>
                    <li @click="selectTeam(team.id)" class="cursor-pointer py-1 my-3 rounded-lg border-2 bg-gray-800 border-gray-700 hover:bg-gray-700 hover:border-gray-600 transition-all duration-300" :class="{'bg-gray-600 border-gray-500' : team.isSelected}" v-for="team in teamsExamples" :key="team.id">{{ team.name }} <i class="bi bi-check-lg text-green-500" v-if="team.isSelected"></i></li>
                </ul>
            </template>
        </Steppy>

    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { Steppy } from 'vue3-steppy';
import draggable from 'vuedraggable';
import { genres } from "../utils/genres";
import TeamService from "../services/TeamService";
import UserService from "../services/UserService";
import { TeamResponse, User, UserCreation } from "../models/types";
import router from "../routes";

interface TeamSelection extends TeamResponse {
    isSelected: boolean;
}

interface Genre {
    id: number;
    name: string;
}

const teamService = new TeamService();
const userService = new UserService();

const step = ref<number>(1);
const nextLabel = ref<string>("Continue");
const doneLabel = ref<string>("Register");
const primaryColor1 = ref<string>("#ef4444");
const primaryColor2 = ref<string>("#111827");
const tabs = ref<any>([
    { title: "Informations", isValid: false },
    { title: "Your favorite genres", isValid: true },
    { title: "Join a team", isValid: true },
]);
const errorMessage = ref<string>('');
const formData = ref<Record<string, string>>({
    email: "",
    password: "",
    confirmPassword: "",
});
const genresList = ref<any>(genres);
const teamsExamples = ref<TeamSelection[]>([]);


const handleChangeForm = () => {
    if(formData.value.email !== "" && formData.value.password !== "" && formData.value.confirmPassword !== "" && formData.value.firstname !== "" && formData.value.lastname !== "" && formData.value.username !== ""){
        if(formData.value.password.length < 6) {
            errorMessage.value = "Password must be at least 6 characters long";
            return;
        }
    
        if(formData.value.email.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/) === null) {
            errorMessage.value = "Please enter a valid email";
            return;
        }
    
        if (formData.value.password !== formData.value.confirmPassword) {
            errorMessage.value = "Passwords do not match";
            return;
        }

        tabs.value[0].isValid = true;
        errorMessage.value = "";
    }

};

const selectTeam = (id: number) => {
    teamsExamples.value = teamsExamples.value.map((team) => {
        if(team.id === id) {
            team.isSelected = !team.isSelected;
        }
        return team;
    });
};

onMounted(async () => {
    const teamsResponse = (await teamService.getAllTeams()).slice(0, 5) as TeamResponse[];
    const teams = teamsResponse.map((team) => ({ ...team, isSelected: false }));
    teamsExamples.value = teams;
});


const handleSubmit = async () => {
    const newUser: UserCreation = {
        email: formData.value.email,
        password: formData.value.password,
        firstname: formData.value.firstname,
        lastname: formData.value.lastname,
        username: formData.value.username,
        favorite_genres: genresList.value.map((genre: Genre) => genre.name).join(","),
    };
    try {
        const responseUser = await userService.register(newUser) as User;
        if(!responseUser) {
            errorMessage.value = "An error occured";
            return;
        } else {
            const selectedTeams = teamsExamples.value.filter((team) => team.isSelected).map((team) => team.id);
            for (const teamId of selectedTeams) {
                await teamService.addUserToTeam(teamId, responseUser.id);
            }
            router.push("/");
        }
    } catch (error) {
        console.error(error);
    }
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