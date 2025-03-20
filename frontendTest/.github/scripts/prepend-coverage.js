#!/usr/bin/env node
/* eslint-disable no-console */
const fs = require('fs');
const path = require('path');

// Se GITHUB_WORKSPACE non è definito, usiamo la cartella corrente
const workspace = process.env.GITHUB_WORKSPACE || process.cwd();

// Percorso del JSON di coverage
const coverageJsonPath = path.join(workspace, 'App/coverage/coverage-summary.json');

// Percorso del readme in minuscolo
const readmePath = path.join(workspace, 'readme.md');

try {
    // 1. Leggi il file coverage-summary.json
    const coverageData = JSON.parse(fs.readFileSync(coverageJsonPath, 'utf8'));

    // 2. Estrai i valori totali
    // (lines, statements, functions e branches)
    const { lines, statements, functions, branches } = coverageData.total;

    // 3. Calcola la media (o usa la metrica che preferisci)
    const avgCoverage = (
        (lines.pct + statements.pct + functions.pct + branches.pct) / 4
    ).toFixed(2);

    // Testo da scrivere in README
    const coverageText = `Coverage Totale: **${avgCoverage}%**`;

    // 4. Leggi il contenuto di readme.md
    let readmeContent = fs.readFileSync(readmePath, 'utf8');

    // 5. Rimuovi l'eventuale blocco coverage esistente
    //    (ci basiamo su commenti speciali)
    const coverageBlockRegex = /<!-- COVERAGE-START -->([\s\S]*?)<!-- COVERAGE-END -->/;
    readmeContent = readmeContent.replace(coverageBlockRegex, '').trim();

    // 6. Crea il nuovo blocco coverage
    const newCoverageBlock = `
<!-- COVERAGE-START -->
${coverageText}
<!-- COVERAGE-END -->
`.trim();

    // 7. Prependi il blocco coverage all’inizio del file
    const newReadme = `${newCoverageBlock}\n\n${readmeContent}\n`;

    // 8. Sovrascrivi readme.md
    fs.writeFileSync(readmePath, newReadme, 'utf8');

    console.log(`✅ Copertura totale aggiornata: ${avgCoverage}%`);
    console.log('✅ File readme.md aggiornato correttamente!');
} catch (error) {
    console.error('❌ Errore durante l\'aggiornamento del README:', error);
    process.exit(1);
}
