from generator import Abstract
import config
import datetime
import os

def main():
    os.makedirs(config.DIR, exist_ok=True)
    today = datetime.date.today().strftime("%Y-%m-%d")
    path = f"{config.DIR}/{today}.{config.FORMAT}"
    art_gen = Abstract(shape_n=config.SHAPE_N, img_size=config.IMG_SIZE)
    art_gen.generate(path)
    print(f"Art saved to: {path}")

if __name__ == "__main__":
    main()