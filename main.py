import streamlit as st
import bed_img
import io
import zipfile
import json
import uuid

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
    st.selectbox('image fit selection', ['stretch','crop','pad'], label_visibility='hidden', key='image_fit')


# The image selection widgets that ask the user to give an image
@st.fragment
def image_selector(key):
    st.subheader(f"{key} 😀", text_alignment='right')
    # Select a custom image to put on the bed
    st.file_uploader('', type=IMAGE_FORMATS, label_visibility='hidden', key=key)

def pack_download():
    st.header('Process your resource pack 😀', divider=True)
    if st.button('CREATE RESOURCE PACK'):

        # This is the buffer the pack will be stored in as a zip file
        zip_buffer = io.BytesIO()

        # start a zip file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:

            # Go through each bed color
            for color in BED_COLORS:

                    # Check if a color has an uploaded image
                    if st.session_state[color]:

                        # make a buffer to save the images to
                        img_buffer = io.BytesIO()

                        # Make the custom bed texture and save to the buffer
                        bed_img.make_bed(
                            bed_img.load_bed(color),
                            bed_img.load_img(st.session_state[color]),
                            st.session_state['image_fit']
                        ).save(img_buffer, format='PNG')

                        # write the image to the zip file
                        zip_file.writestr(f"textures/entity/bed/{color}.png", img_buffer.getvalue())


            # Check if an icon image has been uploaded
            if st.session_state['pack_icon']:
                img_buffer = io.BytesIO()

                # make a 128x128 version of the icon image and save
                bed_img.square_img(bed_img.load_img(st.session_state['pack_icon'])).save(img_buffer, format='PNG')

                zip_file.writestr('pack_icon.png', img_buffer.getvalue())

            zip_file.writestr('manifest.json', generate_manifest())

        # return the buffer to the beginning
        zip_buffer.seek(0)

        # create the download button
        st.download_button('DOWNLOAD RESOURCE PACK', data=zip_buffer, file_name='custom_beds.mcpack', mime='application/zip')

def pack_info():
    st.header('Change the information for your resource pack 😀', divider=True)

    # pack name
    st.text_input('name', value='custom beds', key='pack_name')

    # pack description
    st.text_input('description', value='this pack changes beds', key='pack_desc')

    # pack icon
    st.file_uploader('icon', type=IMAGE_FORMATS, key='pack_icon')


# create the json string for the manifest file
def generate_manifest():

     # standard example manifest file
    base_manifest = {
        'format_version': 2,
        'header': {
            'description': 'this pack changes beds',
            'name': 'custom_beds',
            'uuid': str(uuid.uuid4()),
            'version': [0,0,1],
            'min_engine_version': [1,26,50]
        },
        'modules': [
            {
                'description': 'this pack changes beds',
                'type': 'resources',
                'uuid': str(uuid.uuid4()),
                'version': [0,0,1]
            }
        ]
    }

    # check for a custom name
    if st.session_state['pack_name']:
        base_manifest['header']['name'] = st.session_state['pack_name']

    # check for a custom description
    if st.session_state['pack_desc']:
        base_manifest['header']['description'] = st.session_state['pack_desc']
        base_manifest['modules'][0]['description'] = st.session_state['pack_desc']

    # dump it as a json string
    return json.dumps(base_manifest)

def main():
    # RUN IT UP
    st.set_page_config('Minecraft Bed Resource Pack Generator')


    st.link_button('I NEED HELP', 'https://github.com/smithandart/mcbed-web/blob/main/README.md', width='stretch')

    # col1, col2, col3 = st.columns(3, border=True)

    with st.expander('SETTINGS'):

        pack_info()
        image_fit()

    with st.expander('BED COLORS (KINDA NECESSARY)'):
        st.header('Upload files for each bed color 😀', divider=True)
        for color in BED_COLORS:
            image_selector(color)

    pack_download()

    


        

    
if __name__ == "__main__":
    main()
