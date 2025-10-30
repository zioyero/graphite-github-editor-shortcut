#!/usr/bin/env python3
"""Generate icons for the Graphite GitHub Editor Shortcut extension."""

from PIL import Image, ImageDraw, ImageFont

def create_icon(size, output_path):
    """Create a simple icon with a gradient background and a period symbol."""
    # Create a new image with a gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)

    # Create a gradient from purple to blue (Graphite/GitHub colors)
    for y in range(size):
        # Interpolate between purple (#8B5CF6) and blue (#0969DA)
        r = int(139 + (9 - 139) * (y / size))
        g = int(92 + (105 - 92) * (y / size))
        b = int(246 + (218 - 246) * (y / size))
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    # Draw a rounded rectangle background
    margin = size // 8
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=size // 6,
        fill=(255, 255, 255, 180)
    )

    # Draw a period symbol in the center
    # Calculate font size based on icon size
    font_size = int(size * 0.6)

    try:
        # Try to use a system font
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()

    # Draw the period character
    text = "."
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text
    x = (size - text_width) // 2 - bbox[0]
    y = (size - text_height) // 2 - bbox[1]

    # Draw shadow
    draw.text((x + 1, y + 1), text, fill=(0, 0, 0, 100), font=font)
    # Draw main text
    draw.text((x, y), text, fill=(50, 50, 50), font=font)

    # Save the icon
    img.save(output_path, 'PNG')
    print(f"Created {output_path} ({size}x{size})")

def main():
    """Generate all required icon sizes."""
    sizes = [16, 48, 128]

    for size in sizes:
        output_path = f"icon{size}.png"
        create_icon(size, output_path)

    print("\nAll icons created successfully!")

if __name__ == '__main__':
    main()
