# around-the-woodlands

Link-in-bio landing page for [@aroundwoodlandstx](https://instagram.com/aroundwoodlandstx) — the umbrella brand for Anthony's locally-made apps for The Woodlands area.

**Live:** https://compo-cf.github.io/around-the-woodlands/

## What's here

Single-page static site, no framework, no JS. Pure HTML + inline CSS for fast load and zero third-party dependencies.

Apps linked:
- **S-Tier Eats** — https://apps.apple.com/app/id6773501518
- **The Woodlands Fishing Guide** — https://apps.apple.com/us/app/the-woodlands-fishing-guide/id6773332173
- **Woodlands Trail Guide** — coming soon

Plus the Ko-fi tip jar ([ko-fi.com/subtlefoodie](https://ko-fi.com/subtlefoodie)).

## Files

```
index.html              Page itself (CSS inlined)
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

When the Trail Guide ships, replace the `disabled` card in `index.html` with a real `<a class="app-card" href="...">` (mirror the other two), drop the App Store URL in, commit and push. Pages redeploys automatically.
