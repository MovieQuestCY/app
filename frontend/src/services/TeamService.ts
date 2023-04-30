import { Team, TeamResponse, User } from "../models/types";

class TeamService {
    private teamApiUrl = import.meta.env.VITE_APP_TEAMS_API_URL;
    private dbToken = localStorage.getItem("token");
    private static instance: TeamService;

    static getInstance() {
        if (!TeamService.instance) {
            TeamService.instance = new TeamService();
        }
        return TeamService.instance;
    }

    async getTeam(id: number): Promise<TeamResponse> {
        const response = await fetch(`${this.teamApiUrl}/${id}?authToken=${this.dbToken}`);
        const team = await response.json();
        return team;
    }

    async getAllTeams(): Promise<TeamResponse[]> {
        const response = await fetch(this.teamApiUrl);
        const teams = await response.json() as TeamResponse[];
        return teams;
    }

    async createTeam(name: string, userId: number): Promise<TeamResponse> {
        const response = await fetch(this.teamApiUrl + `?authToken=${this.dbToken}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ 
                name: name,
                user_id: userId,
             }),
        });
        const team = await response.json();
        return team;
    }

    async addUserToTeam(teamId: number, userId: number): Promise<Team> {
        const response = await fetch(`${this.teamApiUrl}${teamId}/add_user/${userId}?authToken=${this.dbToken}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        });
        const team = await response.json();
        return team;
    }

    async removeUserFromTeam(teamId: number, userId: number): Promise<Team> {
        const response = await fetch(`${this.teamApiUrl}${teamId}/remove_user/${userId}?authToken=${this.dbToken}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        });
        const team = await response.json();
        return team;
    }

    async getUserTeams(userId: number): Promise<Team[]> {
        const response = await fetch(`${this.teamApiUrl}${userId}/teams?authToken=${this.dbToken}`);
        const teams = await response.json() as Team[];
        return teams;
    }

    async getTeamMembers(teamId: number): Promise<User[]> {
        const response = await fetch(`${this.teamApiUrl}${teamId}/users?authToken=${this.dbToken}`);
        const team = await response.json() as User[];
        return team;
    }
}

export default TeamService;