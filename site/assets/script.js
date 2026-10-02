// Mobile menu
const menuBtn = document.querySelector('.menu-btn');
const nav = document.getElementById('nav');
if (menuBtn && nav) {
  menuBtn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open);
  });
}

// Quote / contact form.
// Set FORM_ENDPOINT to a Formspree (or similar) URL to receive submissions by email.
// Until then, the form falls back to opening the visitor's email app, addressed to the agency.
const FORM_ENDPOINT = '';
const FALLBACK_EMAIL = 'keytoinsurance@hotmail.com';
const ES = document.documentElement.lang === 'es';

document.querySelectorAll('form.quote').forEach((form) => {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (form.querySelector('.hp').value) return; // honeypot
    const data = Object.fromEntries(new FormData(form));
    delete data.website;
    const msg = form.querySelector('.form-msg');

    if (FORM_ENDPOINT) {
      try {
        const res = await fetch(FORM_ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(data),
        });
        if (!res.ok) throw new Error();
        form.reset();
        msg.textContent = ES ? '¡Gracias! Recibimos su solicitud y le llamaremos pronto.' : 'Thanks! We got your request and will call you back shortly.';
        msg.classList.add('show');
        return;
      } catch {
        msg.textContent = ES ? 'Algo salió mal. Por favor llámenos al 786.417.2459.' : 'Something went wrong. Please call us at 786.417.2459.';
        msg.classList.add('show');
        return;
      }
    }

    const body = Object.entries(data).map(([k, v]) => `${k}: ${v}`).join('\n');
    location.href = `mailto:${FALLBACK_EMAIL}?subject=${encodeURIComponent((ES ? 'Solicitud de cotización – ' : 'Quote request – ') + (data.coverage || 'General'))}&body=${encodeURIComponent(body)}`;
  });
});
