import gradio as gr 

import pickle

grid_search = pickle.load(open('grid_search_svd.sav','rb'))

def greet(usuario, peli):
	res = grid_search.predict(usuario, peli).est
	return round(res,2)


demo = gr.Interface(
	fn=greet, 
	inputs=['text', 'text'],
	outputs="number"
	)

demo.launch()