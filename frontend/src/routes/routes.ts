import Home from './../pages/Home.vue';
import About from './../pages/About.vue';
import Contact from './../pages/Contact.vue';

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
        path: '/:catchAll(.*)',
        component: Home,
    }
];