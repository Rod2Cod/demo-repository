<!-- COVERAGE-START -->
Coverage Totale: **98.36%**
<!-- COVERAGE-END -->

# Avvio dell'Applicazione Vue.js e Test con Docker e Node.js

Guida su come avviare l'applicazione, eseguire test e visualizzare i report di coverage del codice utilizzando Docker o Node.js.

---

## Requisiti

- **Docker**: Assicurati che Docker sia installato e configurato correttamente.
- **Node.js**: Verifica di avere installato Node.js e npm (oppure pnpm se lo utilizzi).

---

## Con Docker

> **Nota**: Assicurati di eseguire i comandi nella directory del progetto `docker-vue`.

### Avvio dell'applicazione
1. Costruzione e avvio in modalità detached:
   ```bash
   docker-compose up --build -d
   ```

2. L'applicazione sarà disponibile all'indirizzo:
   [http://localhost:5173](http://localhost:5173)

### Esecuzione dei test
1. Avvia i test unitari:
   ```bash
   docker exec -it frontend-app npm run tests
   ```

2. Genera il report di coverage del codice:
   ```bash
   docker exec -it frontend-app npm run tests:coverage
   ```

### Arresto dell'applicazione
1. Per fermare i container Docker:
   ```bash
   docker-compose down
   ```

### Visualizzazione dei log
1. Per visualizzare i log di un container:
   ```bash
   docker logs frontend-app
   ```

2. Per visualizzare i log in tempo reale:
   ```bash
   docker logs -f frontend-app
   ```

---

## Con Node.js

> **Nota**: Assicurati di eseguire i comandi nella directory del progetto `App`.

### Avvio dell'applicazione
1. Avvio in locale:
   ```bash
   npm run dev
   ```

2. Avvio con esposizione su tutti gli indirizzi IP della macchina:
   ```bash 
   npm run host
   ```

3. L'applicazione sarà disponibile all'indirizzo:
   [http://localhost:5173](http://localhost:5173)

### Esecuzione dei test
1. Avvia i test unitari:
   ```bash
   npm run tests
   ```

2. Genera il report di coverage del codice:
   ```bash
   npm run tests:coverage
   ```

### Arresto dell'applicazione
1. Per fermare il processo Node.js, utilizza la combinazione di tasti:
   ```
   CTRL + C
   ```

### Visualizzazione dei log
I log di Node.js sono visibili direttamente nella console quando avvii il processo utilizzando `npm run dev` o `npm run host`.

---

## Visualizzazione del report di coverage

Il report di coverage è disponibile in formato HTML e può essere visualizzato aprendo il file `index.html` nella cartella `coverage`. I comandi per aprire il file su diversi sistemi operativi sono indicati di seguito:

### Linux
```bash
xdg-open coverage/index.html
```

### Windows
```cmd
start coverage\index.html
```

### MacOS
```bash
open coverage/index.html
```

---

## Struttura dei comandi

### Comandi per Docker

| **Comando**                                       | **Descrizione**                                   | **Directory**                                                                 |
|---------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------|
| `docker-compose up --build -d`                   | Costruisce e avvia l'app in modalità detached.  | [`docker-vue`](./docker-vue)                                                 |
| `docker exec -it frontend-app npm run test`      | Esegue i test unitari.                         | [`docker-vue`](./docker-vue)                                                 |
| `docker exec -it frontend-app npm run test:coverage` | Genera il report di test coverage.            | [`docker-vue`](./docker-vue)                                                 |
| `docker-compose down`                            | Ferma i container e rimuove le reti.           | [`docker-vue`](./docker-vue)                                                 |
| `docker logs frontend-app`                       | Mostra i log del container Docker.             | [`docker-vue`](./docker-vue)                                                 |
| `docker logs -f frontend-app`                    | Mostra i log in tempo reale del container Docker. | [`docker-vue`](./docker-vue)                                               |

---

### Comandi per Node.js

| **Comando**                                       | **Descrizione**                                   | **Directory**                                                                 |
|---------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------|
| `npm run dev`                                    | Avvia l'applicazione in modalità locale.        | [`App`](./App)                                                       |
| `npm run host`                                   | Avvia l'app con esposizione su tutti gli IP.   | [`App`](./App)                                                       |
| `npm run test`                                   | Esegue i test unitari.                         | [`App`](./App)                                                       |
| `npm run test:coverage`                          | Genera il report di test coverage.            | [`App`](./App)                                                       |
| `CTRL + C`                                       | Ferma il processo Node.js in esecuzione.       | [`App`](./App)                                                       |

---

### Comandi per visualizzare il report di coverage

| **Sistema Operativo** | **Comando**                     | **Descrizione**                                   | **Directory**                                                                 |
|------------------------|---------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------|
| Linux                 | `xdg-open coverage/index.html` | Apre il report di coverage.                     | [`App/coverage/index.html`](./App/coverage/index.html)               |
| Windows               | `start coverage\index.html`   | Apre il report di coverage.                     | [`App/coverage/index.html`](./App/coverage/index.html)               |
| MacOS                 | `open coverage/index.html`     | Apre il report di coverage.                     | [`App/coverage/index.html`](./App/coverage/index.html)               |
## Code Coverage Report
```json
{
  "statements": null,
  "branches": null,
  "functions": null,
  "lines": null
}
```
