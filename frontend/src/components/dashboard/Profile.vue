<template>
    <section class="w-full h-full flex items-center justify-center">
        <div>
        <h1 class="text-3xl font-bold text-center">Your profile</h1>
        <img :src="newUser.profile_picture ?? 'https://thumbs.dreamstime.com/b/default-avatar-profile-vector-user-profile-default-avatar-profile-vector-user-profile-profile-179376714.jpg'" class="mx-auto rounded-full mt-5 w-60" />
        <div class="flex flex-col gap-y-5 mt-10">
            <div class="flex gap-3 items-center ">
                            <div class=" w-full">
                                <label class="block" for="firstname">Firstname <span class="text-red-500">*</span></label>
                                <input v-model="newUser.firstname" type="text" id="firstname" name="firstname"
                                    placeholder="Your firstname..." class="input"  />
                            </div>
                            <div class=" w-full">
                                <label class="block" for="lastname">Lastname <span class="text-red-500">*</span></label>
                                <input v-model="newUser.lastname" type="text" id="lastname" name="lastname"
                                    placeholder="Your lastname..." class="input"  />
                            </div>
                        </div>
            <div>
                <label for="username" class="text-lg font-medium">Username <span class="text-red-500">*</span></label>
                <input type="text" id="username" class="input" v-model="newUser.username" />
            </div>
            <div>
                <label for="email" class="text-lg font-medium">Email</label>
                <input disabled type="email" id="email" class="input opacity-50" v-model="newUser.email" />
            </div>
            <div>
                <label for="avatar" class="text-lg font-medium">Avatar</label>
                <input type="text" id="avatar" class="input" v-model="newUser.profile_picture" />
            </div>
                
            <button class="mx-auto gap-2 px-4 py-1 bg-red-500 text-white rounded-lg text-md hover:bg-red-600 transition-all duration-300" @click="handleSave">Save</button>

            <p class="text-red-500 text-center">{{ messageError }}</p>
            <p class="text-green-500 text-center">{{ messageSuccess }}</p>
        </div>
    </div>
    </section>
</template>

<script setup lang="ts">
import { useAuthStore } from '../../stores/authStore';
import {useUserStore} from '../../stores/userStore';
import { ref, onMounted } from 'vue';
import { User } from '../../models/types';
import UserService from '../../services/UserService';

const authStore = useAuthStore();
const userStore = useUserStore();
const userService = new UserService();

const messageError = ref('');
const messageSuccess = ref('');
const newUser = ref<User>(authStore.user);

const handleSave = async () => {
    if(!newUser.value.firstname || !newUser.value.lastname || !newUser.value.username) {
        messageError.value = 'Please fill all the required fields';
        return;
    }

    messageError.value = '';
    messageSuccess.value = 'Profile updated successfully';
    setTimeout(() => {
        messageSuccess.value = '';
    }, 5000);
    newUser.value = await userService.editUser(newUser.value);

    if(newUser.value) {
        authStore.setUser(newUser.value);
    }
}

onMounted(async () => {
    await userStore.getUserMovies(authStore.user);
    await userStore.getUserTeams(authStore.user);
})

</script>