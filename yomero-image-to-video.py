import cv2
import glob
import gradio as gr

def convert_images_to_video(carpeta):
    images = []
    filenames = sorted(glob.glob(carpeta + '/*.jpg'))
    for filename in filenames:
        images.append(cv2.imread(filename))

    height, width, layers = images[0].shape
    video = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))

    for image in images:
        video.write(image)

    video.release()

    return 'video.mp4'

input = gr.inputs.Textbox(label='Carpeta de imágenes')
output = gr.outputs.Textbox(label='Archivo de vídeo')

gr.Interface(fn=convert_images_to_video, inputs=input, outputs=output).launch()
