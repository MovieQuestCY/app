import {defineStore} from 'pinia';
import { User } from '../models/types';
import UserService from '../services/UserService';
import router from '../routes';
import VueCookies from 'vue-cookies';

const userService = new UserService();

interface UserWithToken extends User {
    token: string;
}

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('user') || '{}') as User,
        token: localStorage.getItem('token') || '',
    }),
    getters: {
        isAuth: (state) => state.user.id !== undefined,
    },
    actions: {
        async login(email: string, password: string): Promise<void | Error> {
            const response: Response = await userService.login(email, password);
            const user: UserWithToken = await response.json();

            if(user.token !== undefined) {
                this.user = user as User;
                this.token = user.token;
                localStorage.setItem('user', JSON.stringify(user));
                VueCookies.set('authToken', user.token);
                router.push('/dashboard/profile');
            } else {
                switch (response.status) {
                    case 401:
                        return new Error('Invalid credentials');
                    case 404:
                        return new Error('User not found');
                    default:
                        return new Error('Login failed');
                }
            }
        },
        async logout() {
            this.user = {} as User;
            localStorage.removeItem('user');
            localStorage.removeItem('movies');
            localStorage.removeItem('teams');
            VueCookies.remove('authToken');
            router.push('/login');
        },
        async setUser(user: User) {
            this.user = user;
            localStorage.setItem('user', JSON.stringify(user));
        }
    }
});