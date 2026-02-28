# Have you ever wanted to make a Minecraft bed texture resource pack because it sounds fun?

Here is a step-by-step guide that will (hopefully) help you make your own resource pack

# OPEN IN YOUR BROWSER
Click this link: https://mcbed-web.streamlit.app/


# or perhaps you would rather run the app yourself...
---
1.  # How to run the program:
    - Using only Python
        -   Install [Python](https://www.python.org/downloads/) (at least 3.13)
        -   Install [Pillow](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html) (at least 12.1.1)
        -   Install [Streamlit](https://docs.streamlit.io/get-started/installation) (at least 1.54.0)
        -   Download and open the folder for this project
        -   Open the terminal inside the folder
        -   Run `streamlit run main.py`
        -   **A browser window should open if successful**
    -   Using uv
        -   Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
        -   Download and open the folder for this project
        -   Open the terminal inside the folder
        -   Run `uv run streamlit run main.py`
        -   **A browser window should open if successful**
    
---
2.  # How to create your modified bed textures:
    -   Select the bed color
    -   Select how your image will be fit
        -   Crop (Default): image gets cropped in the center to a 1:2 ratio, then resized to 256x512
            -   Parts of the image may be cut off
        -   Stretch: image will be resized to be 256x512 with no respect to aspect ratio
            -   Image could end up looking very distorted
        -   Pad: image will be padded on the top to be 1:2 ratio, then resized to 256x512
            -   Image may look very small on the bottom of the bed
    -   Select your custom image
    -   Download your modified bed texture

---
3.  # How to add the modified bed textures to your resource pack:
    -   If you already have a resource pack set up/know how to make one:
        -   Copy your modified bed textures to the `textures/entity/bed` directory in your resource pack folder


    -   If you don't have a resource pack set up/know how to make one:
        -   [How to make a Bedrock resource pack](https://learn.microsoft.com/en-us/minecraft/creator/documents/resourcepack?view=minecraft-bedrock-stable)
        -   [Vanilla Bedrock resource pack reference](https://github.com/Mojang/bedrock-samples/tree/main/resource_pack)
        -   Quick guide to making a resource pack:
            -   Windows key + R -> Enter `%appdata%/Minecraft Bedrock/users/shared/games/com.mojang/development_resource_packs`
            -   Create a folder in above directory with the name of your resource pack
            -   Download/copy [the example manifest file](https://github.com/Mojang/bedrock-samples/blob/main/resource_pack/manifest.json) into your resource pack folder
                -   You don't have to edit this, but refer to the guide above for more information
            -   Create a `textures` folder and open the `textures` folder
            -   Create a `entity` folder and open the `entity` folder
            -   Create a `bed` folder and open the `bed` folder
            -   Copy your modified bed textures to the folder

---
4. # How to view your new Minecraft bed textures in-game:
    -   If you want to apply your resource pack globally to your own client:
        -   Go to *Settings*
        -   Go to down to *Global Resources*
        -   Activate the *Vanilla Resource Pack* (If you copied the manifest file) or the name of your resource pack
        -   **This will only apply to your game and in all your worlds**

    -   If you want to apply your resource pack to a specific world:
        -   Go to *Edit World* on the world you want to apply the resource pack
        -   Go to *Resource Packs*
        -   Activate the *Vanilla Resource Pack* (If you copied the manifest file) or the name of your resource pack
        -   **This will give the option for other players to download on multiplayer for that world only**