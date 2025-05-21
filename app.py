from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main():
    return 'Modelo de ejemplo MLOps'

@app.route("/train_pipeline")
def train_pipeline():
    try:
        from pipeline.train_pipeline import compile_pipeline, run_pipeline
        msg_compile = compile_pipeline()
        msg_run     = run_pipeline()
        return f"{msg_compile}\n{msg_run}"
    except Exception as e:
        import traceback
        return f"❌ Error en el endpoint /train_pipeline:\n{str(e)}\n{traceback.format_exc()}", 500

@app.route("/predict_pipeline")
def predict_pipeline():
    from pipeline.predict_pipeline import compile_pipeline, run_pipeline
    compile_pipeline()
    run_pipeline(scheduled=True)
    return 'Ejecución Correcta!'

@app.route("/on_demand_predict_pipeline")
def on_demand_predict_pipeline():
    from pipeline.predict_pipeline import compile_pipeline, run_pipeline
    compile_pipeline()
    run_pipeline(scheduled=False)
    return 'Ejecución Correcta!'

@app.route("/monitoring")
def monitoring():
    from pipeline.monitoring_prediction import all_models
    render_ = all_models()
    
    return render_

