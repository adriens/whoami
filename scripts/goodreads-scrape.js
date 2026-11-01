// Scrape l'étagère "read" Goodreads depuis un navigateur connecté (RSS coupé par Goodreads).
// Usage : sur https://www.goodreads.com (session ouverte), exécuter ce code dans la console,
// attendre window.__grStatus === 'done', puis copier JSON vers output/goodreads-124105866.json
// et lancer `task fetch-goodreads`. Pas de .entries()/for-of sur Array : Prototype.js (chargé
// par Goodreads) casse les itérateurs natifs. Pas de setTimeout non plus : Chrome bride les
// timers des onglets en arrière-plan (boucle figée) — chaque fetch (~1 s) suffit à espacer.
window.__grStatus = 'running'; window.__books = null;
(async () => {
  const USER = '124105866';
  const M = {Jan:'01',Feb:'02',Mar:'03',Apr:'04',May:'05',Jun:'06',Jul:'07',Aug:'08',Sep:'09',Oct:'10',Nov:'11',Dec:'12'};
  const iso = s => {
    s = (s || '').replace(/\[edit\]/g, '').trim();
    let m = s.match(/^(\w{3}) (\d{1,2}), (\d{4})$/); if (m) return `${m[3]}-${M[m[1]]}-${m[2].padStart(2, '0')}`;
    m = s.match(/^(\w{3}) (\d{4})$/); if (m) return `${m[2]}-${M[m[1]]}-01`;
    m = s.match(/^(\d{4})$/); return m ? `${m[1]}-01-01` : '';
  };
  const val = (tr, f) => {
    const td = tr.querySelector(`td.field.${f} .value`) || tr.querySelector(`td.field.${f}`);
    return td ? td.innerText.replace(/\s+/g, ' ').replace(/\[edit\]/g, '').trim() : '';
  };
  const parse = async url => new DOMParser().parseFromString(await (await fetch(url)).text(), 'text/html');
  const books = [];
  for (let page = 1; page < 20; page++) {
    const rows = (await parse(`/review/list/${USER}?shelf=read&per_page=100&page=${page}`)).querySelectorAll('tr.bookalike.review');
    if (!rows.length) break;
    for (let r = 0; r < rows.length; r++) {
      const tr = rows[r];
      const a = tr.querySelector('td.field.title a');
      const author = val(tr, 'author').replace(/\s*\*$/, '');
      const stars = tr.querySelectorAll('td.field.rating a.star.on').length;
      // 1ère session de lecture = date historique (celle qu'exposait le RSS)
      const readDate = tr.querySelector('td.field.date_read span.date_read_value');
      const year = val(tr, 'date_pub').match(/\d{4}/);
      books.push({
        reviewId: tr.id.replace('review_', ''),
        id: (a.getAttribute('href').match(/show\/(\d+)/) || [])[1],
        title: a.getAttribute('title') || a.innerText.trim(),
        // "Nom, Prénom" → "Prénom Nom" (format de l'ancien RSS)
        author: author.indexOf(',') >= 0 ? author.split(',').map(s => s.trim()).reverse().join(' ') : author,
        isbn: val(tr, 'isbn').replace(/^isbn\s*/, ''),
        rating: stars ? String(stars) : '',
        average_rating: val(tr, 'avg_rating').replace(/^avg rating\s*/, ''),
        num_pages: (val(tr, 'num_pages').match(/\d+/) || [''])[0],
        date_read: readDate ? iso(readDate.textContent.replace(/\s+/g, ' ')) : '',
        date_added: iso(val(tr, 'date_added').replace(/^date added\s*/, '')),
        published_year: year ? year[0] : '',
      });
    }
    window.__grStatus = `listed ${books.length}`;
    if (rows.length < 100) break;
  }
  // La liste tronque les reviews : texte intégral depuis la page de chaque review
  for (let i = 0; i < books.length; i++) {
    const e = (await parse(`/review/show/${books[i].reviewId}`)).querySelector('[itemprop=reviewBody], .reviewText');
    books[i].review = e ? e.innerHTML.trim().replace(/<br\s*\/?>/g, '<br />') : '';
    window.__grStatus = `reviews ${i + 1}/${books.length}`;
  }
  window.__books = books; window.__grStatus = 'done';
})().catch(e => { window.__grStatus = `error: ${e}`; });
