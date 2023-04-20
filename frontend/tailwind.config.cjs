/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  safelist: [
    'bg-gray-700',
     'border-gray-600'
  ],
  theme: {
    extend: {
      container: {
        center: true,
      },
      height: {
        'navbar-dashboard': "calc(100vh - 132px)",
      },
      minHeight: {
        'navbar-dashboard': "calc(100vh - 132px)",
      }
    },
  },
  plugins: [],
}
