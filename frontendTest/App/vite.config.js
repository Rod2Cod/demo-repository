import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  test: {
    environment: 'jsdom',
    coverage: {
      reporter: ['text', 'html', 'json-summary'], // 'text' genera l'output su stdout
      // Altri parametri a tua scelta, come 'exclude', 'include', etc.
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
