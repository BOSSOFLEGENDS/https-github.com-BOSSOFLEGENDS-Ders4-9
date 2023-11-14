import os

def change(old, new):
    try:
        os.rename(old, new)
        print(f"{old} changed with {new}") # f-string
    except FileNotFoundError:
        print(f"{old} cannot found.")
    except FileExistsError:
        print(f"we have already {old} file")

for sub_file in os.listdir("images"):
    resimler = os.listdir("images/" + sub_file)
    for sira, resim in enumerate(resimler):
        yol = "images/" + sub_file + "/"
        change(yol+resim, yol + "img" + str(sira) + ".png")
        # old -> yol+resim
        # new -> "img" + str(sira) + ".png"  img0.png  img1.png



