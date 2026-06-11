from pathlib import Path
from PIL import Image
import colorsys

def clamp(value):
    return max(0, min(255, int(value)))

def rgb_to_hsl(rgb):
    r, g, b = [v / 255 for v in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, s, l

def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (clamp(r * 255), clamp(g * 255), clamp(b * 255))

def similar_colors(rgb):
    h, s, l = rgb_to_hsl(rgb)
    variants = [
        (h, s, l),
        (h, min(1, s + 0.08), min(1, l + 0.08)),
        (h, max(0, s - 0.08), max(0, l - 0.08)),
        (h, s, min(1, l + 0.04))
    ]
    return [hsl_to_rgb(*v) for v in variants]

def enlarge_image():
    image_input = input("Enter the full path to your image: ").strip().strip('"')
    img_path = Path(image_input)

    if not img_path.exists():
        raise FileNotFoundError(f"Missing image file: {img_path}")

    img = Image.open(img_path).convert("RGB")
    width, height = img.size

    new_img = Image.new("RGB", (width * 2, height * 2))
    pixels = img.load()
    new_pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            c1, c2, c3, c4 = similar_colors(pixels[x, y])
            nx, ny = x * 2, y * 2
            new_pixels[nx, ny] = c1
            new_pixels[nx + 1, ny] = c2
            new_pixels[nx, ny + 1] = c3
            new_pixels[nx + 1, ny + 1] = c4

    output_path = img_path.with_name("output.png")
    new_img.save(output_path)
    print(f"Saved {output_path}")
    new_img.show()
    return new_img

if __name__ == "__main__":
    enlarge_image()