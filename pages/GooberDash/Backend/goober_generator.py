from PIL import Image
import os


# For ear of devil hat
def apply_color_tint(image, tint_color):
    image = image.convert("RGBA")
    width, height = image.size
    tint_r, tint_g, tint_b, tint_a = tint_color

    for x in range(width):
        for y in range(height):
            r, g, b, a = image.getpixel((x, y))
            new_r = int((r * (255 - tint_a) + tint_r * tint_a) / 255)
            new_g = int((g * (255 - tint_a) + tint_g * tint_a) / 255)
            new_b = int((b * (255 - tint_a) + tint_b * tint_a) / 255)
            image.putpixel((x, y), (new_r, new_g, new_b, a))

    return image


# For ear of devil hat
def get_pixel_color(image, coord):
    return image.getpixel(coord)


def compose_images(layers, base_path):
    images = [
        Image.open(os.path.join(base_path, f"{layer}.png")).convert("RGBA")
        for layer in layers
    ]
    width, height = images[0].size
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for img in images:
        canvas = Image.alpha_composite(canvas, img)

    return canvas, images


def generate_goober(hat, suit, hand, color):
    layers = []

    # 1_left_hand_and_leg
    if color != "color_skelly":
        if suit == "suit_robot":
            layers.append("1_left_hand_and_leg/left_hand_and_leg_robot")
        else:
            layers.append("1_left_hand_and_leg/left_hand_and_leg")

    # 2_suit_back
    suit_back_list = [
        "suit_angel",
        "suit_archer",
        "suit_beaver",
        "suit_bee",
        "suit_bunny",
        "suit_cat",
        "suit_devil",
        "suit_dino",
        "suit_dog",
        "suit_koala",
        "suit_lion",
        "suit_monkey",
        "suit_polar",
    ]
    if suit in suit_back_list:
        layers.append(f"2_suit_back/{suit}")

    # 3_hat_back
    hat_back_list = [
        "hat_alien",
        "hat_antennae",
        "hat_bunny",
        "hat_monkey",
        "hat_polar",
        "hat_robot",
        "hat_wig",
    ]
    if hat in hat_back_list:
        layers.append(f"3_hat_back/{hat}")

    # 4_hand_back
    hand_back_list = ["hand_bow", "hand_sai"]
    if hand in hand_back_list:
        layers.append(f"4_hand_back/{hand}")

    # 5_color
    try:
        layers.append(f"5_color/{color}")
    except Exception:
        layers.append("5_color/color_default")

    # 6_mouth
    if color != "color_skelly":
        layers.append("6_mouth/mouth")

    # 7_eyes
    if color != "color_skelly":
        layers.append("7_eyes/eyes")

    # 8_suit
    try:
        layers.append(f"8_suit/{suit}")
    except Exception:
        layers.append("8_suit/suit_default")

    # 9_right_leg
    if color != "color_skelly":
        if suit == "suit_robot":
            layers.append("9_right_leg/right_leg_robot")
        else:
            layers.append("9_right_leg/right_leg")

    # 10_hat
    try:
        layers.append(f"10_hat/{hat}")
        if hat == "hat_devil":
            layers.append("10_hat/hat_devil_ear")
    except Exception:
        layers.append("10_hat/hat_default")

    # 11_hand
    try:
        layers.append(f"11_hand/{hand}")
    except Exception:
        layers.append("11_hand/hand_default")

    # 12_right_hand
    if suit == "suit_robot":
        layers.append("12_right_hand/right_hand_robot")
    elif color == "color_skelly":
        layers.append("12_right_hand/right_hand_skelly")
    else:
        layers.append("12_right_hand/right_hand")

    # 13_suit_front
    suit_front_list = ["suit_viking", "suit_wizard"]
    if suit in suit_front_list:
        layers.append(f"13_suit_front/{suit}")

    base_path = "./static/GooberDash/goober"

    # Compose images without tint
    canvas, images = compose_images(layers, base_path)
    intermediate_output_path = "/tmp/intermediate_output.png"
    canvas.save(intermediate_output_path)

    # Load the intermediate composed image
    composed_image = Image.open(intermediate_output_path)

    if hat == "hat_devil":
        # Extract tint color from the final output
        coord = (190, 210)
        tint_color = get_pixel_color(composed_image, coord)

        # Apply tint to the specific layer
        for i, layer in enumerate(layers):
            if layer == "10_hat/hat_devil_ear":
                images[i] = apply_color_tint(images[i], tint_color)

        # Compose images with the tinted layer
        final_canvas = Image.new("RGBA", (canvas.width, canvas.height), (0, 0, 0, 0))
        for img in images:
            final_canvas = Image.alpha_composite(final_canvas, img)

        # Display the final image
        final_output_path = "/tmp/output.png"
        final_canvas.save(final_output_path)
    else:
        final_output_path = intermediate_output_path

    return final_output_path
