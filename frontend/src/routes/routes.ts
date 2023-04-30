import Home from './../pages/Home.vue';
import About from './../pages/About.vue';
import Contact from './../pages/Contact.vue';
import Search from './../pages/Search.vue';
import Login from './../pages/Login.vue';
import Register from './../pages/Register.vue';
import Dashboard from './../pages/Dashboard.vue';
import UserMovies from './../components/dashboard/UserMovies.vue';
import UserTeams from './../components/dashboard/UserTeams.vue';
import FindMovies from './../components/dashboard/FindMovies.vue';
import Profile from './../components/dashboard/Profile.vue';

export const routes = [
    {
        path: '/',
        component: Home,
    },
    {
        path: '/about',
        component: About,
    },
    {
        path: '/contact',
        component: Contact,
    },
    {
        path: '/login',
        component: Login,
    },
    {
        path: '/register',
        component: Register,
    },
    {
        path: '/search/:movie',
        component: Search,
    },
    {
        path: '/dashboard',
        component: Dashboard,
        children: [
            {
                path: 'profile',
                component: Profile,
            },
            {
                path: 'movies',
                component: UserMovies,
            },
            {
                path: 'teams',
                component: UserTeams,
            },
            {
                path: 'find',
                component: FindMovies,
            },
        ]
    },
    {
        path: '/:catchAll(.*)',
        component: Home,
    }
];