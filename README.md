# around-the-woodlands

Link-in-bio landing page for [@aroundwoodlandstx](https://instagram.com/aroundwoodlandstx) — the umbrella brand for Anthony's locally-made apps for The Woodlands area.

**Live:** https://compo-cf.github.io/around-the-woodlands/

## What's here

Single-page static site, no framework, no JS. Pure HTML + inline CSS for fast load and zero third-party dependencies.

Apps linked:
- **S-Tier Eats** (iPhone) — https://apps.apple.com/app/id6773501518
- **S-Tier Eats for Android** — https://play.google.com/store/apps/details?id=com.compofelice.stiereats
- **The Woodlands Fishing Guide** — https://apps.apple.com/us/app/the-woodlands-fishing-guide/id6773332173
- **Woodlands Trail Guide** — https://apps.apple.com/us/app/woodlands-trail-guide/id6785576912

Also by the developer:
- **Cosmica: Idle Universe** — https://apps.apple.com/us/app/cosmica-idle-universe/id6784340038
- **Pupdoku: Puppy Puzzles** — https://apps.apple.com/us/app/id6797896315

Plus the Ko-fi tip jar ([ko-fi.com/subtlefoodie](https://ko-fi.com/subtlefoodie)).

## Files

```
index.html              Page itself (CSS inlined)
icons/                  App icons for the cards, from the store listings
icon.png                512px hero icon
icon-master.png         1024px master, not served
favicon.png             256px tab icon
apple-touch-icon.png    180px iOS home-screen icon
og-image.png            1200x630 social-share card
scripts/build_assets.py Regenerate all derived images from icon-master.png
```

To regenerate the derived images after editing the master:

```
python scripts/build_assets.py
```

## Hosting

GitHub Pages, served from `main` branch root.

To enable on a fresh fork: Settings -> Pages -> Source: `main`, folder: `/ (root)` -> Save. Wait ~30 seconds for first publish.

## Updating apps

Each app is one `<a class="app-card" href="...">` block in `index.html`. The four field guides use the large card (`app-card--lg`: icon, kicker, detailed description and a store button) and the "Also by the developer" games use the compact row card. Phones get one column; from 760px up the large cards sit in a 2x2 grid. Copy whichever card fits, change the icon, name, description and URL, then commit and push. Pages redeploys automatically. A second platform gets its own card, as with S-Tier Eats for Android.

Each card shows the app's real icon from `icons/` (PNGs at 3x the size they're shown: 256px for the large cards, 168px for the compact ones, so they stay sharp on retina; the page rounds the corners). For an iOS app, `https://itunes.apple.com/lookup?id=<appId>` returns `artworkUrl512`; resize that to 168px. For a Play-only app use the icon from the Play listing. Use each platform's own icon, because they can differ (S-Tier Eats' Android icon has no letters on the bars). Re-fetch when an app changes its icon.

Write descriptions from the live store listing (the App Store page carries the full text), not from memory, and only claim features that ship on that platform. Only link apps that have a public store listing; Play closed-test apps return 404.

If an app name appears in the share image, change the text in `scripts/build_assets.py` and re-render only `og-image.png`. Running the whole script also rewrites the icons.
