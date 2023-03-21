import gradio as gr 

import pickle

grid_search = pickle.load(open('grid_search_svd.sav','rb'))

def recomendation_system(usuario, pelicula):
	estimated_rating = grid_search.predict(usuario, pelicula).est
	return round(estimated_rating,2)


# demo = gr.Interface(
# 	recomendation_system,
# 	[
# 		'text',
# 		'text'
# 	],
# 	"number",
# 	examples=[['124380','as5250']],
# 	title='Sistema de recomendaciones',
# 	description='Prediga el puntaje de una película por un usuario del catálogo de Amazon',
# )



with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
	gr.Markdown(
        """
	    # Sistema de recomendaciones
	    Prediga el puntaje de una película por un usuario del catálogo de **Amazon**.
	    """
    )
	usuario = gr.Textbox(label="Id Usuario")
	pelicula = gr.Textbox(label="Id Pelicula")
	output = gr.Textbox(label="Puntaje estimado")
	predict_btn = gr.Button("Predecir puntaje")
	predict_btn.click(fn=recomendation_system, inputs=[usuario,pelicula], outputs=output)


demo.launch()

