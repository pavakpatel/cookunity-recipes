# CookUnity recipe collection

A printable collection of 14 meals, with photos, published ingredient details, source links, and estimated home recipes.

**[Open the recipe collection](https://pavakpatel.github.io/cookunity-recipes/)**

CookUnity's meal pages provide ingredients, nutrition, and reheating directions, but do not publish measured recipes for cooking from scratch. The home recipes here are original, untested reconstructions with estimated quantities and methods. Published nutrition applies to the delivered meals, not these reconstructions.

The collection was assembled from CookUnity pages on September 8 and 10, 2026. Meal photos come from the corresponding CookUnity listings. This is an independent personal collection, not an official CookUnity publication.

## Files

- `index.html`: the website, with a Print / Save PDF button.
- `recipes.md`: recipes in Markdown.
- `recipes.json`: structured recipe data.
- `source-details.json`: published ingredient labels and meal facts.
- `photos.json` and `images/`: photo mappings and local image files.
- `build_collection.py` and `additional_recipes.py`: the collection generator and additional recipe definitions.

Rebuild with Python 3:

```sh
python3 build_collection.py
```

GitHub Pages serves the root of the `main` branch. All photos and site assets are stored locally in the repository.
