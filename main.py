import streamlit as st
import bed_img
import io

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

def color_selector():

    st.header('Select your bed color 😀', divider=True)
    bed_color = st.selectbox('Bed color:', BED_COLORS)

    st.session_state.bed_color = bed_color
    st.session_state.base_bed = bed_img.load_bed(bed_color)

    if st.session_state.base_bed:
        # Display a preview of the bed color
        st.image(st.session_state.base_bed, width=256)
    else:
        # Show missing bed texture warning
        st.write('Missing texture of this bed color...')

def image_selector():

    st.header('Select your custom image 😀', divider=True)
    # Select a custom image to put on the bed
    uploaded_img = st.file_uploader('Custom image:', type=['.png','.jpeg','.jpg','.webp'])
    st.session_state.custom_img = None

    if uploaded_img:
        # Set currently selected image
        st.session_state.custom_img = bed_img.load_img(uploaded_img)
    
    if st.session_state.custom_img:
        # Display a preview of your custom image
        st.image(st.session_state.custom_img, width=256)
    else:
        st.write('Waiting for a custom image...')

def modified_bed():

    st.header('Download your modified bed texture 😀', divider=True)
    # Show edited bed texture
    if st.session_state.custom_img and st.session_state.base_bed:
        st.subheader('Modified bed texture:')
        edited_img = bed_img.make_bed(st.session_state.base_bed, st.session_state.custom_img)
        
        buf = io.BytesIO()
        edited_img.save(buf, format='PNG')

        st.download_button('Download texture', buf.getvalue(), f"{st.session_state.bed_color}.png")
        st.image(edited_img, width=256)


def main():
    st.set_page_config('Minecraft Bed Texture')
    
    col1, col2, col3 = st.columns(3, gap='large')

    with col1:
        color_selector()

    with col2:
        image_selector()

    with col3:
        modified_bed()
        
if __name__ == "__main__":
    main()
