# Apex Collision Center Website

Production static website for **Apex Collision Center**, 4544 Dufferin Street, North York, ON M3H 5X2.
Live target: **https://apexcollisioncenter.ca** (GitHub Pages + custom domain).

## What is here

- 25 pages: home, about, services overview, 18 individual service pages, gallery, reviews, FAQ, contact with online booking form
- 20 AI generated photographic images in `assets/img/` plus the brand logo and favicon set
- Shared design system in `assets/css/style.css`, interactions in `assets/js/main.js`
- SEO and AI discoverability: `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, JSON-LD (AutoRepair, Service, FAQPage, BreadcrumbList) on every page, Open Graph and Twitter cards, canonical URLs
- `CNAME` file with the custom domain, `.nojekyll` for GitHub Pages

## Preview locally

```bash
cd ~/workspace/apex-collision-center
python3 -m http.server 8080
# open http://localhost:8080
```

## Rebuild after content changes

All copy lives in `site_data.py`. Page structure lives in `build.py`. To change text, services, hours or FAQs, edit `site_data.py` and run:

```bash
python3 build.py
```

Never edit the generated HTML by hand; it will be overwritten.

## Deploy to GitHub Pages

The `gh` CLI is available but not logged in yet. Steps:

```bash
cd ~/workspace/apex-collision-center
git init
git add .
git commit -m "Apex Collision Center website launch"
gh auth login
gh repo create apexcollisioncenter --public --source=. --push
```

Then in the repo on GitHub: Settings > Pages > Deploy from branch > `main` / root.
Add the custom domain `apexcollisioncenter.ca` in the Pages settings (the `CNAME` file is already in the repo).

## DNS (Cloudflare, apexcollisioncenter.ca)

GitHub Pages custom domain needs these records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<github-username>.github.io` |

Set them to **DNS only** (grey cloud) until GitHub issues the certificate, then proxying can be re-enabled. GitHub provisions HTTPS automatically; allow up to 24 hours.

Email records (Brevo, Cloudflare Email Routing) already in place: do not touch the MX, TXT, DKIM or DMARC rows.

## Booking form

GitHub Pages is static, so the booking form composes a pre addressed email to mustafa@apexcollisioncenter.ca via the visitor's own email app. No backend needed.

## Notes for the owner

- Reviews on the Reviews page are representative samples. Replace them with real Google reviews once the Google Business profile is live.
- The gallery note says photos are representative. Swap in real shop photos any time by replacing files in `assets/img/` (keep the same filenames) and rerunning the local preview. No rebuild needed for image swaps.
- Service list reflects the approved 18 services (timing belt, transmission rebuild, wheel alignment, tire sales, throttle body and safety inspection were removed per the owner).
