import gradio as gr
import gradio.inputs


 #interacting with input and output directories

import pickle
from final_maybe import LanguageModel
with open('model.sav','rb') as handle:
    loaded_model = pickle.load(handle)
def fn(X_test):
    

    X_final = tuple(map(str, X_test.split(' ')))
    model = loaded_model
    result = model._best_candidate(X_final,0)
    
    return result
description = "Give two words as input and our model will predict the next word"
here = gr.Interface(fn=fn,
                     inputs= gradio.inputs.Textbox( lines=1, placeholder=None, default="", label=None),
                     outputs='text',
                     title="Next Word Prediction",
                     description=description,
                     theme="default",
                     allow_flagging="auto",
                     flagging_dir='flagging records')
#here.launch(inline=False, share = True)
if __name__ == "__main__":
    app, local_url, share_url = here.launch(share=True)


