import streamlit as st
import bed_img
import io

# File names of each bed color in Minecraft
BED_COLORS = [
    'white',
    'silver',
    'gray',
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'lime',
    'green',
    'cyan',
    'light_blue',
    'blue',
    'purple',
    'magenta',
    'pink'
]

# Image file formats currently accepted
IMAGE_FORMATS = [
    '.png',
    '.jpeg',
    '.jpg',
    '.webp'
]

# The section that lets the user select a bed color and shows the bed texture for reference
def color_selector():
    st.header('Select your bed color 😀', divider=True)
    bed_color = st.selectbox('bed color selection', BED_COLORS, label_visibility='hidden')

    st.session_state.bed_color = bed_color
    st.session_state.base_bed = bed_img.load_bed(bed_color)

    if st.session_state.base_bed:
        # Display a preview of the bed color
        st.image(st.session_state.base_bed, width=256)
    else:
        # Show missing bed texture warning
        st.write('Missing texture of this bed color...')

# The part that lets the user select an option for how the image will be fit on the bed
def image_fit() -> None:
    st.header('Choose how your image will fit 😀', divider=True)
    option = st.selectbox('image fit selection', ['crop','stretch','pad'], label_visibility='hidden')

    if option:
        st.session_state.image_fit = option

# The image selection service that asks the user to give an image
def image_selector():
    st.header('Select your custom image 😀', divider=True)
    # Select a custom image to put on the bed
    uploaded_img = st.file_uploader('image uploader', type=IMAGE_FORMATS, label_visibility='hidden')
    st.session_state.custom_img = None

    if uploaded_img:
        # Set currently selected image
        st.session_state.custom_img = bed_img.load_img(uploaded_img)
    
    if st.session_state.custom_img:
        # Display a preview of your custom image
        st.image(st.session_state.custom_img, width=256)
    else:
        st.write('Waiting for a custom image...')

# This is how the user can see how the final product will look and can enter their credit card information to download
def modified_bed():
    st.header('Download your modified bed texture 😀', divider=True)
    # Show edited bed texture
    if st.session_state.custom_img and st.session_state.base_bed:
        st.subheader('Modified bed texture:')

        # I LOVE SESSION STATE SO MUCH
        st.session_state.edited_bed = bed_img.make_bed(st.session_state.base_bed, st.session_state.custom_img, fit=st.session_state.image_fit)
        
        buf = io.BytesIO()
        st.session_state.edited_bed.save(buf, format='PNG')

        st.download_button('Download texture', buf.getvalue(), f"{st.session_state.bed_color}.png")
        st.image(st.session_state.edited_bed, width=256)


def main():
    # RUN IT UP
    st.set_page_config('Minecraft Bed Texture')
    
    color_selector()

    image_fit()

    image_selector()

    modified_bed()
    
if __name__ == "__main__":
    main()
