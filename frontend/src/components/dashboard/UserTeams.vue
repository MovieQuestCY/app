<template>
    <div class="flex justify-between items-center">
        <h1 class="text-3xl font-bold ">Your teams</h1>
        <div class="flex gap-2 items-center">
            <input v-model="newTeam" type="text" class=" px-2 py-[2px] border-2 border-gray-600 bg-gray-700 rounded-lg focus-visible:outline-none focus:border-gray-300 transition-all duration-300" placeholder="Team name" />
            <button @click="createTeam" class="flex gap-2 px-4 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300">Create</button>
            <p>{{ message }}</p>
        </div>
    </div>
    <ul class="py-8 flex flex-col gap-2">
        <li v-for="team in teams" :key="team.id" class="bg-gray-800 border-2 border-gray-700 px-4 py-2 rounded-md flex justify-between items-center">
            <p class="text-lg">{{ team.name }}</p>
            <button @click="leaveTeam(team)" class="px-2 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300">Leave</button>
        </li>
    </ul>
    <h1 class="text-3xl font-bold pt-3">Other existing teams</h1>
    <ul class="py-8 flex flex-col gap-2">
        <li v-for="team in allTeams" :key="team.id" class="bg-gray-800 border-2 border-gray-700 px-4 py-2 rounded-md flex justify-between items-center">
            <p class="text-lg">{{ team.name }}</p>
            <button @click="joinTeam(team)" class="px-2 py-1 bg-blue-500 text-white rounded-lg text-md hover:bg-blue-600 transition-all duration-300">Join</button>
        </li>
    </ul>
</template>

<script setup lang="ts">
import { TeamResponse } from '../../models/types';
import { ref, onMounted } from 'vue';
import {useUserStore} from '../../stores/userStore';
import {useAuthStore} from '../../stores/authStore';
import TeamService from '../../services/TeamService';

const userStore = useUserStore();
const authStore = useAuthStore();
const teamService = new TeamService();

const teams = ref<TeamResponse[]>([]);
const allTeams = ref<TeamResponse[]>([]);
const newTeam = ref<string>('');
const message = ref<string>('');
const currentUser = authStore.user;

const createTeam = async () => {
    if(!newTeam.value) {
        message.value = 'Please enter a team name';
        setTimeout(() => {
            message.value = '';
        }, 3000);
        return;
    }
    const team = await userStore.createTeam(currentUser, newTeam.value);
    localStorage.setItem('teams', JSON.stringify([...teams.value, team]));
    teams.value = [...teams.value, team];
};

const joinTeam = async (team: TeamResponse) => {
    await userStore.joinTeam(currentUser, team);
    localStorage.setItem('teams', JSON.stringify([...teams.value, team]));
    teams.value = [...teams.value, team];
};

const leaveTeam = async (team: TeamResponse) => {
    await userStore.leaveTeam(currentUser, team);
    localStorage.setItem('teams', JSON.stringify(teams.value.filter((t: TeamResponse) => t.id !== team.id)));
    teams.value = teams.value.filter((t: TeamResponse) => t.id !== team.id);
};

onMounted(async () => {
    if (localStorage.getItem('teams')) {
        const teamsFromLocalStorage = localStorage.getItem('teams');
        const teamsFromLocalStorageParsed = JSON.parse(teamsFromLocalStorage!);
        teams.value = teamsFromLocalStorageParsed;
    } else {
        await userStore.getUserTeams(currentUser);
        teams.value = userStore.teams;
    }

    allTeams.value = (await teamService.getAllTeams()).filter((team: TeamResponse) => {
        return !teams.value.some((userTeam: TeamResponse) => userTeam.id === team.id);
    });
});
</script>