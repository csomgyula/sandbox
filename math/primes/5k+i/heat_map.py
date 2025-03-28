import numpy as np
import csv
from PIL import Image, ImageDraw, ImageFont
import argparse

def interpolate_color(min_color, max_color, value, min_value, max_value):
    """Interpolates between min_color and max_color based on value in range [min_value, max_value]."""
    ratio = (value - min_value) / (max_value - min_value) if max_value > min_value else 0
    return tuple(int(min_c + ratio * (max_c - min_c)) for min_c, max_c in zip(min_color, max_color))

def generate_heatmap(file_path, values, cell_size, min_color, max_color, labels=None):
    """Generates and saves a heatmap image based on the given matrix."""
    values = np.array(values)
    min_value, max_value = np.min(values), np.max(values)
    rows, cols = values.shape
    img_width, img_height = cols * cell_size[0], rows * cell_size[1]
    image = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(image)
    
    for i in range(rows):
        for j in range(cols):
            color = interpolate_color(min_color, max_color, values[i, j], min_value, max_value)
            x0, y0 = j * cell_size[0], i * cell_size[1]
            x1, y1 = x0 + cell_size[0], y0 + cell_size[1]
            draw.rectangle([x0, y0, x1, y1], fill=color)
            
            if labels is not None:
                value = labels[i][j]
                try:                
                    value = int(value)
                except:
                    pass
                text = str(value)                                
                
                try:
                    font = ImageFont.load_default()
                except:
                    font = None  # Fallback if no default font available
                text_size = draw.textbbox((0, 0), text, font=font) if font else (0, 0, 0, 0)
                text_width, text_height = text_size[2] - text_size[0], text_size[3] - text_size[1]
                text_x = x0 + (cell_size[0] - text_width) // 2
                text_y = y0 + (cell_size[1] - text_height) // 2
                draw.text((text_x, text_y), text, fill="black", font=font)
    
    image.save(file_path)

def load_csv(file_path):
    """Loads a CSV file and returns a matrix as a list of lists."""
    with open(file_path, newline='') as csvfile:
        return [list(map(float, row)) for row in csv.reader(csvfile, delimiter=',')]

def main():
    parser = argparse.ArgumentParser(description="Generate a heatmap from a CSV file.")
    parser.add_argument("values_csv",   help="Path to the CSV file containing the heat values.", default ="heat_map_values.csv")
    parser.add_argument("output_image", help="Path to save the output heatmap image.", default = "heat_map.png")
    parser.add_argument("--labels_csv", help="Path to the CSV file containing labels (optional).", default=None)
    parser.add_argument("--cell_size",  type=int, nargs=2, default=[50, 50], help="Cell size in pixels (width height).")
    
    # https://www.schemecolor.com/neutral-blues.php
    parser.add_argument("--min_color",  type=int, nargs=3, default=[10*16+13, 12*16+ 4, 13*16+13], help="RGB color for the minimum value.")
    parser.add_argument("--max_color",  type=int, nargs=3, default=[ 7*16+10,  9*16+15, 12*16+15], help="RGB color for the maximum value.")
    args = parser.parse_args()
    values = load_csv(args.values_csv)
    #print(f"DEBUG\tvalues:\n{values}")
    labels = load_csv(args.labels_csv) if args.labels_csv else None
    
    generate_heatmap(
        args.output_image,
        values,
        tuple(args.cell_size),
        tuple(args.min_color),
        tuple(args.max_color),
        labels
    )
    
if __name__ == "__main__":
    main()
