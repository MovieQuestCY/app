import { Team, User, UserCreation } from "../models/types";

class UserService {
    private userApiUrl = import.meta.env.VITE_APP_USERS_API_URL;
    private dbToken = localStorage.getItem("token");
    private static instance: UserService;

    static getInstance() {
        if (!UserService.instance) {
            UserService.instance = new UserService();
        }
        return UserService.instance;
    }

    async getUser(id: number): Promise<User> {
        const response = await fetch(`${this.userApiUrl}${id}?authToken=${this.dbToken}`);
        const user = await response.json();
        return user;
    }

    async getAllUsers(): Promise<User[]> {
        const response = await fetch(this.userApiUrl + `?authToken=${this.dbToken}`);
        const users = await response.json() as User[];
        return users;
    }

    async editUser(user: User): Promise<User> {
        const response = await fetch(`${this.userApiUrl}${user.id}?authToken=${this.dbToken}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        });
        const editedUser = await response.json();
        return editedUser;
    }

    

    async register(user: UserCreation): Promise<User> {
        const response = await fetch(this.userApiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        });
        const newUser = await response.json();
        return newUser;
    }

    async login(email: string, password: string): Promise<Response> {
        return await fetch(`${this.userApiUrl}login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
        });
    }
}

export default UserService;