import streamlit as st
import bed_img

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



def main():
    st.set_page_config('Minecraft Bed Texture')
    bed_color = st.selectbox('Bed color', BED_COLORS)


    original_bed = bed_img.preview_img(bed_img.load_bed(bed_color))
    if original_bed:
        # Display a preview of the bed color
        bed_preview = st.image(original_bed)
    else:
        missing_bed = st.text('Missing image of this bed color')

    # Select a custom image to put on the bed
    uploaded_img = st.file_uploader('Custom image', type=['.png','.jpeg','.jpg','.webp'])
    custom_img = None
    if uploaded_img:
        # Set currently selected image
        custom_img = bed_img.load_img(uploaded_img)
    
    if custom_img:
        # Display a preview of your custom image
        custom_preview = st.image(bed_img.preview_img(custom_img))

    # Show edited bed texture
    if custom_img and original_bed:
        st.subheader('Custom bed')
        edited_img = st.image(bed_img.make_bed(original_bed, custom_img))

if __name__ == "__main__":
    main()
