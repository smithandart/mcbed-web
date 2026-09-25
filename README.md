# Have you ever wanted to make a Minecraft bed texture resource pack because it sounds fun?

Yeah, this whole project will make an entire Minecraft resource pack for you.

# OPEN IN YOUR BROWSER
Click this link: https://mcbed-web.streamlit.app/

---
    
# USING THE APP:
## How to create your own custom resource pack:
-   Set your resource pack name **OR LEAVE AS DEFAULT**
-   Set your resource pack description **OR LEAVE AS DEFAULT**
-   Set your resource pack icon **OR DON'T NOTHING IS ALSO FINE**

-   Select how your image will be fit  **OR LEAVE AS DEFAULT**
    -   ***Stretch*** (Default): image will be resized to be 256x512 with no respect to aspect ratio
        -   Image could end up looking very distorted
    -   ***Crop***: image gets cropped in the center to a 1:2 ratio, then resized to 256x512
        -   Parts of the image may be cut off
    -   ***Pad***: image will be padded on the top to be 1:2 ratio, then resized to 256x512
        -   Image may look very small
-   Select your custom image for each color **DOES NOT NEED AN IMAGE FOR EVERY COLOR**
-   Click the `CREATE RESOURCE PACK` button
-   Click the `DOWNLOAD RESOURCE PACK` button

## How to add your new Minecraft bed resource pack in-game:
-   Click the `.mcpack` file you just downloaded
-   Minecraft should open and start importing your resource pack

-   If you want to apply your resource pack globally to your own client:
    -   Go to `Settings`
    -   Go to `Global Resources`
    -   Activate the name of your resource pack in `MY PACKS`
    -   **This will only apply to your game and in all your worlds**

-   If you want to apply your resource pack to a specific world:
    -   Go to `Play`
    -   Click `Edit` or the pencil button on the world you want to use
    -   Go to `Resource packs`
    -   Go to `Available`
    -   Go to `Owned`
    -   Activate the name of your resource pack in `MY PACKS`
    -   **This will give the option for other players to download on multiplayer for that world only**

---
# or perhaps you would rather run the app yourself...
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

