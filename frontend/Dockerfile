# Usa un'immagine Node.js per lo sviluppo
FROM node:18 AS build-stage

# Imposta la directory di lavoro
WORKDIR /app

# Copia package.json e package-lock.json (o pnpm-lock.yaml) dalla cartella `App`
COPY App/package*.json ./
# Se usi pnpm:
# COPY App/pnpm-lock.yaml ./

# Installa le dipendenze
RUN npm install
# Se usi pnpm:
# RUN npm install -g pnpm && pnpm install

# Copia il resto dell'applicazione
COPY App ./

# Espone la porta su cui gira Vue.js
EXPOSE 5173

# Comando di avvio per lo sviluppo
CMD ["npm", "run", "dev", "--", "--host"]
