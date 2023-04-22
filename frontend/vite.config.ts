import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    watch: {
      ignored: ['!**/node_modules/your-package-name/**'],
      usePolling: true
    },
  },
  define: {
    'process.env': process.env
  }
  


})
