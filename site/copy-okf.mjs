// Copie le bundle OKF généré (output/okf) dans public/okf avant le build Astro,
// pour qu'il soit déployé sur GitHub Pages (/whoami/okf/...).
// Source de vérité = output/okf (commité) ; public/okf est gitignoré (régénéré).
import { existsSync, cpSync } from 'node:fs';

const src = '../output/okf';
const dest = 'public/okf';

if (existsSync(src)) {
  cpSync(src, dest, { recursive: true });
  console.log('OKF bundle copié → public/okf');
} else {
  console.warn('output/okf absent — copie OKF ignorée (lancer `task build-okf`)');
}
