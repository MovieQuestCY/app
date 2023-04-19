import { Team, TeamResponse } from "../models/types";

class TeamService {
    private teamApiUrl = "http://localhost:8082/teams";
    private static instance: TeamService;

    static getInstance() {
        if (!TeamService.instance) {
            TeamService.instance = new TeamService();
        }
        return TeamService.instance;
    }

    async getTeam(id: number): Promise<TeamResponse> {
        const response = await fetch(`${this.teamApiUrl}/${id}`);
        const team = await response.json();
        return team;
    }

    async getAllTeams(): Promise<TeamResponse[]> {
        const response = await fetch(this.teamApiUrl);
        const teams = await response.json() as TeamResponse[];
        return teams;
    }

    async addUserToTeam(teamId: number, userId: number): Promise<Team> {
        const response = await fetch(`${this.teamApiUrl}/${teamId}/add_user/${userId}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        });
        const team = await response.json();
        return team;
    }
}

export default TeamService;