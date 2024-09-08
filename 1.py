import gradio as gr
from PIL import Image

def image_processor(image1, image2):
    try:
        if image1 is None or image2 is None:
            return None
      
        # 定义A点和B点的坐标
        A = (2109, 516)
        B = (4636, 1458)
      
        # 计算覆盖区域的宽度和高度
        width = B[0] - A[0]
        height = B[1] - A[1]
      
        # 将img2调整大小以匹配覆盖区域
        image2_resized = image2.resize((width, height))

        # 将调整大小后的img2粘贴到img1的A点位置
        image1.paste(image2_resized, A)
      
        # 返回合并后的图像
        return image1
    except Exception as e:
        return None


def clear_image():
    return None, None, None

with gr.Blocks() as demo:
    with gr.Row():
        img1 = gr.Image(label="器材图片", sources=["upload", "clipboard"], type="pil")
        img2 = gr.Image(label="投影图片", sources=["upload", "clipboard"], type="pil")
        img3 = gr.Image(show_download_button=True, type="pil")
    
    with gr.Row():
        merge_btn = gr.Button("合并", )
        clear_btn = gr.Button("清除", )

    merge_btn.click(image_processor, inputs=[img1, img2], outputs=img3)
    clear_btn.click(clear_image, outputs=[img1, img2, img3])    

if __name__ == "__main__":
    demo.launch(share=True)
