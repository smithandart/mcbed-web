import streamlit as st
import bed_img
import io
import zipfile

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

# The part that lets the user select an option for how the image will be fit on the bed
def image_fit() -> None:
    st.header('Choose how your image will fit 😀', divider=True)
    option = st.selectbox('image fit selection', ['stretch','crop','pad'], label_visibility='hidden')

    if option:
        st.session_state.image_fit = option

# The image selection widgets that ask the user to give an image
@st.fragment
def image_selector(key):
    st.subheader(f"{key} 😀", text_alignment='right')
    # Select a custom image to put on the bed
    st.file_uploader('image uploader', type=IMAGE_FORMATS, label_visibility='hidden', key=key)

def image_download():
    st.header('Process your images 😀', divider=True)
    if st.button('CREATE ZIP'):

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            
            for color in BED_COLORS:
                    print('process', color)

                    if st.session_state[color]:
                        st.subheader(f"processing {color}")

                        img_buffer = io.BytesIO()

                        bed_img.make_bed(
                            bed_img.load_bed(color),
                            bed_img.load_img(st.session_state[color]),
                            st.session_state['image_fit']
                        ).save(img_buffer, format='PNG')

                        zip_file.writestr(f"{color}.png", img_buffer.getvalue())

                    else:
                        print('nothing uploaded')

        zip_buffer.seek(0)

        st.download_button('DOWNLOAD ZIP', data=zip_buffer, file_name='bed_textures.zip', mime='application/zip')

def main():
    # RUN IT UP
    st.set_page_config('Minecraft Bed Texture')

    col1, col2, col3 = st.columns(3, border=True)

    with col1:

        image_fit()
        image_download()


    with col2:

        st.header('Upload files for each bed color 😀', divider=True)
        for color in BED_COLORS[0:8]:
            image_selector(color)

    with col3:

        st.header('Upload files for each bed color 😀', divider=True)
        for color in BED_COLORS[8:16]:
            image_selector(color)

        

    
if __name__ == "__main__":
    main()
