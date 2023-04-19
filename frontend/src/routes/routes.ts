import Home from './../pages/Home.vue';
import About from './../pages/About.vue';
import Contact from './../pages/Contact.vue';
import Search from './../pages/Search.vue';
import Login from './../pages/Login.vue';
import Register from './../pages/Register.vue';

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
        path: '/:catchAll(.*)',
        component: Home,
    }
];