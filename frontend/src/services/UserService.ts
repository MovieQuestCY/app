import { User, UserCreation } from "../models/types";

class UserService {
    private userApiUrl = "http://localhost:8082/users";
    private static instance: UserService;

    static getInstance() {
        if (!UserService.instance) {
            UserService.instance = new UserService();
        }
        return UserService.instance;
    }

    async getUser(id: number): Promise<User> {
        const response = await fetch(`${this.userApiUrl}/${id}`);
        const user = await response.json();
        return user;
    }

    async getAllUsers(): Promise<User[]> {
        const response = await fetch(this.userApiUrl);
        const users = await response.json() as User[];
        return users;
    }

    async registerUser(user: UserCreation): Promise<User> {
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
}

export default UserService;